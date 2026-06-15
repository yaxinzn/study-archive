#!/usr/bin/env python3
from pathlib import Path
from urllib.parse import unquote, urlsplit
import os
import re
import subprocess

REPO = Path(__file__).resolve().parents[1]
READING = REPO / "_data" / "reading.yml"
NEWS = REPO / "_data" / "news.yml"
MANUAL = REPO / "_data" / "news_manual.yml"

NEWS_LIMIT = int(os.environ.get("NEWS_LIMIT", "500"))

PDF_STEM_RE = re.compile(
    r"([A-Za-z][A-Za-z0-9]*(?:_[A-Za-z0-9]+)+_(?:AER|QJE|JPE|JF|JFE|RFS|RES|REStat|RESTat|Econometrica|AEJMacro|AEJApplied|AEJEP|TAR|JDE|JET)_?(?:19|20)\d{2})(?:\(\d+\))?\.pdf",
    re.I,
)

MAINTENANCE_SUBJECTS = (
    "Correct reading news dates",
    "Apply explicit reading news dates",
    "Fix reading news dates",
    "Restore per-paper reading news entries",
    "Repair automatic reading news generation",
    "Deduplicate automatic reading news",
    "Regenerate reading news",
    "Show manual per-paper reading news on updates page",
)

def run_git(args, allow_fail=True):
    try:
        return subprocess.check_output(
            ["git"] + args,
            cwd=str(REPO),
            text=True,
            stderr=subprocess.DEVNULL,
        )
    except subprocess.CalledProcessError:
        if allow_fail:
            return ""
        raise

def yaml_quote(s):
    return '"' + (s or "").replace("\\", "\\\\").replace('"', '\\"') + '"'

def clean_subject(s):
    s = re.sub(r"\s+", " ", (s or "").strip())
    s = re.sub(r"\s*\[skip ci\]\s*", "", s, flags=re.I)
    s = re.sub(r"\s*\[ci skip\]\s*", "", s, flags=re.I)
    return s.strip()

def stem_from_value(value):
    raw = (value or "").strip().strip('"').strip("'")
    if not raw:
        return ""

    no_query = raw.split("?", 1)[0].split("#", 1)[0]

    if "://" in no_query:
        filename = Path(unquote(urlsplit(raw).path)).name
    else:
        filename = Path(unquote(no_query)).name

    if not filename.lower().endswith(".pdf"):
        return ""

    stem = filename[:-4]
    stem = re.sub(r"\(\d+\)$", "", stem)
    return stem

def parse_reading_stems(text):
    stems = []
    seen = set()
    blocks = []
    current = []

    for line in text.splitlines(keepends=True):
        if line.startswith("- title:") and current:
            blocks.append("".join(current))
            current = [line]
        else:
            current.append(line)

    if current:
        blocks.append("".join(current))

    for block in blocks:
        file_match = re.search(r'(?m)^\s*file:\s*["\']?(.*?)["\']?\s*$', block)
        stem = stem_from_value(file_match.group(1)) if file_match else ""

        if not stem:
            m = PDF_STEM_RE.search(block)
            if m:
                stem = m.group(1)
                stem = re.sub(r"\(\d+\)$", "", stem)

        if stem and stem not in seen:
            stems.append(stem)
            seen.add(stem)

    return stems

def parse_news_items(path):
    if not path.exists():
        return []

    txt = path.read_text(encoding="utf-8", errors="replace")
    items = []
    cur_date = None

    for line in txt.splitlines():
        m_date = re.match(r'^\s*-\s*date:\s*"?([^"\n]+)"?\s*$', line)
        if m_date:
            cur_date = m_date.group(1).strip()
            continue

        m_title = re.match(r'^\s*title:\s*"?([^"\n]+)"?\s*$', line)
        if m_title and cur_date:
            items.append((cur_date, m_title.group(1).strip()))
            cur_date = None

    return items

def is_reading_title(title):
    return bool(re.match(r"^Reading:\s+add/update\s+.+\.pdf$", title or ""))

def is_maintenance_subject(title):
    return any((title or "").startswith(x) for x in MAINTENANCE_SUBJECTS)

entries = []
seen_titles = set()

log = run_git([
    "log",
    "--reverse",
    "--format=%H%x1f%cI%x1f%cs",
    "--",
    "_data/reading.yml",
])

order = 0

for line in log.splitlines():
    if "\x1f" not in line:
        continue

    sha, iso_dt, short_date = line.split("\x1f", 2)
    content = run_git(["show", f"{sha}:_data/reading.yml"])

    for stem in parse_reading_stems(content):
        title = f"Reading: add/update {stem}.pdf"

        if title in seen_titles:
            continue

        entries.append({
            "date": short_date,
            "title": title,
            "sort": iso_dt,
            "order": order,
        })
        seen_titles.add(title)
        order += 1

current_text = READING.read_text(encoding="utf-8", errors="replace") if READING.exists() else ""
existing_dates = {}

for d, title in parse_news_items(MANUAL) + parse_news_items(NEWS):
    existing_dates.setdefault(title, d)

for stem in parse_reading_stems(current_text):
    title = f"Reading: add/update {stem}.pdf"
    if title in seen_titles:
        continue

    fallback_date = existing_dates.get(title, run_git(["log", "-1", "--format=%cs", "--", "_data/reading.yml"]).strip())
    fallback_sort = fallback_date + "T00:00:00+00:00"

    entries.append({
        "date": fallback_date,
        "title": title,
        "sort": fallback_sort,
        "order": order,
    })
    seen_titles.add(title)
    order += 1

manual_nonreading = []

for d, title in parse_news_items(MANUAL) + parse_news_items(NEWS):
    if is_reading_title(title):
        continue
    if is_maintenance_subject(title):
        continue
    if title in seen_titles:
        continue

    entries.append({
        "date": d,
        "title": title,
        "sort": d + "T00:00:00+00:00",
        "order": order,
    })
    manual_nonreading.append((d, title))
    seen_titles.add(title)
    order += 1

raw_commits = run_git([
    "log",
    "--first-parent",
    f"--max-count={NEWS_LIMIT}",
    "--format=%cI%x1f%cs%x1f%s",
])

for line in raw_commits.splitlines():
    if "\x1f" not in line:
        continue

    iso_dt, short_date, subject = line.split("\x1f", 2)
    subject = clean_subject(subject)

    if not subject:
        continue

    lower = subject.lower()
    if lower.startswith("merge branch") or lower.startswith("merge pull request"):
        continue

    if lower.startswith("reading: add/update"):
        continue

    if is_maintenance_subject(subject):
        continue

    if subject in seen_titles:
        continue

    entries.append({
        "date": short_date,
        "title": subject,
        "sort": iso_dt,
        "order": order,
    })
    seen_titles.add(subject)
    order += 1

entries.sort(key=lambda x: (x["sort"], -x["order"]), reverse=True)

NEWS.write_text(
    "# Auto-generated from first appearance in _data/reading.yml and git commit history.\n"
    "# Reading paper dates are derived from the first commit where each PDF appears in _data/reading.yml.\n"
    + "\n".join(
        f"- date: {yaml_quote(x['date'])}\n  title: {yaml_quote(x['title'])}"
        for x in entries
    ).rstrip()
    + "\n",
    encoding="utf-8",
)

if manual_nonreading:
    MANUAL.write_text(
        "\n".join(
            f"- date: {yaml_quote(d)}\n  title: {yaml_quote(title)}"
            for d, title in manual_nonreading
        ).rstrip()
        + "\n",
        encoding="utf-8",
    )
else:
    MANUAL.write_text("[]\n", encoding="utf-8")

print(f"Wrote {NEWS.relative_to(REPO)} with {len(entries)} entries.")
print(f"Wrote {MANUAL.relative_to(REPO)} with {len(manual_nonreading)} non-reading manual entries.")

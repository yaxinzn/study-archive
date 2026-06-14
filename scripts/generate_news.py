#!/usr/bin/env python3
from pathlib import Path
from urllib.parse import unquote, urlsplit
import os
import re
import subprocess

REPO = Path(__file__).resolve().parents[1]
OUT = REPO / "_data" / "news.yml"
MANUAL = REPO / "_data" / "news_manual.yml"
OUT.parent.mkdir(exist_ok=True)

NEWS_LIMIT = int(os.environ.get("NEWS_LIMIT", "500"))
MAX_EXPANDED_READING_ITEMS = int(os.environ.get("MAX_EXPANDED_READING_ITEMS", "100"))

PDF_RE = re.compile(
    r"([A-Za-z][A-Za-z0-9]*(?:_[A-Za-z0-9]+)+_(?:AER|QJE|JPE|JF|JFE|RFS|RES|REStat|RESTat|Econometrica|AEJMacro|AEJApplied|AEJEP|TAR|JDE|JET)_?(?:19|20)\d{2}(?:\(\d+\))?\.pdf)"
)

def run_git(args, allow_fail=False):
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
    s = (s or "").strip()
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'

def clean_subject(s):
    s = re.sub(r"\s+", " ", (s or "").strip())
    s = re.sub(r"\s*\[skip ci\]\s*", "", s, flags=re.I)
    s = re.sub(r"\s*\[ci skip\]\s*", "", s, flags=re.I)
    return s.strip()

def label_from_value(value):
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
    return stem + ".pdf"

def labels_from_text(text):
    labels = []
    seen = set()

    for m in PDF_RE.finditer(text or ""):
        label = re.sub(r"\(\d+\)(?=\.pdf$)", "", m.group(1))
        if label not in seen:
            labels.append(label)
            seen.add(label)

    for raw in re.findall(r"https://www\.dropbox\.com/[^\s\"']+?\.pdf(?:\?[^\s\"']*)?", text or ""):
        label = label_from_value(raw)
        if label and label not in seen:
            labels.append(label)
            seen.add(label)

    for raw in re.findall(r"(?m)^\+?\s*(?:file|filename|pdf_url|dropbox_path):\s*(.*?)\s*$", text or ""):
        label = label_from_value(raw)
        if label and label not in seen:
            labels.append(label)
            seen.add(label)

    return labels

def commit_changed_paths(sha):
    raw = run_git(["show", "--name-only", "--format=", sha], allow_fail=True)
    return {line.strip() for line in raw.splitlines() if line.strip()}

def commit_diff_text(sha):
    return run_git(
        [
            "show",
            "--format=",
            "--unified=0",
            "--",
            "_data/reading.yml",
            "_data/dropbox_pdf_links.yml",
            "reading/library",
        ],
        allow_fail=True,
    )

def reading_labels_from_commit(sha):
    diff = commit_diff_text(sha)
    added = []

    for line in diff.splitlines():
        if line.startswith("+++") or line.startswith("---"):
            continue
        if line.startswith("+"):
            added.append(line[1:])

    labels = labels_from_text("\n".join(added))
    if len(labels) > MAX_EXPANDED_READING_ITEMS:
        return []
    return labels

def direct_pdf_labels_from_commit(sha):
    raw = run_git(["show", "--name-status", "--format=", sha], allow_fail=True)
    labels = []
    seen = set()

    for line in raw.splitlines():
        parts = line.split("\t")
        if len(parts) < 2:
            continue

        status = parts[0][:1]
        path = parts[-1]

        if status not in {"A", "M", "R"}:
            continue
        if not path.startswith("reading/library/"):
            continue
        if not path.lower().endswith(".pdf"):
            continue

        label = label_from_value(path)
        if label and label not in seen:
            labels.append(label)
            seen.add(label)

    return labels

def titles_for_commit(sha, subject):
    subject = clean_subject(subject)

    if re.match(r"^Reading:\s+add/update\s+.+\.pdf$", subject, flags=re.I):
        return [subject]

    paths = commit_changed_paths(sha)
    labels = []

    if (
        "_data/reading.yml" in paths
        or "_data/dropbox_pdf_links.yml" in paths
        or any(p.startswith("reading/library/") for p in paths)
    ):
        labels.extend(reading_labels_from_commit(sha))
        labels.extend(direct_pdf_labels_from_commit(sha))

    deduped = []
    seen = set()
    for label in labels:
        if label not in seen:
            deduped.append(label)
            seen.add(label)

    if 1 <= len(deduped) <= MAX_EXPANDED_READING_ITEMS:
        return [f"Reading: add/update {label}" for label in deduped]

    if subject:
        lower = subject.lower()
        if not lower.startswith("merge branch") and not lower.startswith("merge pull request"):
            return [subject]

    return []

def load_manual_items():
    if not MANUAL.exists():
        return []

    txt = MANUAL.read_text(encoding="utf-8", errors="replace")
    items = []
    current_date = None

    for line in txt.splitlines():
        m_date = re.match(r'^\s*-\s*date:\s*"?([^"\n]+)"?\s*$', line)
        if m_date:
            current_date = m_date.group(1).strip()
            continue

        m_title = re.match(r'^\s*title:\s*"?([^"\n]+)"?\s*$', line)
        if m_title and current_date:
            items.append((current_date, m_title.group(1).strip()))
            current_date = None

    return items

items = []
seen = set()

for date, title in load_manual_items():
    key = (date, title)
    if key not in seen:
        seen.add(key)
        items.append((date, title))

raw_log = run_git([
    "log",
    "--first-parent",
    f"--max-count={NEWS_LIMIT}",
    "--date=short",
    "--pretty=format:%H%x1f%cd%x1f%s",
])

for line in raw_log.splitlines():
    if "\x1f" not in line:
        continue

    sha, date, subject = line.split("\x1f", 2)

    for title in titles_for_commit(sha, subject):
        key = (date, title)
        if key in seen:
            continue
        seen.add(key)
        items.append((date, title))

with OUT.open("w", encoding="utf-8") as f:
    f.write("# Auto-generated from git commit history by scripts/generate_news.py\n")
    f.write("# Manual backfills are read from _data/news_manual.yml.\n")
    for date, title in items:
        f.write(f"- date: {yaml_quote(date)}\n")
        f.write(f"  title: {yaml_quote(title)}\n")

print(f"Wrote {OUT.relative_to(REPO)} with {len(items)} entries.")

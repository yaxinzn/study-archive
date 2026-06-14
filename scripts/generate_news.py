#!/usr/bin/env python3
from pathlib import Path
from urllib.parse import unquote, urlsplit
import os
import re
import subprocess

REPO = Path(__file__).resolve().parents[1]
OUT = REPO / "_data" / "news.yml"
OUT.parent.mkdir(exist_ok=True)

NEWS_LIMIT = int(os.environ.get("NEWS_LIMIT", "300"))
MAX_EXPANDED_READING_ITEMS = int(os.environ.get("MAX_EXPANDED_READING_ITEMS", "50"))

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

def label_from_file_value(value):
    raw = (value or "").strip().strip('"').strip("'")
    if not raw:
        return ""

    no_query = raw.split("?", 1)[0].split("#", 1)[0]

    if "://" in no_query:
        path = urlsplit(raw).path
        filename = Path(unquote(path)).name
    else:
        filename = Path(unquote(no_query)).name

    if not filename:
        return ""

    if not filename.lower().endswith(".pdf"):
        return ""

    stem = filename[:-4]
    stem = re.sub(r"\(\d+\)$", "", stem)
    return stem + ".pdf"

def extract_scalar(block, key):
    m = re.search(rf"(?m)^\s*{re.escape(key)}:\s*(.*?)\s*$", block)
    if not m:
        return ""

    val = m.group(1).strip()
    if (val.startswith('"') and val.endswith('"')) or (val.startswith("'") and val.endswith("'")):
        val = val[1:-1]

    return val.strip()

def parse_reading_entries(text):
    entries = []
    current = []

    for line in text.splitlines(keepends=True):
        if line.startswith("- title:") and current:
            entries.append("".join(current).rstrip())
            current = [line]
        else:
            current.append(line)

    if current:
        entries.append("".join(current).rstrip())

    parsed = []

    for block in entries:
        if not block.strip().startswith("- title:"):
            continue

        file_value = extract_scalar(block, "file")
        label = label_from_file_value(file_value)
        if not label:
            continue

        normalized_block = re.sub(r"\s+", " ", block).strip()
        parsed.append((label, normalized_block))

    return parsed

def get_commit_file(sha, path):
    return run_git(["show", f"{sha}:{path}"], allow_fail=True)

def get_commit_parent_file(sha, path):
    return run_git(["show", f"{sha}^:{path}"], allow_fail=True)

def name_status_rows(sha):
    raw = run_git(["show", "--name-status", "--format=", sha], allow_fail=True)
    rows = []

    for line in raw.splitlines():
        parts = line.split("\t")
        if len(parts) >= 2:
            status = parts[0]
            path = parts[-1]
            rows.append((status, path, parts))

    return rows

def commit_changes_path(sha, wanted_path):
    for _status, path, parts in name_status_rows(sha):
        if path == wanted_path or wanted_path in parts[1:]:
            return True
    return False

def reading_items_changed_in_commit(sha):
    old_text = get_commit_parent_file(sha, "_data/reading.yml")
    new_text = get_commit_file(sha, "_data/reading.yml")

    if not new_text:
        return []

    old_entries = dict(parse_reading_entries(old_text))
    new_entries = parse_reading_entries(new_text)

    changed = []
    seen = set()

    for label, block in new_entries:
        if old_entries.get(label) != block and label not in seen:
            changed.append(label)
            seen.add(label)

    return changed

def pdf_paths_changed_in_commit(sha):
    labels = []
    seen = set()

    for status, path, _parts in name_status_rows(sha):
        status_kind = status[:1]

        if status_kind not in {"A", "M", "R"}:
            continue

        if not path.startswith("reading/library/"):
            continue

        if not path.lower().endswith(".pdf"):
            continue

        label = label_from_file_value(path)
        if label and label not in seen:
            labels.append(label)
            seen.add(label)

    return labels

def news_titles_for_commit(sha, subject):
    subject = clean_subject(subject)

    # Keep old-style one-paper reading commit messages exactly as they are.
    if re.match(r"^Reading:\s+add/update\s+.+\.pdf$", subject, flags=re.I):
        return [subject]

    # Expand small reading.yml updates into one news entry per paper.
    if commit_changes_path(sha, "_data/reading.yml"):
        changed_labels = reading_items_changed_in_commit(sha)

        if 1 <= len(changed_labels) <= MAX_EXPANDED_READING_ITEMS:
            return [f"Reading: add/update {label}" for label in changed_labels]

        # Avoid creating thousands of news rows for migration commits.
        if len(changed_labels) > MAX_EXPANDED_READING_ITEMS:
            return [subject or f"Reading: add/update {len(changed_labels)} papers"]

    # Also expand small direct PDF add/update commits when applicable.
    changed_pdf_labels = pdf_paths_changed_in_commit(sha)
    if 1 <= len(changed_pdf_labels) <= MAX_EXPANDED_READING_ITEMS:
        return [f"Reading: add/update {label}" for label in changed_pdf_labels]

    if not subject:
        return []

    lower = subject.lower()
    if lower.startswith("merge branch") or lower.startswith("merge pull request"):
        return []

    return [subject]

raw_log = run_git([
    "log",
    "--first-parent",
    f"--max-count={NEWS_LIMIT}",
    "--date=short",
    "--pretty=format:%H%x1f%cd%x1f%s",
])

items = []
seen = set()

for line in raw_log.splitlines():
    if "\x1f" not in line:
        continue

    sha, date, subject = line.split("\x1f", 2)

    for title in news_titles_for_commit(sha, subject):
        key = (date, title)
        if key in seen:
            continue

        seen.add(key)
        items.append((date, title))

with OUT.open("w", encoding="utf-8") as f:
    f.write("# Auto-generated from git commit history by scripts/generate_news.py\n")
    f.write("# Reading commits that change _data/reading.yml are expanded into per-paper rows.\n")
    for date, title in items:
        f.write(f"- date: {yaml_quote(date)}\n")
        f.write(f"  title: {yaml_quote(title)}\n")

print(f"Wrote {OUT.relative_to(REPO)} with {len(items)} entries.")

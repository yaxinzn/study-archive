#!/usr/bin/env python3
from pathlib import Path
import os
import re
import subprocess

REPO = Path(__file__).resolve().parents[1]
OUT = REPO / "_data" / "news.yml"
MANUAL = REPO / "_data" / "news_manual.yml"
OUT.parent.mkdir(exist_ok=True)

NEWS_LIMIT = int(os.environ.get("NEWS_LIMIT", "500"))

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
    s = (s or "").strip()
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'

def clean_subject(s):
    s = re.sub(r"\s+", " ", (s or "").strip())
    s = re.sub(r"\s*\[skip ci\]\s*", "", s, flags=re.I)
    s = re.sub(r"\s*\[ci skip\]\s*", "", s, flags=re.I)
    return s.strip()

def load_items(path):
    if not path.exists():
        return []
    txt = path.read_text(encoding="utf-8", errors="replace")
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
seen_titles = set()

for d, title in load_items(MANUAL):
    if title not in seen_titles:
        items.append((d, title))
        seen_titles.add(title)

raw = run_git([
    "log",
    "--first-parent",
    f"--max-count={NEWS_LIMIT}",
    "--date=short",
    "--pretty=format:%cd%x1f%s",
])

for line in raw.splitlines():
    if "\x1f" not in line:
        continue
    d, subject = line.split("\x1f", 1)
    subject = clean_subject(subject)
    if not subject:
        continue
    lower = subject.lower()
    if lower.startswith("merge branch") or lower.startswith("merge pull request"):
        continue
    if subject in seen_titles:
        continue
    items.append((d, subject))
    seen_titles.add(subject)

with OUT.open("w", encoding="utf-8") as f:
    f.write("# Auto-generated from _data/news_manual.yml and git commit history.\n")
    for d, title in items:
        f.write(f"- date: {yaml_quote(d)}\n")
        f.write(f"  title: {yaml_quote(title)}\n")

print(f"Wrote {OUT.relative_to(REPO)} with {len(items)} entries.")

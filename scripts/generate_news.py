#!/usr/bin/env python3
from pathlib import Path
import os
import re
import subprocess

REPO = Path(__file__).resolve().parents[1]
OUT = REPO / "_data" / "news.yml"
OUT.parent.mkdir(exist_ok=True)

NEWS_LIMIT = int(os.environ.get("NEWS_LIMIT", "300"))

def run_git(args):
    return subprocess.check_output(
        ["git"] + args,
        cwd=str(REPO),
        text=True,
        stderr=subprocess.DEVNULL,
    )

def yaml_quote(s):
    s = (s or "").strip()
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'

def clean_subject(s):
    s = re.sub(r"\s+", " ", (s or "").strip())
    s = re.sub(r"\s*\[skip ci\]\s*", "", s, flags=re.I)
    s = re.sub(r"\s*\[ci skip\]\s*", "", s, flags=re.I)
    return s.strip()

raw = run_git([
    "log",
    "--first-parent",
    f"--max-count={NEWS_LIMIT}",
    "--date=short",
    "--pretty=format:%cd%x1f%s",
])

items = []
seen = set()

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

    if subject in seen:
        continue

    seen.add(subject)
    items.append((d, subject))

with OUT.open("w", encoding="utf-8") as f:
    f.write("# Auto-generated update history from git commits.\n")
    for d, subject in items:
        f.write(f"- date: {yaml_quote(d)}\n")
        f.write(f"  title: {yaml_quote(subject)}\n")

print(f"Wrote {OUT.relative_to(REPO)} with {len(items)} entries.")

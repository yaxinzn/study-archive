#!/usr/bin/env bash
set -euo pipefail

SRC="${1:-}"
TITLE="${2:-}"
DESC="${3:-}"

if [[ -z "$SRC" || -z "$TITLE" || -z "$DESC" ]]; then
  echo 'Usage: ./scripts/add_reading_paper.sh "/path/to/file.pdf" "TITLE" "ONE-SENTENCE DESC"'
  exit 1
fi

REPO="$(git rev-parse --show-toplevel 2>/dev/null || true)"
if [[ -z "$REPO" ]]; then
  echo "ERROR: not inside a git repo"
  exit 1
fi
cd "$REPO"

# stop if a rebase is in progress
if [[ -d ".git/rebase-merge" || -d ".git/rebase-apply" ]]; then
  echo "ERROR: rebase in progress. Finish it first: git rebase --continue OR git rebase --abort"
  exit 1
fi

# Always work on main
cur="$(git branch --show-current)"
if [[ "$cur" != "main" ]]; then
  git checkout main
fi

safe_pull_rebase () {
  # Try git's native autostash first
  if git pull --rebase --autostash origin main >/dev/null 2>&1; then
    return 0
  fi

  # Fallback: manual stash
  local need_stash=0
  if ! git diff --quiet || ! git diff --cached --quiet || [[ -n "$(git ls-files --others --exclude-standard)" ]]; then
    git stash push -u -m "autostash(add_reading_paper)" >/dev/null || true
    need_stash=1
  fi

  git pull --rebase origin main

  if [[ $need_stash -eq 1 ]]; then
    git stash pop >/dev/null || true
  fi
}

safe_pull_rebase

if [[ ! -r "$SRC" ]]; then
  echo "ERROR: cannot read PDF: $SRC"
  ls -l "$SRC" 2>/dev/null || true
  exit 1
fi

mkdir -p reading/library _data

# stable ASCII filename
export SRC_BASENAME
SRC_BASENAME="$(basename "$SRC")"

DST_NAME="$(python3 - <<'PY'
import os, re
base = os.environ.get("SRC_BASENAME","")
base = re.sub(r"\s+", "_", base)
base = re.sub(r"[()]", "", base)
base = re.sub(r"[^A-Za-z0-9._-]", "_", base)
if not base.lower().endswith(".pdf"):
    base += ".pdf"
print(base, end="")
PY
)"

cp "$SRC" "reading/library/$DST_NAME"

# Upsert into _data/reading.yml by file name (update title/desc if exists, else prepend)
export TITLE DESC DST_NAME
python3 - <<'PY'
from pathlib import Path
import os, re

yml = Path("_data/reading.yml")
title = os.environ["TITLE"]
desc  = os.environ["DESC"]
file  = os.environ["DST_NAME"]

def esc(x: str) -> str:
    return x.replace('"', '\\"')

title_e = esc(title)
desc_e  = esc(desc)
file_e  = esc(file)

new_block = f'''- title: "{title_e}"
  file: "{file_e}"
  desc: "{desc_e}"
'''

txt = yml.read_text(encoding="utf-8") if yml.exists() else ""
pat = re.compile(r'(?ms)^- title: ".*?"\n  file: "' + re.escape(file_e) + r'"\n  desc: ".*?"\n')

if pat.search(txt):
    txt2 = pat.sub(new_block, txt, count=1)
else:
    txt2 = (new_block + "\n" + txt.lstrip()).rstrip() + "\n"

yml.write_text(txt2, encoding="utf-8")
print("Updated _data/reading.yml")
PY

git add "reading/library/$DST_NAME" "_data/reading.yml"
git commit -m "Reading: add/update ${DST_NAME}" || echo "Nothing to commit"

# Remote may have advanced (e.g., workflows) — rebase again safely, then push
safe_pull_rebase

# Push with one retry if remote advanced again
if ! git push origin main; then
  safe_pull_rebase
  git push origin main
fi

echo "✅ Added/updated: $DST_NAME"
echo "Reading page: https://yaxinzn.github.io/study-archive/reading/"
echo "PDF:          https://yaxinzn.github.io/study-archive/reading/library/$DST_NAME"

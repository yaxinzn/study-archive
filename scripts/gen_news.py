import subprocess
from pathlib import Path

def run(cmd):
    return subprocess.check_output(cmd, text=True).strip()

def yq(s: str) -> str:
    # YAML-safe double-quoted string
    s = s.replace("\\", "\\\\").replace('"', '\\"')
    return f'"{s}"'

# Grab last commits that touched materials/ or index.md
# title = commit subject, date = YYYY-MM-DD
log = run([
    "git", "log",
    "--date=short",
    "--pretty=format:%ad|%s",
    "-n", "12",
    "--",
    "materials",
    "index.md",
])

items = []
for line in log.splitlines():
    if "|" not in line:
        continue
    date, title = line.split("|", 1)
    title = title.strip()
    date = date.strip()
    # (Optional) you can customize "note" later; keep blank by default
    items.append({"date": date, "title": title})

out = ["# Auto-generated from git log. Do not edit manually.\n"]
for it in items:
    out.append(f"- date: {yq(it['date'])}\n")
    out.append(f"  title: {yq(it['title'])}\n")

Path("_data/news.yml").write_text("".join(out), encoding="utf-8")
print("Wrote _data/news.yml with", len(items), "items")

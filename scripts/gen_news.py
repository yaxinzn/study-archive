import subprocess
from pathlib import Path

NEWS_PATH = Path("_data/news.yml")
MAX_COMMITS_SCAN = 1000  # how far back to scan git log
TRACK_PATHS = ["materials", "index.md", "updates", "updates/index.md"]

def run(cmd):
    return subprocess.check_output(cmd, text=True).strip()

def load_existing():
    if not NEWS_PATH.exists():
        return [], set()
    lines = NEWS_PATH.read_text(encoding="utf-8").splitlines()
    items = []
    keys = set()
    cur = {}
    for line in lines:
        line = line.rstrip()
        if line.startswith("- "):
            if cur:
                items.append(cur)
                k = f"{cur.get('date','')}|{cur.get('title','')}"
                keys.add(k)
            cur = {}
            # "- date: "YYYY-MM-DD""
            if "date:" in line:
                cur["date"] = line.split("date:", 1)[1].strip().strip('"')
        elif line.strip().startswith("title:"):
            cur["title"] = line.split("title:", 1)[1].strip().strip('"')
        elif line.strip().startswith("note:"):
            cur["note"] = line.split("note:", 1)[1].strip().strip('"')
    if cur:
        items.append(cur)
        k = f"{cur.get('date','')}|{cur.get('title','')}"
        keys.add(k)
    return items, keys

def yaml_quote(s: str) -> str:
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'

# Scan git log (date + subject) for tracked paths
log = run([
    "git", "log",
    "--date=short",
    "--pretty=format:%ad|%s",
    f"-n", str(MAX_COMMITS_SCAN),
    "--",
    *TRACK_PATHS,
])

existing_items, existing_keys = load_existing()

new_items = []
for line in log.splitlines():
    if "|" not in line:
        continue
    date, title = line.split("|", 1)
    date = date.strip()
    title = title.strip()
    key = f"{date}|{title}"
    if key not in existing_keys:
        new_items.append({"date": date, "title": title})

# Keep newest first on page: prepend new commits to the top, keep old ones below
all_items = new_items + existing_items

out = ["# Auto-generated update history (append-only). Do not edit manually.\n"]
for it in all_items:
    out.append(f"- date: {yaml_quote(it['date'])}\n")
    out.append(f"  title: {yaml_quote(it['title'])}\n")
    if it.get("note"):
        out.append(f"  note: {yaml_quote(it['note'])}\n")

NEWS_PATH.write_text("".join(out), encoding="utf-8")
print(f"Wrote {NEWS_PATH} with {len(all_items)} items ({len(new_items)} new).")

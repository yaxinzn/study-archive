import subprocess
from pathlib import Path

NEWS_PATH = Path("_data/news.yml")

# Scan enough history; raise if you want (bigger = slower)
MAX_COMMITS_SCAN = 5000

TRACK_PATHS = ["materials", "index.md", "updates", "updates/index.md"]

def run(cmd):
    return subprocess.check_output(cmd, text=True).strip()

def yaml_quote(s: str) -> str:
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'

def load_existing():
    """Load existing YAML items (best-effort) and keep any ts/date/title/note."""
    if not NEWS_PATH.exists():
        return {}

    items = {}
    cur = None
    for raw in NEWS_PATH.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if line.startswith("- "):
            # start new item
            cur = {}
            # "- date: "YYYY-MM-DD""
            if "date:" in line:
                cur["date"] = line.split("date:", 1)[1].strip().strip('"')
            items[id(cur)] = cur
        elif cur is not None:
            if line.startswith("ts:"):
                try:
                    cur["ts"] = int(line.split("ts:", 1)[1].strip().strip('"'))
                except:
                    cur["ts"] = 0
            elif line.startswith("title:"):
                cur["title"] = line.split("title:", 1)[1].strip().strip('"')
            elif line.startswith("note:"):
                cur["note"] = line.split("note:", 1)[1].strip().strip('"')

    # Convert to key map
    keyed = {}
    for _, it in items.items():
        date = it.get("date", "")
        title = it.get("title", "")
        if date and title:
            keyed[f"{date}|{title}"] = it
    return keyed

# Existing history (keyed by date|title)
existing = load_existing()

# Git log: timestamp|date|subject (newest first)
log = run([
    "git", "log",
    "--pretty=format:%ct|%ad|%s",
    "--date=short",
    "-n", str(MAX_COMMITS_SCAN),
    "--",
    *TRACK_PATHS,
])

# Merge: prefer git timestamp/date/title; keep existing note if present
merged = dict(existing)

for line in log.splitlines():
    parts = line.split("|", 2)
    if len(parts) != 3:
        continue
    ts_s, date, title = parts
    try:
        ts = int(ts_s)
    except:
        ts = 0
    date = date.strip()
    title = title.strip()
    key = f"{date}|{title}"

    if key in merged:
        merged[key]["ts"] = max(ts, int(merged[key].get("ts", 0) or 0))
        merged[key]["date"] = date
        merged[key]["title"] = title
    else:
        merged[key] = {"ts": ts, "date": date, "title": title}

# Sort newest -> oldest (by ts, then date, then title)
sorted_items = sorted(
    merged.values(),
    key=lambda it: (int(it.get("ts", 0) or 0), it.get("date", ""), it.get("title", "")),
    reverse=True
)

out = ["# Auto-generated update history (sorted newest -> oldest). Do not edit manually.\n"]
for it in sorted_items:
    out.append(f"- ts: {yaml_quote(str(int(it.get('ts', 0) or 0)))}\n")
    out.append(f"  date: {yaml_quote(it.get('date',''))}\n")
    out.append(f"  title: {yaml_quote(it.get('title',''))}\n")
    if it.get("note"):
        out.append(f"  note: {yaml_quote(it['note'])}\n")

NEWS_PATH.write_text("".join(out), encoding="utf-8")
print(f"Wrote {NEWS_PATH} with {len(sorted_items)} items (newest -> oldest).")

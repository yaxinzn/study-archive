from pathlib import Path
import re

REPO_ROOT = Path(".")
MATERIALS = REPO_ROOT / "materials"

START = "<!-- AUTO-LIST-START -->"
END   = "<!-- AUTO-LIST-END -->"

def list_entries(folder: Path):
    # list only immediate children: folders + files
    entries = []
    for p in folder.iterdir():
        name = p.name
        if name.startswith(".") or name == "index.md" or name == ".DS_Store":
            continue
        if p.is_dir():
            # require trailing slash so Jekyll treats it as folder page
            entries.append(("dir", name + "/"))
        elif p.is_file():
            entries.append(("file", name))
    # sort dirs first, then files; both alphabetical
    entries.sort(key=lambda x: (0 if x[0]=="dir" else 1, x[1].lower()))
    return entries

def build_md_list(folder: Path):
    items = list_entries(folder)
    if not items:
        return "- (No files yet.)\n"
    lines = []
    for typ, name in items:
        # link relative to this index.md
        lines.append(f"- **[{name}]({name})**\n")
    return "".join(lines)

def ensure_front_matter(text: str, title_guess: str):
    # If file already has front matter, keep it
    if text.lstrip().startswith("---"):
        return text
    fm = f"""---
layout: sc
title: {title_guess}
hero_title: {title_guess}
hero_subtitle: Study materials
hero_desc: Notes, PDFs, and structured summaries for {title_guess}.
---

"""
    return fm + text.lstrip()

def update_index(index_path: Path, title_guess: str, body_list: str):
    txt = index_path.read_text(encoding="utf-8") if index_path.exists() else ""
    txt = ensure_front_matter(txt, title_guess)

    # If AUTO block exists, replace contents
    if START in txt and END in txt:
        pattern = re.compile(re.escape(START) + r"[\s\S]*?" + re.escape(END))
        replacement = START + "\n" + body_list + END
        txt2 = pattern.sub(replacement, txt, count=1)
    else:
        # Append a standard section at end
        if not txt.endswith("\n"):
            txt += "\n"
        txt2 = txt.rstrip() + "\n\n## Files\n" + START + "\n" + body_list + END + "\n"

    index_path.write_text(txt2, encoding="utf-8")

def main():
    if not MATERIALS.exists():
        raise SystemExit("materials/ not found")

    for folder in sorted([p for p in MATERIALS.iterdir() if p.is_dir() and not p.name.startswith(".")],
                         key=lambda p: p.name.lower()):
        index_path = folder / "index.md"

        # Title guess from folder name (with nicer mapping)
        name = folder.name
        pretty = name.replace("-", " ").title()
        title_map = {
            "Ap Empirical": "Asset Pricing (Empirical)",
            "Ap Theory": "Asset Pricing (Theory)",
            "Cf Empirical": "Corporate Finance (Empirical)",
            "Cf Theory": "Corporate Finance (Theory)",
            "Eio": "Empirical IO",
            "Macro Finance": "Macro-Finance",
            "Tfp Measurement": "TFP Measurement",
            "Math Foundations": "Math Foundations",
        }
        title_guess = title_map.get(pretty, pretty)

        body_list = build_md_list(folder)
        update_index(index_path, title_guess, body_list)

    print("✅ Auto-updated materials/*/index.md AUTO-LIST blocks.")

if __name__ == "__main__":
    main()

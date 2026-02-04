from pathlib import Path
import re

ROOT = Path(".")
MATERIALS = ROOT / "materials"

START = "<!-- AUTO-LIST-START -->"
END   = "<!-- AUTO-LIST-END -->"

def list_entries(folder: Path):
    entries = []
    for p in folder.iterdir():
        name = p.name
        if name.startswith(".") or name in {"index.md", ".DS_Store"}:
            continue
        if p.is_dir():
            entries.append(("dir", name + "/"))
        elif p.is_file():
            entries.append(("file", name))
    entries.sort(key=lambda x: (0 if x[0]=="dir" else 1, x[1].lower()))
    return entries

def build_md_list(folder: Path):
    items = list_entries(folder)
    if not items:
        return "- (No files yet.)\n"
    return "".join([f"- **[{name}]({name})**\n" for _, name in items])

def ensure_front_matter(text: str, title_guess: str):
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

def remove_section_by_heading_all(txt: str, heading_regex: str):
    # remove all sections whose heading matches heading_regex (e.g., ^## Files$)
    while True:
        m = re.search(heading_regex, txt, flags=re.IGNORECASE | re.MULTILINE)
        if not m:
            return txt
        start = m.start()
        after = txt.find("\n", m.end())
        after = after + 1 if after != -1 else len(txt)
        nxt = re.search(r"(?m)^##\s+", txt[after:])
        end = after + (nxt.start() if nxt else len(txt[after:]))
        txt = (txt[:start].rstrip() + "\n\n" + txt[end:].lstrip())

def title_guess_from_folder(folder: Path):
    pretty = folder.name.replace("-", " ").title()
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
    return title_map.get(pretty, pretty)

def main():
    if not MATERIALS.exists():
        raise SystemExit("materials/ not found")

    for folder in sorted([p for p in MATERIALS.iterdir() if p.is_dir() and not p.name.startswith(".")],
                         key=lambda p: p.name.lower()):
        idx = folder / "index.md"
        txt = idx.read_text(encoding="utf-8") if idx.exists() else ""

        title_guess = title_guess_from_folder(folder)
        txt = ensure_front_matter(txt, title_guess)

        # Remove duplicated sections entirely:
        # 1) remove Notes / files sections
        txt = remove_section_by_heading_all(txt, r"(?m)^##\s*Notes\s*/\s*files\s*$")
        # 2) remove ALL Files sections (we will add a single fresh one)
        txt = remove_section_by_heading_all(txt, r"(?m)^##\s*Files\s*$")

        # Append a single Files section with AUTO-LIST
        body = build_md_list(folder)
        txt = txt.rstrip() + f"\n\n## Files\n{START}\n{body}{END}\n"

        idx.write_text(txt, encoding="utf-8")

    print("✅ Updated all subjects: removed Notes/files; kept only Files (AUTO-LIST).")

if __name__ == "__main__":
    main()

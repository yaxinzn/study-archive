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

def remove_section_by_heading(txt: str, heading: str):
    # Remove a whole section starting from "## heading" until next "## "
    pat = re.compile(rf"(?im)^##\s*{re.escape(heading)}\s*$")
    m = pat.search(txt)
    if not m:
        return txt
    start = m.start()
    after = txt.find("\n", m.end())
    after = after + 1 if after != -1 else len(txt)
    nxt = re.search(r"(?m)^##\s+", txt[after:])
    end = after + (nxt.start() if nxt else len(txt[after:]))
    return (txt[:start].rstrip() + "\n\n" + txt[end:].lstrip())

def find_notes_heading(txt: str):
    # Match "## Notes / files" (case-insensitive, spaces flexible)
    pat = re.compile(r"(?im)^##\s*Notes\s*/\s*files\s*$")
    return pat.search(txt)

def ensure_notes_section(txt: str):
    m = find_notes_heading(txt)
    if m:
        return txt
    # If no Notes/files section, append one with a short editable manual note
    manual = "Add 1–2 sentences here as your manual description. The list below is auto-generated.\n"
    block = f"\n\n## Notes / files\n{manual}\n{START}\n- (No files yet.)\n{END}\n"
    return txt.rstrip() + block + "\n"

def upsert_auto_block_in_notes(txt: str, body_list: str):
    # Ensure Notes section exists
    txt = ensure_notes_section(txt)
    m = find_notes_heading(txt)
    # Find the section region: from after heading line to next ## heading
    sec_start = txt.find("\n", m.end())
    sec_start = sec_start + 1 if sec_start != -1 else len(txt)
    nxt = re.search(r"(?m)^##\s+", txt[sec_start:])
    sec_end = sec_start + (nxt.start() if nxt else len(txt[sec_start:]))

    section = txt[sec_start:sec_end]

    # If markers exist, replace only inside markers
    if START in section and END in section:
        pat = re.compile(re.escape(START) + r"[\s\S]*?" + re.escape(END))
        section2 = pat.sub(START + "\n" + body_list + END, section, count=1)
    else:
        # Otherwise, append markers at end of the Notes section (preserving manual text above)
        section2 = section.rstrip() + "\n\n" + START + "\n" + body_list + END + "\n"

    return txt[:sec_start] + section2 + txt[sec_end:]

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

        # Remove duplicated section "## Files" if present
        txt = remove_section_by_heading(txt, "Files")

        # Update only AUTO-LIST block inside Notes/files section
        body = build_md_list(folder)
        txt = upsert_auto_block_in_notes(txt, body)

        idx.write_text(txt, encoding="utf-8")

    print("✅ Updated all subjects: keep manual note + update only AUTO-LIST inside Notes/files.")

if __name__ == "__main__":
    main()

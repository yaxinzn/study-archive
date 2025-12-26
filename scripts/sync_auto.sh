#!/usr/bin/env bash
set -euo pipefail

cd "$(git rev-parse --show-toplevel)"

BASE="/Users/yaxinzheng/Library/CloudStorage/Dropbox/Study_Cycle"

# ---- folder name normalization rules ----
# Default mapping: lower-case, underscores -> hyphens
# Special cases handled below (because your website uses certain canonical names).
map_dest() {
  local folder="$1"
  local f_lc
  f_lc="$(echo "$folder" | tr '[:upper:]' '[:lower:]')"

  case "$f_lc" in
    eio)               echo "materials/eio" ;;
    micro)             echo "materials/micro" ;;               # Dropbox has "Micro"
    macro)             echo "materials/macro" ;;
    econometrics)      echo "materials/econometrics" ;;
    "math-foundations")echo "materials/math-foundations" ;;
    "ap-theory")       echo "materials/ap-theory" ;;
    "ap-empirical")    echo "materials/ap-empirical" ;;
    cf_theory)         echo "materials/cf-theory" ;;
    cf_empirical)      echo "materials/cf-empirical" ;;
    macrofinance)      echo "materials/macro-finance" ;;
    *)
      # default: underscores -> hyphens, keep lowercase
      echo "materials/${f_lc//_/-}"
      ;;
  esac
}

# Pretty titles (optional). If not matched, title = folder name.
title_for() {
  local folder="$1"
  local f_lc
  f_lc="$(echo "$folder" | tr '[:upper:]' '[:lower:]')"
  case "$f_lc" in
    eio) echo "Empirical IO" ;;
    micro) echo "Micro" ;;
    macro) echo "Macro" ;;
    econometrics) echo "Econometrics" ;;
    "math-foundations") echo "Math Foundations" ;;
    "ap-theory") echo "Asset Pricing (Theory)" ;;
    "ap-empirical") echo "Asset Pricing (Empirical)" ;;
    cf_theory) echo "Corporate Finance (Theory)" ;;
    cf_empirical) echo "Corporate Finance (Empirical)" ;;
    macrofinance) echo "Macro-Finance" ;;
    *) echo "$folder" ;;
  esac
}

# Simple scope text (optional). If missing, uses a placeholder.
scope_for() {
  local folder="$1"
  local f_lc
  f_lc="$(echo "$folder" | tr '[:upper:]' '[:lower:]')"
  case "$f_lc" in
    eio) echo "Demand estimation, cost/production, competition and conduct, entry/exit, identification, and counterfactual analysis." ;;
    micro) echo "Preferences, uncertainty, general equilibrium, and mechanisms." ;;
    macro) echo "Growth, business cycles, and monetary frameworks." ;;
    econometrics) echo "Identification, estimation, inference, and robustness." ;;
    "math-foundations") echo "Linear algebra, probability, optimization, and analysis." ;;
    "ap-theory") echo "SDF, no-arbitrage, and equilibrium pricing." ;;
    "ap-empirical") echo "Factors, predictability, anomalies, and methods." ;;
    cf_theory) echo "Contracting, capital structure, governance, and core theory mechanisms." ;;
    cf_empirical) echo "Causal designs, measurement, and empirical firm behavior." ;;
    macrofinance) echo "Risk premia, term structure, and policy transmission." ;;
    *) echo "Notes and PDFs for $folder." ;;
  esac
}

gen_index() {
  local dst="$1"
  local title="$2"
  local scope="$3"

  python3 - <<PY
from pathlib import Path
dst = Path("$dst")
pdfs = sorted(dst.glob("*.pdf"), key=lambda p: p.name.lower())
lines = []
lines += [f"# {title}\n\n"]
lines += ["## Scope\n", f"{scope}\n\n"]
lines += ["## Notes / files\n"]
if not pdfs:
    lines += ["- (No PDFs found.)\n"]
else:
    for p in pdfs:
        lines.append(f"- **[{p.name}]({p.name})**\n")
(dst / "index.md").write_text("".join(lines), encoding="utf-8")
print("index.md updated:", dst / "index.md", "PDFs:", len(pdfs))
PY
}

sync_folder() {
  local folder="$1"
  local src="$BASE/$folder"
  local dst
  dst="$(map_dest "$folder")"

  local title scope
  title="$(title_for "$folder")"
  scope="$(scope_for "$folder")"

  mkdir -p "$dst"

  echo "==> Sync: $folder"
  echo "    from: $src"
  echo "    to:   $dst"

  # Sync PDFs only (overwrite updates; delete removed)
  rsync -av --delete \
    --include="*/" \
    --include="*.pdf" \
    --exclude="*" \
    "$src/" "$dst/"

  gen_index "$dst" "$title" "$scope"

  git add "$dst"
  if ! git diff --cached --quiet; then
    git commit -m "Update ${dst#materials/} materials"
  else
    echo "    No changes to commit for $folder"
  fi
}

usage() {
  echo "Usage:"
  echo "  $0 all            # sync all folders under Study_Cycle"
  echo "  $0 <foldername>   # sync one folder (e.g., EIO, cf_theory, Micro)"
}

main() {
  if [[ $# -ne 1 ]]; then usage; exit 1; fi
  local target="$1"

  if [[ ! -d "$BASE" ]]; then
    echo "ERROR: Study_Cycle not found: $BASE"
    exit 1
  fi

  if [[ "$target" == "all" ]]; then
    for d in "$BASE"/*; do
      [[ -d "$d" ]] || continue
      folder="$(basename "$d")"
      # skip folders you don't want to publish:
      if [[ "$folder" == "Terminal" ]]; then
        echo "==> Skip: $folder"
        continue
      fi
      sync_folder "$folder"
    done
  else
    if [[ ! -d "$BASE/$target" ]]; then
      echo "ERROR: folder not found: $BASE/$target"
      exit 1
    fi
    sync_folder "$target"
  fi

  # avoid push rejection if remote got updated (e.g., your news workflow)
  git pull --rebase origin main || true
  git push origin main
  echo "✅ Done."
}

main "$@"

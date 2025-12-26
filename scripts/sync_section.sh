#!/usr/bin/env bash
set -euo pipefail

cd "$(git rev-parse --show-toplevel)"

# Dropbox base
BASE="/Users/yaxinzheng/Library/CloudStorage/Dropbox/Study_Cycle"

# section -> (Dropbox source, repo dest)
declare -A SRC=(
  [eio]="$BASE/EIO"
  [cf-theory]="$BASE/cf_theory"
  [cf-empirical]="$BASE/cf_empirical"
  [econometrics]="$BASE/econometrics"
  [micro]="$BASE/Micro"
  [macro]="$BASE/macro"
  [math-foundations]="$BASE/math-foundations"
  [ap-theory]="$BASE/ap-theory"
  [ap-empirical]="$BASE/ap-empirical"
  [macro-finance]="$BASE/macrofinance"
)

declare -A DEST=(
  [eio]="materials/eio"
  [cf-theory]="materials/cf-theory"
  [cf-empirical]="materials/cf-empirical"
  [econometrics]="materials/econometrics"
  [micro]="materials/micro"
  [macro]="materials/macro"
  [math-foundations]="materials/math-foundations"
  [ap-theory]="materials/ap-theory"
  [ap-empirical]="materials/ap-empirical"
  [macro-finance]="materials/macro-finance"
)

declare -A TITLE=(
  [eio]="Empirical IO"
  [cf-theory]="Corporate Finance (Theory)"
  [cf-empirical]="Corporate Finance (Empirical)"
  [econometrics]="Econometrics"
  [micro]="Micro"
  [macro]="Macro"
  [math-foundations]="Math Foundations"
  [ap-theory]="Asset Pricing (Theory)"
  [ap-empirical]="Asset Pricing (Empirical)"
  [macro-finance]="Macro-Finance"
)

declare -A SCOPE=(
  [eio]="Demand estimation, cost/production, competition and conduct, entry/exit, identification, and counterfactual analysis."
  [cf-theory]="Contracting, capital structure, governance, and core theory mechanisms."
  [cf-empirical]="Causal designs, measurement, and empirical firm behavior."
  [econometrics]="Identification, estimation, inference, and robustness."
  [micro]="Preferences, uncertainty, general equilibrium, and mechanisms."
  [macro]="Growth, business cycles, monetary frameworks."
  [math-foundations]="Linear algebra, probability, optimization, and analysis."
  [ap-theory]="SDF, no-arbitrage, equilibrium pricing."
  [ap-empirical]="Factors, predictability, anomalies, methods."
  [macro-finance]="Risk premia, term structure, policy transmission."
)

usage() {
  echo "Usage: $0 <section|all>"
  echo "Sections:"
  printf "  - %s\n" "${!DEST[@]}" | sort
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
for p in pdfs:
    lines.append(f"- **[{p.name}]({p.name})**\n")
(dst / "index.md").write_text("".join(lines), encoding="utf-8")
print("index.md updated:", dst / "index.md", "PDFs:", len(pdfs))
PY
}

sync_one() {
  local key="$1"
  local src="${SRC[$key]}"
  local dst="${DEST[$key]}"
  local title="${TITLE[$key]}"
  local scope="${SCOPE[$key]}"

  if [[ ! -d "$src" ]]; then
    echo "WARN: source not found, skip: $key -> $src"
    return 0
  fi

  mkdir -p "$dst"

  echo "==> Sync $key"
  rsync -av --delete \
    --include="*/" \
    --include="*.pdf" \
    --exclude="*" \
    "$src/" "$dst/"

  gen_index "$dst" "$title" "$scope"

  git add "$dst"
  if ! git diff --cached --quiet; then
    git commit -m "Update ${key} materials"
  else
    echo "    No changes to commit for $key"
  fi
}

main() {
  if [[ $# -ne 1 ]]; then usage; exit 1; fi
  local target="$1"

  if [[ "$target" == "all" ]]; then
    for key in $(printf "%s\n" "${!DEST[@]}" | sort); do
      sync_one "$key"
    done
  else
    if [[ -z "${DEST[$target]:-}" ]]; then usage; exit 1; fi
    sync_one "$target"
  fi

  git pull --rebase origin main || true
  git push origin main
  echo "✅ Done."
}

main "$@"

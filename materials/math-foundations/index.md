---
layout: sc
title: Math Foundations
hero_title: Math Foundations
hero_subtitle: File grid
hero_desc: linear algebra, probability, optimization, analysis
---

<div class="grid-note">
  <strong>Files in this folder</strong> — PDFs and subfolders are listed automatically.
</div>


<style>
.file-grid{
  display:grid;
  grid-template-columns: repeat(4, minmax(0, 1fr));  /* bigger tiles */
  gap: 16px;
  margin-top: 14px;
}
@media (max-width: 1100px){ .file-grid{ grid-template-columns: repeat(3, minmax(0, 1fr)); } }
@media (max-width: 900px){ .file-grid{ grid-template-columns: repeat(2, minmax(0, 1fr)); } }
@media (max-width: 640px){ .file-grid{ grid-template-columns: repeat(1, minmax(0, 1fr)); } }

.file-card{
  border:1px solid rgba(0,0,0,.10);
  border-radius:14px;
  background:#fff;
  padding: 16px 16px 14px 16px;   /* bigger padding */
  min-height: 150px;              /* bigger height */
  display:flex;
  flex-direction:column;
  justify-content:space-between;
}
.file-top{ display:flex; justify-content:space-between; gap:12px; align-items:flex-start; }
.file-name{
  font-weight:850;
  font-size:14px;
  line-height:1.25;
  word-break:break-word;
}
.file-intro{
  margin-top: 8px;
  opacity: .80;
  font-size: 12.5px;
  line-height: 1.35;
}
.badge{
  flex:0 0 auto;
  font-size:11px;
  letter-spacing:.08em;
  font-weight:900;
  padding:2px 8px;
  border-radius:999px;
  border:1px solid rgba(0,0,0,.12);
  opacity:.85;
}
.badge.pdf{ background: rgba(176,138,46,.10); }
.badge.folder{ background: rgba(15,61,46,.08); }
.badge.file{ background: rgba(29,78,216,.06); }

.file-meta{
  margin-top: 10px;
  opacity: .70;
  font-size: 12px;
}
.file-link{
  margin-top: 12px;
  font-weight: 700;
  font-size: 12.5px;
  opacity: .95;
}
.file-link a{ text-decoration:none; }
.file-link a:hover{ text-decoration:underline; }

.grid-note{
  margin: 16px 0 0 0;
  padding: 12px 14px;
  border: 1px solid rgba(0,0,0,.10);
  border-left: 4px solid #b08a2e;
  border-radius: 10px;
  background: #fff;
  opacity: .92;
}
</style>


<div id="fileGrid" class="file-grid"></div>


<script>
(async function(){
  const OWNER = "yaxinzn";
  const REPO  = "study-archive";
  const PATH  = "materials/math-foundations";
  const WEB_PREFIX = "{{ site.baseurl }}/" + PATH + "/";

  // One-sentence intros for tiles (edit freely)
  // Keys can be file names (e.g., "Econometric1.pdf") or folder names with trailing slash (e.g., "week1/")
  const INTROS = {
  "Econometric1.pdf": "Core lecture notes: identification, estimation, and inference with practical examples."
  "Micro1.pdf": "Consumer choice to KKT and geometry; foundations for later micro theory."
  "week1/": "Week 1 materials and notes."
  "week2/": "Week 2 materials and notes."
};

  const grid = document.getElementById("fileGrid");
  if (!grid) return;

  function humanSize(bytes){
    if (bytes === undefined || bytes === null) return "";
    const units = ["B","KB","MB","GB"];
    let i = 0, n = bytes;
    while (n >= 1024 && i < units.length-1){ n /= 1024; i++; }
    return `${n.toFixed(i===0?0:1)} ${units[i]}`;
  }

  function extBadge(name){
    const parts = (name || "").split(".");
    if (parts.length < 2) return "FILE";
    return parts[parts.length-1].toUpperCase();
  }

  const api = `https://api.github.com/repos/${OWNER}/${REPO}/contents/${PATH}`;
  const res = await fetch(api);
  if (!res.ok){
    grid.innerHTML = `<div class="file-meta">Could not load file list from GitHub.</div>`;
    return;
  }
  const items = await res.json();

  const isHidden = (n) => !n || n === "index.md" || n.startsWith(".") || n === ".DS_Store";

  const dirs = items
    .filter(x => x.type === "dir" && !isHidden(x.name))
    .sort((a,b) => (a.name||"").localeCompare(b.name||""));

  const files = items
    .filter(x => x.type === "file" && !isHidden(x.name))
    .sort((a,b) => (a.name||"").localeCompare(b.name||""));

  function introFor(key){
    return (INTROS && INTROS[key]) ? INTROS[key] : "";
  }

  // folders first
  for (const d of dirs){
    const key = d.name + "/";
    const url = WEB_PREFIX + encodeURIComponent(d.name) + "/";
    const intro = introFor(key);
    const card = document.createElement("div");
    card.className = "file-card";
    card.innerHTML = `
      <div>
        <div class="file-top">
          <div class="file-name">${d.name}/</div>
          <div class="badge folder">FOLDER</div>
        </div>
        ${intro ? `<div class="file-intro">${intro}</div>` : ``}
        <div class="file-meta">Subfolder</div>
      </div>
      <div class="file-link">
        <a href="${url}">Open</a>
      </div>`;
    grid.appendChild(card);
  }

  // files
  for (const f of files){
    const url = WEB_PREFIX + encodeURIComponent(f.name);
    const badge = extBadge(f.name);
    const badgeClass = (badge === "PDF") ? "pdf" : "file";
    const intro = introFor(f.name);
    const card = document.createElement("div");
    card.className = "file-card";
    card.innerHTML = `
      <div>
        <div class="file-top">
          <div class="file-name">${f.name}</div>
          <div class="badge ${badgeClass}">${badge}</div>
        </div>
        ${intro ? `<div class="file-intro">${intro}</div>` : ``}
        <div class="file-meta">${humanSize(f.size || 0)}</div>
      </div>
      <div class="file-link">
        <a href="${url}" target="_blank" rel="noopener">Open</a>
      </div>`;
    grid.appendChild(card);
  }

  if (dirs.length + files.length === 0){
    grid.innerHTML = `<div class="file-meta">No files yet.</div>`;
  }
})();
</script>


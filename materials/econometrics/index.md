---
layout: sc
title: Econometrics
hero_title: Econometrics
hero_subtitle: File grid (auto)
hero_desc: A 5-column file grid that auto-lists PDFs in this folder. Upload/remove files on GitHub and the grid updates automatically.
---

<style>
.grid-actions{
  margin: 16px 0 18px 0;
  display:flex;
  gap:12px;
  flex-wrap:wrap;
}
.grid-btn{
  display:inline-block;
  padding:10px 14px;
  border:1px solid rgba(0,0,0,.18);
  border-radius:10px;
  background:#fff;
  font-weight:650;
  text-decoration:none;
}
.grid-btn:hover{ text-decoration:none; transform: translateY(-1px); }

.grid-note{
  margin: 10px 0 18px 0;
  padding: 14px 16px;
  border: 1px solid rgba(0,0,0,.12);
  border-left: 4px solid #1d4ed8;
  border-radius: 10px;
  background: #fff;
  opacity: .92;
}

.file-grid{
  display:grid;
  grid-template-columns: repeat(5, minmax(0, 1fr));
  gap: 14px;
  margin-top: 10px;
}
@media (max-width: 1100px){ .file-grid{ grid-template-columns: repeat(4, minmax(0, 1fr)); } }
@media (max-width: 900px){ .file-grid{ grid-template-columns: repeat(3, minmax(0, 1fr)); } }
@media (max-width: 640px){ .file-grid{ grid-template-columns: repeat(2, minmax(0, 1fr)); } }

.file-card{
  border:1px solid rgba(0,0,0,.10);
  border-radius:12px;
  background:#fff;
  padding: 12px 12px 10px 12px;
  min-height: 110px;
  display:flex;
  flex-direction:column;
  justify-content:space-between;
}
.file-name{
  font-weight: 800;
  font-size: 13px;
  line-height: 1.25;
  word-break: break-word;
}
.file-meta{
  margin-top: 8px;
  opacity: .75;
  font-size: 12px;
}
.file-link{
  margin-top: 10px;
  font-weight: 650;
  font-size: 12px;
}
.file-link a{ text-decoration:none; }
.file-link a:hover{ text-decoration:underline; }

.file-card.upload{
  border:1px dashed rgba(0,0,0,.22);
  background: rgba(29,78,216,.03);
}
.badge{
  display:inline-block;
  font-size:11px;
  letter-spacing:.08em;
  font-weight:900;
  color:#1d4ed8;
  margin-top:6px;
}
</style>

<div class="grid-actions">
  <a class="grid-btn" href="https://github.com/yaxinzn/study-archive/upload/main/materials/econometrics" target="_blank" rel="noopener">
    Upload files (drag & drop on GitHub)
  </a>
  <a class="grid-btn" href="https://github.com/yaxinzn/study-archive/tree/main/materials/econometrics" target="_blank" rel="noopener">
    Manage folder on GitHub
  </a>
</div>

<div class="grid-note">
  <strong>How to add / delete tiles:</strong> each tile corresponds to a PDF in <code>materials/econometrics/</code>.
  To add, upload a PDF (drag & drop) on GitHub. To delete, remove the file on GitHub. This page auto-updates.
</div>

<div id="grid" class="file-grid"></div>

<script>
(async function(){
  const OWNER = "yaxinzn";
  const REPO  = "study-archive";
  const PATH  = "materials/econometrics";
  const WEB_PREFIX = "{{ site.baseurl }}/materials/econometrics/";

  const grid = document.getElementById("grid");

  function humanSize(bytes){
    if (!bytes && bytes !== 0) return "";
    const units = ["B","KB","MB","GB"];
    let i = 0, n = bytes;
    while (n >= 1024 && i < units.length-1){ n /= 1024; i++; }
    return `${n.toFixed(i===0?0:1)} ${units[i]}`;
  }

  // Upload tile first (so it’s always visible)
  const upload = document.createElement("div");
  upload.className = "file-card upload";
  upload.innerHTML = `
    <div>
      <div class="file-name">Add a new file</div>
      <div class="badge">DRAG & DROP</div>
      <div class="file-meta">Upload PDFs to GitHub, then this grid refreshes automatically.</div>
    </div>
    <div class="file-link">
      <a href="https://github.com/yaxinzn/study-archive/upload/main/materials/econometrics" target="_blank" rel="noopener">Open GitHub upload →</a>
    </div>`;
  grid.appendChild(upload);

  const api = `https://api.github.com/repos/${OWNER}/${REPO}/contents/${PATH}`;
  const res = await fetch(api);
  if (!res.ok){
    const err = document.createElement("div");
    err.className = "file-meta";
    err.textContent = "Could not load file list from GitHub API.";
    grid.appendChild(err);
    return;
  }
  const items = await res.json();

  // show only PDFs; ignore index.md and other files
  const pdfs = items
    .filter(x => x.type === "file" && (x.name || "").toLowerCase().endsWith(".pdf"))
    .sort((a,b) => (a.name || "").localeCompare(b.name || ""));

  for (const f of pdfs){
    const card = document.createElement("div");
    card.className = "file-card";
    const fileUrl = WEB_PREFIX + encodeURIComponent(f.name);
    const githubUrl = f.html_url || "";

    card.innerHTML = `
      <div>
        <div class="file-name">${f.name}</div>
        <div class="file-meta">${humanSize(f.size || 0)}</div>
      </div>
      <div class="file-link">
        <a href="${fileUrl}" target="_blank" rel="noopener">Open</a>
        ${githubUrl ? ` · <a href="${githubUrl}" target="_blank" rel="noopener">GitHub</a>` : ""}
      </div>
    `;
    grid.appendChild(card);
  }
})();
</script>

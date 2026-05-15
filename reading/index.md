---
layout: reading
title: Paper Reading
permalink: /reading/
hero_title: Paper Reading
hero_subtitle: Quick notes (high-signal)
hero_desc: Short, structured notes that prioritize identification logic, variable construction, and replication hooks.
---

<style>
.reading-callout{
  margin: 16px 0 18px 0;
  padding: 14px 16px;
  border: 1px solid rgba(0,0,0,.12);
  border-left: 4px solid #0f3d2e;
  border-radius: 10px;
  background: #fff;
}
.reading-callout-title{
  font-weight: 850;
  margin-bottom: 6px;
}
.reading-callout p{
  margin: 8px 0;
}
.reading-small{
  opacity: .88;
}

/* Search */
.reading-search{
  margin: 10px 0 18px 0;
  padding: 12px 14px;
  border: 1px solid rgba(0,0,0,.10);
  border-radius: 10px;
  background: #fff;
}
.reading-search-row{
  display:flex;
  gap:10px;
  flex-wrap:wrap;
  align-items:center;
}
#readingQuery{
  flex: 1 1 420px;
  padding: 10px 12px;
  border: 1px solid rgba(0,0,0,.18);
  border-radius: 10px;
  font-size: 15px;
}
#readingClear{
  padding: 10px 12px;
  border: 1px solid rgba(0,0,0,.18);
  border-radius: 10px;
  background:#fff;
  font-weight: 650;
  cursor:pointer;
}
#readingClear:hover{
  transform: translateY(-1px);
}
.reading-count{
  margin-top: 8px;
  opacity: .78;
  font-size: 13px;
}
.reading-empty{
  display:none;
  margin-top: 8px;
  padding: 10px 12px;
  border: 1px dashed rgba(0,0,0,.18);
  border-radius: 10px;
  background: rgba(0,0,0,.02);
  opacity: .85;
}

/* Random picker */
.reading-random{
  margin: 10px 0 18px 0;
  padding: 12px 14px;
  border: 1px solid rgba(0,0,0,.10);
  border-radius: 10px;
  background: #fff;
}
.reading-random-row{
  display:flex;
  gap:10px;
  flex-wrap:wrap;
  align-items:center;
}
.reading-random-row button{
  padding: 10px 12px;
  border: 1px solid rgba(0,0,0,.18);
  border-radius: 10px;
  background:#fff;
  font-weight: 650;
  cursor:pointer;
}
.reading-random-row button:hover{
  transform: translateY(-1px);
}
.reading-random-row button:disabled{
  opacity: .45;
  cursor: not-allowed;
  transform: none;
}
.reading-random-note{
  margin-top: 8px;
  opacity: .78;
  font-size: 13px;
}
.reading-random-status{
  margin-top: 8px;
  font-size: 13px;
  opacity: .82;
}
#readingRandomList{
  margin: 10px 0 0 20px;
}
#readingRandomList li{
  margin: 5px 0;
}

/* Cards */
.reading-entry{
  margin: 16px 0;
  padding: 14px 16px;
  border: 1px solid rgba(0,0,0,.10);
  border-left: 4px solid #0f3d2e;
  border-radius: 10px;
  background: #fff;
}
.reading-title{
  font-weight: 800;
}
.reading-file{
  margin-top: 10px;
}
.reading-desc{
  margin-top: 8px;
  opacity: .90;
}
</style>

<div class="reading-callout">
  <div class="reading-callout-title">Paper Reading &amp; Quick Notes</div>
  <p>
    A curated reading notebook: concise notes that prioritize <strong>identification</strong>, <strong>variable construction</strong>,
    and <strong>replication hooks</strong>.
  </p>
  <p class="reading-small">
    If anything is unclear or incorrect, please tell me—I will revise and improve it.
  </p>
</div>

<div class="reading-search">
  <div class="reading-search-row">
    <input id="readingQuery" type="search" placeholder="Search by author / title / keywords…" autocomplete="off">
    <button id="readingClear" type="button">Clear</button>
  </div>
  <div class="reading-count" id="readingCount"></div>
  <div class="reading-empty" id="readingEmpty">No matching papers. Try a different keyword, such as an author surname.</div>
</div>

<div class="reading-random">
  <div class="reading-random-row">
    <button id="readingRandomBtn" type="button">Pick 10 Random PDFs</button>
    <button id="readingCopyBtn" type="button" disabled>Copy Selected Names</button>
    <button id="readingDownloadNamesBtn" type="button" disabled>Download Selected Names</button>
    <button id="readingCopyDownloadBtn" type="button" disabled>Copy + Download Names</button>
  </div>

  <div class="reading-random-note">
    Reading check: randomly select 10 PDF files from the library. After selection, you can copy the selected PDF names, download them as a text file, or do both with one click.
  </div>

  <div class="reading-random-status" id="readingRandomStatus" aria-live="polite"></div>

  <ol id="readingRandomList"></ol>
</div>

## Library

{% assign items = site.data.reading %}
{% if items and items.size > 0 %}
  {% for p in items %}
  <div class="reading-entry" data-search="{{ p.title | escape }} {{ p.file | escape }} {{ p.desc | escape }}">
    <div class="reading-title">{{ p.title }}</div>

    <p class="reading-file">
      <strong>File:</strong>
      <a href="{{ site.baseurl }}/reading/library/{{ p.file | uri_escape }}">{{ p.file }}</a>
    </p>

    <p class="reading-desc">{{ p.desc }}</p>
  </div>
  {% endfor %}
{% else %}
  <div class="reading-entry">
    <div class="reading-title">No papers yet.</div>
    <p class="reading-desc">Add entries to <code>_data/reading.yml</code> and upload PDFs to <code>reading/library/</code>.</p>
  </div>
{% endif %}

<script>
(function(){
  const input = document.getElementById('readingQuery');
  const clearBtn = document.getElementById('readingClear');
  const entries = Array.from(document.querySelectorAll('.reading-entry'));
  const count = document.getElementById('readingCount');
  const empty = document.getElementById('readingEmpty');

  const randomBtn = document.getElementById('readingRandomBtn');
  const copyBtn = document.getElementById('readingCopyBtn');
  const downloadNamesBtn = document.getElementById('readingDownloadNamesBtn');
  const copyDownloadBtn = document.getElementById('readingCopyDownloadBtn');
  const randomList = document.getElementById('readingRandomList');
  const randomStatus = document.getElementById('readingRandomStatus');

  let selectedPDFs = [];
  let selectedDate = '';

  if (!input) return;

  function norm(x){
    return (x || '').toLowerCase().replace(/\s+/g, ' ').trim();
  }

  function update(){
    const q = norm(input.value);
    let shown = 0;

    for (const el of entries) {
      const hay = norm(el.getAttribute('data-search')) || norm(el.textContent);
      const ok = !q || hay.includes(q);
      el.style.display = ok ? '' : 'none';
      if (ok) shown += 1;
    }

    if (count) {
      count.textContent = `${shown} / ${entries.length} papers`;
    }

    if (empty) {
      empty.style.display = shown === 0 ? 'block' : 'none';
    }
  }

  function getLocalDateStamp(){
    const now = new Date();
    const year = now.getFullYear();
    const month = String(now.getMonth() + 1).padStart(2, '0');
    const day = String(now.getDate()).padStart(2, '0');

    return `${year}-${month}-${day}`;
  }

  function getPDFs(){
    return Array.from(document.querySelectorAll('.reading-file a'))
      .map(a => ({
        name: a.textContent.trim(),
        href: a.getAttribute('href')
      }))
      .filter(pdf => pdf.name && pdf.href);
  }

  function shuffle(items){
    return items
      .map(item => ({ item, randomValue: Math.random() }))
      .sort((a, b) => a.randomValue - b.randomValue)
      .map(obj => obj.item);
  }

  function setActionButtonsEnabled(enabled){
    if (copyBtn) {
      copyBtn.disabled = !enabled;
    }

    if (downloadNamesBtn) {
      downloadNamesBtn.disabled = !enabled;
    }

    if (copyDownloadBtn) {
      copyDownloadBtn.disabled = !enabled;
    }
  }

  function formatSelectedNames(){
    return selectedPDFs
      .map((pdf, index) => `${index + 1}. ${pdf.name}`)
      .join('\n');
  }

  function formatSelectedNamesFile(){
    return [
      `Random PDF Selection Date: ${selectedDate}`,
      '',
      formatSelectedNames()
    ].join('\n');
  }

  function renderRandomList(){
    if (!randomList) return;

    randomList.innerHTML = '';

    if (selectedPDFs.length === 0) {
      randomList.innerHTML = '<li>No PDFs found.</li>';
      return;
    }

    for (const pdf of selectedPDFs) {
      const li = document.createElement('li');
      const a = document.createElement('a');

      a.textContent = pdf.name;
      a.href = pdf.href;
      a.target = '_blank';
      a.rel = 'noopener';

      li.appendChild(a);
      randomList.appendChild(li);
    }
  }

  function pickRandomPDFs(){
    const pdfs = getPDFs();

    selectedPDFs = shuffle(pdfs).slice(0, 10);
    selectedDate = getLocalDateStamp();

    renderRandomList();

    const hasSelection = selectedPDFs.length > 0;
    setActionButtonsEnabled(hasSelection);

    if (randomStatus) {
      if (hasSelection) {
        randomStatus.textContent = `Selected ${selectedPDFs.length} PDF names on ${selectedDate}.`;
      } else {
        randomStatus.textContent = 'No PDFs were found in the library.';
      }
    }
  }

  async function copySelectedNames(showStatus = true){
    if (!selectedPDFs.length) return false;

    const text = formatSelectedNames();

    try {
      if (navigator.clipboard && window.isSecureContext) {
        await navigator.clipboard.writeText(text);
      } else {
        throw new Error('Clipboard API is unavailable.');
      }
    } catch (err) {
      const temp = document.createElement('textarea');

      temp.value = text;
      temp.setAttribute('readonly', '');
      temp.style.position = 'absolute';
      temp.style.left = '-9999px';

      document.body.appendChild(temp);
      temp.select();
      document.execCommand('copy');
      document.body.removeChild(temp);
    }

    if (showStatus && randomStatus) {
      randomStatus.textContent = `Copied ${selectedPDFs.length} PDF names to clipboard. Selection date: ${selectedDate}.`;
    }

    return true;
  }

  function downloadSelectedNames(showStatus = true){
    if (!selectedPDFs.length) return false;

    const fileContent = formatSelectedNamesFile();
    const blob = new Blob([fileContent], { type: 'text/plain;charset=utf-8' });
    const url = URL.createObjectURL(blob);

    const a = document.createElement('a');
    a.href = url;
    a.download = `${selectedDate}.txt`;

    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);

    URL.revokeObjectURL(url);

    if (showStatus && randomStatus) {
      randomStatus.textContent = `Downloaded selected PDF names as ${selectedDate}.txt.`;
    }

    return true;
  }

  async function copyAndDownloadSelectedNames(){
    if (!selectedPDFs.length) return;

    await copySelectedNames(false);
    downloadSelectedNames(false);

    if (randomStatus) {
      randomStatus.textContent = `Copied and downloaded ${selectedPDFs.length} PDF names as ${selectedDate}.txt.`;
    }
  }

  input.addEventListener('input', update);

  clearBtn && clearBtn.addEventListener('click', () => {
    input.value = '';
    update();
    input.focus();
  });

  input.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
      input.value = '';
      update();
    }
  });

  randomBtn && randomBtn.addEventListener('click', pickRandomPDFs);
  copyBtn && copyBtn.addEventListener('click', () => copySelectedNames(true));
  downloadNamesBtn && downloadNamesBtn.addEventListener('click', () => downloadSelectedNames(true));
  copyDownloadBtn && copyDownloadBtn.addEventListener('click', copyAndDownloadSelectedNames);

  setActionButtonsEnabled(false);
  update();
})();
</script>

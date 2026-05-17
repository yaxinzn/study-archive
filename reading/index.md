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

/* Two-column layout */
.reading-layout{
  display: grid;
  grid-template-columns: minmax(0, 1fr) 300px;
  gap: 20px;
  align-items: start;
}
.reading-main{
  min-width: 0;
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

/* Author initial guide */
.reading-guide{
  position: sticky;
  top: 18px;
  max-height: calc(100vh - 36px);
  overflow: auto;
  margin: 10px 0 18px 0;
  padding: 14px;
  border: 1px solid rgba(0,0,0,.10);
  border-radius: 10px;
  background: #fff;
}
.reading-guide-title{
  font-weight: 850;
  margin-bottom: 6px;
}
.reading-guide-desc{
  margin: 0 0 12px 0;
  font-size: 13px;
  line-height: 1.45;
  opacity: .78;
}
.reading-initial-row{
  display: flex;
  gap: 8px;
  margin-bottom: 10px;
}
#readingInitialInput{
  width: 100%;
  min-width: 0;
  padding: 10px 12px;
  border: 1px solid rgba(0,0,0,.18);
  border-radius: 10px;
  font-size: 15px;
  text-transform: uppercase;
}
#readingInitialClear{
  flex: 0 0 auto;
  padding: 10px 12px;
  border: 1px solid rgba(0,0,0,.18);
  border-radius: 10px;
  background:#fff;
  font-weight: 650;
  cursor:pointer;
}
#readingInitialClear:hover{
  transform: translateY(-1px);
}
.reading-letter-grid{
  display: grid;
  grid-template-columns: repeat(6, 1fr);
  gap: 6px;
  margin: 8px 0 12px 0;
}
.reading-letter-btn{
  padding: 7px 0;
  border: 1px solid rgba(0,0,0,.16);
  border-radius: 8px;
  background: #fff;
  font-size: 12px;
  font-weight: 750;
  cursor: pointer;
}
.reading-letter-btn:hover:not(:disabled){
  transform: translateY(-1px);
}
.reading-letter-btn.is-active{
  background: #0f3d2e;
  border-color: #0f3d2e;
  color: #fff;
}
.reading-letter-btn:disabled{
  opacity: .32;
  cursor: not-allowed;
}
.reading-guide-count{
  margin-top: 8px;
  padding-top: 10px;
  border-top: 1px solid rgba(0,0,0,.08);
  font-size: 13px;
  font-weight: 750;
}
.reading-guide-list{
  list-style: none;
  margin: 10px 0 0 0;
  padding: 0;
}
.reading-guide-list li{
  margin: 0;
  padding: 9px 0;
  border-bottom: 1px solid rgba(0,0,0,.07);
}
.reading-guide-list li:last-child{
  border-bottom: 0;
}
.reading-guide-list a{
  display: block;
  font-weight: 750;
  line-height: 1.35;
  overflow-wrap: anywhere;
}
.reading-guide-meta{
  display: block;
  margin-top: 4px;
  font-size: 12px;
  line-height: 1.35;
  opacity: .75;
  overflow-wrap: anywhere;
}
.reading-guide-empty{
  margin-top: 10px;
  padding: 10px 12px;
  border: 1px dashed rgba(0,0,0,.18);
  border-radius: 10px;
  background: rgba(0,0,0,.02);
  font-size: 13px;
  line-height: 1.4;
  opacity: .82;
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
.reading-author,
.reading-file{
  margin-top: 10px;
}
.reading-desc{
  margin-top: 8px;
  opacity: .90;
}

@media (max-width: 980px){
  .reading-layout{
    grid-template-columns: 1fr;
  }
  .reading-guide{
    position: static;
    max-height: none;
  }
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

{% assign items = site.data.reading %}

<div class="reading-layout">
  <main class="reading-main">
    <div class="reading-search">
      <div class="reading-search-row">
        <input id="readingQuery" type="search" placeholder="Search by author / title / keywords…" autocomplete="off">
        <button id="readingClear" type="button">Clear</button>
      </div>
      <div class="reading-count" id="readingCount"></div>
      <div class="reading-empty" id="readingEmpty">No matching papers. Try a different keyword or clear the author initial filter.</div>
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

    <h2 id="library">Library</h2>

    {% if items and items.size > 0 %}
      {% for p in items %}
        {% assign paper_authors = "" %}
        {% if p.author %}
          {% assign paper_authors = p.author %}
        {% elsif p.authors %}
          {% assign paper_authors = p.authors | join: ", " %}
        {% endif %}

        <div class="reading-entry"
             data-search="{{ paper_authors | escape }} {{ p.title | escape }} {{ p.file | escape }} {{ p.desc | escape }}"
             data-author="{{ paper_authors | escape }}"
             data-title="{{ p.title | escape }}"
             data-file="{{ p.file | escape }}">
          <div class="reading-title">{{ p.title }}</div>

          {% if paper_authors and paper_authors != "" %}
            <p class="reading-author">
              <strong>Author:</strong>
              {{ paper_authors }}
            </p>
          {% endif %}

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
  </main>

  <aside class="reading-guide" aria-labelledby="readingGuideTitle">
    <div class="reading-guide-title" id="readingGuideTitle">Author Initial Guide</div>
    <p class="reading-guide-desc">
      Type an author initial or click a letter to filter the library and show matching PDF files.
    </p>

    <div class="reading-initial-row">
      <input id="readingInitialInput" type="text" maxlength="1" inputmode="latin" placeholder="A" aria-label="Author initial">
      <button id="readingInitialClear" type="button">Clear</button>
    </div>

    <div class="reading-letter-grid" id="readingLetterButtons" aria-label="Author initials A to Z"></div>

    <div class="reading-guide-count" id="readingGuideCount"></div>
    <ul class="reading-guide-list" id="readingGuideList"></ul>
  </aside>
</div>

<script>
(function(){
  const input = document.getElementById('readingQuery');
  const clearBtn = document.getElementById('readingClear');
  const entries = Array.from(document.querySelectorAll('.reading-entry'));
  const count = document.getElementById('readingCount');
  const empty = document.getElementById('readingEmpty');

  const initialInput = document.getElementById('readingInitialInput');
  const initialClearBtn = document.getElementById('readingInitialClear');
  const letterButtonsWrap = document.getElementById('readingLetterButtons');
  const guideCount = document.getElementById('readingGuideCount');
  const guideList = document.getElementById('readingGuideList');

  const randomBtn = document.getElementById('readingRandomBtn');
  const copyBtn = document.getElementById('readingCopyBtn');
  const downloadNamesBtn = document.getElementById('readingDownloadNamesBtn');
  const copyDownloadBtn = document.getElementById('readingCopyDownloadBtn');
  const randomList = document.getElementById('readingRandomList');
  const randomStatus = document.getElementById('readingRandomStatus');

  let selectedPDFs = [];
  let selectedDate = '';
  let selectedInitial = '';
  let letterButtons = [];

  if (!input) return;

  function norm(x){
    return (x || '')
      .toString()
      .normalize('NFD')
      .replace(/[\u0300-\u036f]/g, '')
      .toLowerCase()
      .replace(/\s+/g, ' ')
      .trim();
  }

  function cleanSeed(x){
    return (x || '')
      .toString()
      .replace(/\.pdf$/i, '')
      .replace(/[_–—-]+/g, ' ')
      .replace(/\b(et al|and|with|by)\b/ig, ' ')
      .replace(/\s+/g, ' ')
      .trim();
  }

  function normalizeInitial(x){
    const match = (x || '')
      .toString()
      .normalize('NFD')
      .replace(/[\u0300-\u036f]/g, '')
      .toUpperCase()
      .match(/[A-Z]/);

    return match ? match[0] : '';
  }

  function initialsFromAuthor(author){
    const words = cleanSeed(author)
      .normalize('NFD')
      .replace(/[\u0300-\u036f]/g, '')
      .match(/[A-Za-z]+/g) || [];

    return Array.from(new Set(words.map(word => word.charAt(0).toUpperCase())));
  }

  function firstInitialFromText(text){
    const match = cleanSeed(text)
      .normalize('NFD')
      .replace(/[\u0300-\u036f]/g, '')
      .match(/[A-Za-z]/);

    return match ? match[0].toUpperCase() : '';
  }

  function getEntryData(el){
    const link = el.querySelector('.reading-file a');
    const titleNode = el.querySelector('.reading-title');

    const author = (el.getAttribute('data-author') || '').trim();
    const title = (el.getAttribute('data-title') || (titleNode ? titleNode.textContent : '') || '').trim();
    const file = (el.getAttribute('data-file') || (link ? link.textContent : '') || '').trim();
    const href = link ? link.getAttribute('href') : '';

    let initials = [];

    if (author) {
      initials = initialsFromAuthor(author);
    } else {
      const fallbackInitial = firstInitialFromText(title || file);
      initials = fallbackInitial ? [fallbackInitial] : [];
    }

    return {
      el,
      author,
      title,
      file,
      href,
      initials,
      search: norm(`${author} ${title} ${file} ${el.textContent}`),
      sortKey: norm(`${author || title || file} ${file}`)
    };
  }

  const paperData = entries
    .map(getEntryData)
    .filter(item => item.href && item.file);

  const dataByElement = new Map(paperData.map(item => [item.el, item]));
  const alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.split('');

  function getAvailableInitials(){
    const available = new Set();

    for (const item of paperData) {
      for (const letter of item.initials) {
        available.add(letter);
      }
    }

    return available;
  }

  function buildLetterButtons(){
    if (!letterButtonsWrap) return;

    letterButtonsWrap.innerHTML = '';
    letterButtons = [];

    for (const letter of alphabet) {
      const btn = document.createElement('button');

      btn.type = 'button';
      btn.className = 'reading-letter-btn';
      btn.dataset.letter = letter;
      btn.textContent = letter;
      btn.setAttribute('aria-pressed', 'false');
      btn.addEventListener('click', () => setInitial(letter));

      letterButtonsWrap.appendChild(btn);
      letterButtons.push(btn);
    }
  }

  function updateLetterButtons(activeLetter){
    const available = getAvailableInitials();

    for (const btn of letterButtons) {
      const letter = btn.dataset.letter;
      const hasMatches = available.has(letter);
      const isActive = activeLetter === letter;

      btn.disabled = !hasMatches;
      btn.classList.toggle('is-active', isActive);
      btn.setAttribute('aria-pressed', isActive ? 'true' : 'false');
      btn.title = hasMatches
        ? `Show PDFs with author initial ${letter}`
        : `No PDFs found for author initial ${letter}`;
    }
  }

  function getGuideMatches(letter){
    if (!letter) return [];

    return paperData
      .filter(item => item.initials.includes(letter))
      .sort((a, b) => a.sortKey.localeCompare(b.sortKey));
  }

  function renderGuide(letter){
    if (!guideList || !guideCount) return;

    guideList.innerHTML = '';

    if (!letter) {
      guideCount.textContent = 'No author initial selected';
      const li = document.createElement('li');
      li.className = 'reading-guide-empty';
      li.textContent = 'Type an author initial or click an A–Z button to see matching PDF files.';
      guideList.appendChild(li);
      return;
    }

    const matches = getGuideMatches(letter);
    guideCount.textContent = `${matches.length} PDF${matches.length === 1 ? '' : 's'} for author initial ${letter}`;

    if (matches.length === 0) {
      const li = document.createElement('li');
      li.className = 'reading-guide-empty';
      li.textContent = `No PDFs found for author initial ${letter}.`;
      guideList.appendChild(li);
      return;
    }

    for (const item of matches) {
      const li = document.createElement('li');
      const a = document.createElement('a');
      const meta = document.createElement('span');

      a.textContent = item.file;
      a.href = item.href;
      a.target = '_blank';
      a.rel = 'noopener';

      meta.className = 'reading-guide-meta';
      meta.textContent = item.author ? `${item.author} — ${item.title}` : item.title;

      li.appendChild(a);
      li.appendChild(meta);
      guideList.appendChild(li);
    }
  }

  function update(){
    const q = norm(input.value);
    const activeLetter = normalizeInitial(selectedInitial || (initialInput ? initialInput.value : ''));
    let shown = 0;

    for (const el of entries) {
      const item = dataByElement.get(el);
      const hay = item ? item.search : norm(el.getAttribute('data-search') || el.textContent);
      const searchOk = !q || hay.includes(q);
      const initialOk = !activeLetter || (item && item.initials.includes(activeLetter));
      const ok = searchOk && initialOk;

      el.style.display = ok ? '' : 'none';

      if (item && ok) {
        shown += 1;
      }
    }

    if (count) {
      count.textContent = `${shown} / ${paperData.length} papers`;
    }

    if (empty) {
      empty.style.display = shown === 0 ? 'block' : 'none';
    }

    renderGuide(activeLetter);
    updateLetterButtons(activeLetter);
  }

  function setInitial(value){
    selectedInitial = normalizeInitial(value);

    if (initialInput) {
      initialInput.value = selectedInitial;
    }

    update();
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

  initialInput && initialInput.addEventListener('input', () => {
    setInitial(initialInput.value);
  });

  initialInput && initialInput.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
      setInitial('');
    }
  });

  initialClearBtn && initialClearBtn.addEventListener('click', () => {
    setInitial('');
    initialInput && initialInput.focus();
  });

  randomBtn && randomBtn.addEventListener('click', pickRandomPDFs);
  copyBtn && copyBtn.addEventListener('click', () => copySelectedNames(true));
  downloadNamesBtn && downloadNamesBtn.addEventListener('click', () => downloadSelectedNames(true));
  copyDownloadBtn && copyDownloadBtn.addEventListener('click', copyAndDownloadSelectedNames);

  buildLetterButtons();
  setActionButtonsEnabled(false);
  update();
})();
</script>

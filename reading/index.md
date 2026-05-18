---
layout: reading
title: Paper Reading
permalink: /reading/
hero_title: Paper Reading
hero_subtitle: Quick notes (high-signal)
hero_desc: Short, structured notes that prioritize identification logic, variable construction, and replication hooks.
---

<style>
:root{
  --reading-green:#0f3d2e;
  --reading-green-soft:rgba(15,61,46,.06);
  --reading-border:rgba(0,0,0,.10);
  --reading-border-strong:rgba(0,0,0,.16);
  --reading-text:#111827;
  --reading-muted:rgba(17,24,39,.64);
  --reading-bg:#fff;
  --reading-shadow:0 14px 34px rgba(0,0,0,.08);
}

.reading-page{
  max-width:1080px;
  margin:0 auto;
}

.reading-callout,
.reading-panel,
.reading-picker,
.reading-side,
.reading-entry{
  border:1px solid var(--reading-border);
  border-radius:14px;
  background:var(--reading-bg);
}

.reading-callout{
  margin:16px 0 20px 0;
  padding:15px 18px;
  border-left:4px solid var(--reading-green);
}
.reading-callout-title{
  margin:0 0 5px 0;
  color:var(--reading-text);
  font-size:18px;
  font-weight:850;
  line-height:1.25;
}
.reading-callout p{
  margin:6px 0;
  color:var(--reading-muted);
  line-height:1.55;
}

/* Full-width filter panel */
.reading-panel{
  margin:0 0 20px 0;
  padding:16px;
}
.reading-panel-head{
  display:flex;
  gap:14px;
  justify-content:space-between;
  align-items:flex-start;
  margin-bottom:14px;
}
.reading-panel-title{
  margin:0;
  color:var(--reading-green);
  font-size:18px;
  font-weight:900;
  line-height:1.25;
}
.reading-panel-note{
  margin:4px 0 0 0;
  max-width:760px;
  color:var(--reading-muted);
  font-size:13px;
  line-height:1.45;
}
.reading-filter-stack{
  display:grid;
  gap:10px;
}
.reading-search-line{
  display:grid;
  grid-template-columns:minmax(0,1fr) auto;
  gap:10px;
  align-items:end;
}
.reading-filter-row{
  display:grid;
  grid-template-columns:minmax(150px,.9fr) minmax(170px,1fr) minmax(130px,.75fr);
  gap:10px;
  max-width:650px;
  align-items:end;
}
.reading-field{
  display:block;
  min-width:0;
}
.reading-field span,
.reading-field-label{
  display:block;
  margin:0 0 5px 0;
  color:rgba(17,24,39,.78);
  font-size:12px;
  font-weight:850;
  letter-spacing:.01em;
}
.reading-field input,
.reading-journal-summary{
  width:100%;
  min-height:40px;
  box-sizing:border-box;
  padding:9px 11px;
  border:1px solid rgba(0,0,0,.18);
  border-radius:10px;
  background:#fff;
  color:var(--reading-text);
  font-size:14px;
}
.reading-field input::placeholder{
  color:rgba(17,24,39,.46);
}
#readingInitialInput{
  text-transform:uppercase;
}
.reading-field input:focus,
.reading-journal-select:focus-within .reading-journal-summary{
  outline:2px solid rgba(15,61,46,.15);
  border-color:rgba(15,61,46,.48);
}
.reading-secondary-btn,
.reading-random-row button,
.reading-filter-chip,
.reading-letter-btn{
  border:1px solid var(--reading-border-strong);
  border-radius:10px;
  background:#fff;
  color:var(--reading-text);
  cursor:pointer;
  font-weight:760;
}
.reading-secondary-btn{
  flex:0 0 auto;
  min-height:40px;
  padding:9px 12px;
  white-space:nowrap;
}
.reading-secondary-btn:hover,
.reading-random-row button:hover:not(:disabled),
.reading-filter-chip:hover,
.reading-letter-btn:hover:not(:disabled){
  transform:translateY(-1px);
}

/* Compact journal dropdown */
.reading-journal-select{
  position:relative;
  max-width:100%;
}
.reading-journal-summary{
  list-style:none;
  cursor:pointer;
  display:grid;
  grid-template-columns:minmax(0,1fr) auto;
  align-items:center;
  gap:8px;
  white-space:nowrap;
}
.reading-journal-summary::-webkit-details-marker{
  display:none;
}
.reading-journal-summary::after{
  content:'▾';
  color:var(--reading-muted);
  font-size:11px;
}
.reading-journal-select[open] .reading-journal-summary::after{
  content:'▴';
}
#readingJournalSummaryText{
  overflow:hidden;
  text-overflow:ellipsis;
}
.reading-journal-menu{
  position:absolute;
  z-index:30;
  right:0;
  margin-top:7px;
  width:max-content;
  min-width:220px;
  max-width:min(320px, calc(100vw - 40px));
  max-height:280px;
  overflow:auto;
  padding:8px;
  border:1px solid var(--reading-border);
  border-radius:12px;
  background:#fff;
  box-shadow:var(--reading-shadow);
}
.reading-journal-option{
  display:flex;
  align-items:center;
  gap:8px;
  min-width:0;
  padding:7px 8px;
  border-radius:8px;
  color:var(--reading-text);
  font-size:13px;
  line-height:1.25;
  white-space:nowrap;
}
.reading-journal-option:hover{
  background:var(--reading-green-soft);
}
.reading-journal-option input{
  width:auto;
  min-height:0;
  margin:0;
}
.reading-journal-option span{
  overflow:hidden;
  text-overflow:ellipsis;
}
.reading-journal-option.is-muted{
  opacity:.42;
}

/* Optional initial picker */
.reading-advanced{
  margin-top:10px;
}
.reading-advanced summary{
  width:max-content;
  cursor:pointer;
  color:var(--reading-green);
  font-size:13px;
  font-weight:820;
}
.reading-letter-grid{
  display:grid;
  grid-template-columns:repeat(13, minmax(0,1fr));
  gap:5px;
  max-width:620px;
  margin-top:8px;
}
.reading-letter-btn{
  min-height:30px;
  padding:4px 0;
  font-size:12px;
}
.reading-letter-btn.is-active{
  border-color:var(--reading-green);
  background:var(--reading-green);
  color:#fff;
}
.reading-letter-btn:disabled{
  cursor:not-allowed;
  opacity:.28;
}

.reading-active-filters{
  display:flex;
  flex-wrap:wrap;
  gap:6px;
  margin-top:10px;
}
.reading-active-filters[hidden]{
  display:none;
}
.reading-filter-chip{
  display:inline-flex;
  align-items:center;
  gap:6px;
  max-width:100%;
  padding:6px 9px;
  background:var(--reading-green-soft);
  color:var(--reading-green);
  font-size:12px;
  line-height:1.2;
}
.reading-filter-chip strong{
  color:var(--reading-green);
  font-size:13px;
}
.reading-count{
  margin-top:9px;
  color:var(--reading-muted);
  font-size:13px;
}
.reading-empty{
  display:none;
  margin-top:10px;
  padding:10px 12px;
  border:1px dashed rgba(0,0,0,.18);
  border-radius:10px;
  background:rgba(0,0,0,.025);
  color:var(--reading-muted);
}

/* Main content + side directory */
.reading-content-grid{
  display:grid;
  grid-template-columns:minmax(0,1fr) 292px;
  gap:22px;
  align-items:start;
}
.reading-main{
  min-width:0;
}

/* Review picker */
.reading-picker{
  margin:0 0 18px 0;
  padding:0;
}
.reading-picker summary{
  cursor:pointer;
  display:flex;
  gap:10px;
  justify-content:space-between;
  align-items:center;
  padding:13px 15px;
  color:var(--reading-text);
  font-weight:850;
}
.reading-picker-subtitle{
  color:var(--reading-muted);
  font-size:12px;
  font-weight:500;
}
.reading-picker-body{
  padding:0 15px 14px 15px;
  border-top:1px solid rgba(0,0,0,.08);
}
.reading-random-row{
  display:flex;
  flex-wrap:wrap;
  gap:8px;
  margin-top:12px;
}
.reading-random-row button{
  min-height:36px;
  padding:8px 10px;
  font-size:13px;
}
.reading-random-row button:disabled{
  cursor:not-allowed;
  opacity:.42;
  transform:none;
}
.reading-random-status{
  margin-top:9px;
  color:var(--reading-muted);
  font-size:13px;
}
#readingRandomList{
  margin:10px 0 0 20px;
}
#readingRandomList li{
  margin:5px 0;
}

/* Library cards */
.reading-section-title{
  margin:20px 0 10px 0;
  color:var(--reading-green);
  font-size:26px;
  line-height:1.2;
}
.reading-entry{
  margin:12px 0;
  padding:14px 16px;
  border-left:4px solid var(--reading-green);
}
.reading-entry[hidden]{
  display:none !important;
}
.reading-entry-top{
  display:flex;
  gap:12px;
  align-items:flex-start;
  justify-content:space-between;
}
.reading-title{
  color:var(--reading-text);
  font-weight:850;
  line-height:1.35;
}
.reading-card-meta{
  display:flex;
  flex:0 0 auto;
  flex-wrap:wrap;
  justify-content:flex-end;
  gap:5px;
}
.reading-pill{
  display:inline-flex;
  align-items:center;
  padding:3px 7px;
  border:1px solid rgba(0,0,0,.12);
  border-radius:999px;
  background:rgba(0,0,0,.02);
  color:rgba(17,24,39,.70);
  font-size:11px;
  line-height:1.25;
}
.reading-author,
.reading-file{
  margin:8px 0 0 0;
  font-size:14px;
  line-height:1.45;
}
.reading-file a{
  overflow-wrap:anywhere;
}
.reading-note{
  margin-top:9px;
}
.reading-note summary{
  width:max-content;
  cursor:pointer;
  color:var(--reading-green);
  font-size:13px;
  font-weight:820;
}
.reading-desc{
  margin:8px 0 0 0;
  color:rgba(17,24,39,.82);
  line-height:1.64;
}

/* Right-side focused PDF directory */
.reading-side{
  position:sticky;
  top:18px;
  max-height:calc(100vh - 36px);
  overflow:auto;
  padding:15px;
}
.reading-side-title{
  margin-bottom:5px;
  color:var(--reading-text);
  font-weight:850;
}
.reading-side-hint{
  margin:0 0 12px 0;
  color:var(--reading-muted);
  font-size:13px;
  line-height:1.45;
}
.reading-guide-count{
  padding:10px 0;
  border-top:1px solid rgba(0,0,0,.08);
  border-bottom:1px solid rgba(0,0,0,.08);
  color:var(--reading-text);
  font-size:13px;
  font-weight:850;
}
.reading-guide-list{
  margin:10px 0 0 0;
  padding:0;
  list-style:none;
}
.reading-guide-list li{
  padding:9px 0;
  border-bottom:1px solid rgba(0,0,0,.07);
}
.reading-guide-list li:last-child{
  border-bottom:0;
}
.reading-guide-list a{
  display:block;
  font-weight:760;
  line-height:1.35;
  overflow-wrap:anywhere;
}
.reading-guide-meta{
  display:block;
  margin-top:4px;
  color:var(--reading-muted);
  font-size:12px;
  line-height:1.35;
  overflow-wrap:anywhere;
}
.reading-guide-empty{
  padding:10px 12px !important;
  border:1px dashed rgba(0,0,0,.18) !important;
  border-radius:10px;
  background:rgba(0,0,0,.025);
  color:var(--reading-muted);
  font-size:13px;
  line-height:1.4;
}

@media (max-width:980px){
  .reading-content-grid{
    grid-template-columns:1fr;
  }
  .reading-side{
    position:static;
    max-height:none;
  }
}
@media (max-width:720px){
  .reading-panel-head,
  .reading-search-line,
  .reading-entry-top,
  .reading-picker summary{
    display:block;
  }
  .reading-secondary-btn{
    margin-top:10px;
  }
  .reading-filter-row{
    grid-template-columns:1fr;
    max-width:none;
  }
  .reading-card-meta{
    justify-content:flex-start;
    margin-top:8px;
  }
  .reading-letter-grid{
    grid-template-columns:repeat(7, minmax(0,1fr));
  }
  .reading-journal-menu{
    position:static;
    width:100%;
    min-width:0;
    max-width:none;
    box-shadow:none;
  }
}
</style>

<div class="reading-page">
  <div class="reading-callout">
    <div class="reading-callout-title">Paper Reading &amp; Quick Notes</div>
    <p>A curated reading notebook for fast review. Search by author, title, PDF name, keyword, author initials, year, or journal.</p>
  </div>

  {% assign items = site.data.reading %}

  <section class="reading-panel" aria-label="Paper search and filters">
    <div class="reading-panel-head">
      <div>
        <h2 class="reading-panel-title">Find papers</h2>
        <p class="reading-panel-note">Journal and year are parsed from PDF names such as <code>Author_RES_2023.pdf</code>. Use one filter or combine several.</p>
      </div>
      <button id="readingResetFilters" class="reading-secondary-btn" type="button">Clear all</button>
    </div>

    <div class="reading-filter-stack">
      <div class="reading-search-line">
        <label class="reading-field reading-field-search" for="readingQuery">
          <span>Search</span>
          <input id="readingQuery" type="search" placeholder="Author / title / keyword / PDF file…" autocomplete="off">
        </label>
      </div>

      <div class="reading-filter-row">
        <label class="reading-field" for="readingInitialInput">
          <span>Author initials</span>
          <input id="readingInitialInput" type="text" inputmode="latin" placeholder="G R Y" aria-label="Author initials">
        </label>

        <label class="reading-field" for="readingYearInput">
          <span>Year</span>
          <input id="readingYearInput" type="text" inputmode="numeric" list="readingYearOptions" placeholder="2023 or 2020-2024" aria-label="Publication year">
          <datalist id="readingYearOptions"></datalist>
        </label>

        <div class="reading-field">
          <div class="reading-field-label">Journal</div>
          <details class="reading-journal-select" id="readingJournalDetails">
            <summary class="reading-journal-summary"><span id="readingJournalSummaryText">All</span></summary>
            <div class="reading-journal-menu" id="readingJournalMenu">
              <label class="reading-journal-option">
                <input id="readingJournalAll" type="checkbox" checked>
                <span>All journals</span>
              </label>
              <div id="readingJournalOptions"></div>
            </div>
          </details>
        </div>
      </div>
    </div>

    <details class="reading-advanced">
      <summary>A–Z initial picker</summary>
      <div class="reading-letter-grid" id="readingLetterButtons" aria-label="Author initials A to Z"></div>
    </details>

    <div class="reading-active-filters" id="readingActiveFilters" hidden></div>
    <div class="reading-count" id="readingCount"></div>
    <div class="reading-empty" id="readingEmpty">No matching papers. Try clearing one filter or using a broader keyword.</div>
  </section>

  <div class="reading-content-grid">
    <main class="reading-main">
      <details class="reading-picker">
        <summary>
          <span>Review picker</span>
          <span class="reading-picker-subtitle">Pick up to 10 PDFs from current results</span>
        </summary>
        <div class="reading-picker-body">
          <div class="reading-random-row">
            <button id="readingRandomBtn" type="button">Pick PDFs</button>
            <button id="readingCopyBtn" type="button" disabled>Copy names</button>
            <button id="readingDownloadNamesBtn" type="button" disabled>Download names</button>
            <button id="readingCopyDownloadBtn" type="button" disabled>Copy + download</button>
          </div>
          <div class="reading-random-status" id="readingRandomStatus" aria-live="polite"></div>
          <ol id="readingRandomList"></ol>
        </div>
      </details>

      <h2 class="reading-section-title" id="library">Library</h2>

      {% if items and items.size > 0 %}
        {% for p in items %}
          {% assign paper_authors = "" %}
          {% if p.author %}
            {% assign paper_authors = p.author %}
          {% elsif p.authors %}
            {% assign paper_authors = p.authors | join: ", " %}
          {% endif %}

          <article class="reading-entry"
               data-search="{{ paper_authors | escape }} {{ p.title | escape }} {{ p.file | escape }} {{ p.desc | escape }}"
               data-author="{{ paper_authors | escape }}"
               data-title="{{ p.title | escape }}"
               data-file="{{ p.file | escape }}">
            <div class="reading-entry-top">
              <div>
                <div class="reading-title">{{ p.title }}</div>
                {% if paper_authors and paper_authors != "" %}
                  <p class="reading-author"><strong>Author:</strong> {{ paper_authors }}</p>
                {% endif %}
                <p class="reading-file">
                  <strong>File:</strong>
                  <a href="{{ site.baseurl }}/reading/library/{{ p.file | uri_escape }}">{{ p.file }}</a>
                </p>
              </div>
              <div class="reading-card-meta" data-card-meta></div>
            </div>

            <details class="reading-note">
              <summary>Quick note</summary>
              <p class="reading-desc">{{ p.desc }}</p>
            </details>
          </article>
        {% endfor %}
      {% else %}
        <article class="reading-entry">
          <div class="reading-title">No papers yet.</div>
          <p class="reading-desc">Add entries to <code>_data/reading.yml</code> and upload PDFs to <code>reading/library/</code>.</p>
        </article>
      {% endif %}
    </main>

    <aside class="reading-side" aria-labelledby="readingGuideTitle">
      <div class="reading-side-title" id="readingGuideTitle">Matching PDFs</div>
      <p class="reading-side-hint">A focused PDF directory appears here after filtering. Use it to jump to papers quickly.</p>
      <div class="reading-guide-count" id="readingGuideCount"></div>
      <ul class="reading-guide-list" id="readingGuideList"></ul>
    </aside>
  </div>
</div>

<script>
(function(){
  const input = document.getElementById('readingQuery');
  const entries = Array.from(document.querySelectorAll('.reading-entry'));
  const count = document.getElementById('readingCount');
  const empty = document.getElementById('readingEmpty');

  const initialInput = document.getElementById('readingInitialInput');
  const letterButtonsWrap = document.getElementById('readingLetterButtons');

  const yearInput = document.getElementById('readingYearInput');
  const yearOptions = document.getElementById('readingYearOptions');

  const journalDetails = document.getElementById('readingJournalDetails');
  const journalSummaryText = document.getElementById('readingJournalSummaryText');
  const journalAll = document.getElementById('readingJournalAll');
  const journalOptionsWrap = document.getElementById('readingJournalOptions');
  const resetFiltersBtn = document.getElementById('readingResetFilters');
  const activeFiltersWrap = document.getElementById('readingActiveFilters');

  const guideCount = document.getElementById('readingGuideCount');
  const guideList = document.getElementById('readingGuideList');

  const randomBtn = document.getElementById('readingRandomBtn');
  const copyBtn = document.getElementById('readingCopyBtn');
  const downloadNamesBtn = document.getElementById('readingDownloadNamesBtn');
  const copyDownloadBtn = document.getElementById('readingCopyDownloadBtn');
  const randomList = document.getElementById('readingRandomList');
  const randomStatus = document.getElementById('readingRandomStatus');

  if (!input) return;

  const alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.split('');
  const maxGuideItems = 45;

  let selectedPDFs = [];
  let selectedDate = '';
  let selectedFilterSummary = '';
  let selectedInitials = new Set();
  let selectedJournals = new Set();
  let letterButtons = [];
  let journalCheckboxes = [];
  let lastVisibleItems = [];

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

  function uniqueSorted(values){
    return Array.from(new Set(values.filter(Boolean))).sort((a, b) => a.localeCompare(b));
  }

  function parseInitialSet(value){
    const letters = (value || '')
      .toString()
      .normalize('NFD')
      .replace(/[\u0300-\u036f]/g, '')
      .toUpperCase()
      .match(/[A-Z]/g) || [];

    return new Set(uniqueSorted(letters));
  }

  function syncInitialInput(){
    if (initialInput) {
      initialInput.value = Array.from(selectedInitials).sort().join(' ');
    }
  }

  function parseFileMeta(file){
    const base = (file || '').toString().replace(/\.pdf$/i, '');
    const parts = base.split('_').map(part => part.trim()).filter(Boolean);
    let year = '';
    let journal = '';
    let authorParts = [];

    for (let i = parts.length - 1; i >= 0; i -= 1) {
      const yearMatch = parts[i].match(/(?:19|20)\d{2}/);

      if (yearMatch) {
        year = yearMatch[0];
        journal = i > 0 ? parts[i - 1].toUpperCase() : '';
        authorParts = i > 1 ? parts.slice(0, i - 1) : [];
        break;
      }
    }

    return { year, journal, authorParts };
  }

  function initialsFromAuthorParts(parts){
    const initials = [];

    for (const part of parts || []) {
      const match = part
        .toString()
        .normalize('NFD')
        .replace(/[\u0300-\u036f]/g, '')
        .match(/[A-Za-z]/);

      if (match) initials.push(match[0].toUpperCase());
    }

    return uniqueSorted(initials);
  }

  function initialsFromAuthorField(author){
    const words = cleanSeed(author)
      .normalize('NFD')
      .replace(/[\u0300-\u036f]/g, '')
      .match(/[A-Za-z]+/g) || [];

    return uniqueSorted(words.map(word => word.charAt(0).toUpperCase()));
  }

  function firstInitialFromText(text){
    const match = cleanSeed(text)
      .normalize('NFD')
      .replace(/[\u0300-\u036f]/g, '')
      .match(/[A-Za-z]/);

    return match ? match[0].toUpperCase() : '';
  }

  function formatAuthorParts(parts){
    return (parts || []).filter(Boolean).join(', ');
  }

  function getEntryData(el){
    const link = el.querySelector('.reading-file a');
    const titleNode = el.querySelector('.reading-title');
    const author = (el.getAttribute('data-author') || '').trim();
    const title = (el.getAttribute('data-title') || (titleNode ? titleNode.textContent : '') || '').trim();
    const file = (el.getAttribute('data-file') || (link ? link.textContent : '') || '').trim();
    const href = link ? link.getAttribute('href') : '';
    const meta = parseFileMeta(file);

    let initials = initialsFromAuthorParts(meta.authorParts);

    if (initials.length === 0 && author) {
      initials = initialsFromAuthorField(author);
    }

    if (initials.length === 0) {
      const fallbackInitial = firstInitialFromText(title || file);
      initials = fallbackInitial ? [fallbackInitial] : [];
    }

    const fileAuthorLabel = formatAuthorParts(meta.authorParts);
    const authorDisplay = author || fileAuthorLabel;
    const searchText = [
      author,
      fileAuthorLabel,
      title,
      file,
      meta.journal,
      meta.year,
      el.textContent
    ].join(' ');

    return {
      el,
      author,
      authorDisplay,
      title,
      file,
      href,
      initials,
      year: meta.year,
      journal: meta.journal,
      search: norm(searchText),
      sortKey: norm(`${authorDisplay || title || file} ${meta.year} ${meta.journal} ${file}`)
    };
  }

  const paperData = entries
    .map(getEntryData)
    .filter(item => item.href && item.file);

  const dataByElement = new Map(paperData.map(item => [item.el, item]));

  function addCardPill(wrap, text){
    if (!wrap || !text) return;

    const pill = document.createElement('span');
    pill.className = 'reading-pill';
    pill.textContent = text;
    wrap.appendChild(pill);
  }

  function hydrateCardMeta(){
    for (const item of paperData) {
      const wrap = item.el.querySelector('[data-card-meta]');
      if (!wrap) continue;

      wrap.innerHTML = '';
      addCardPill(wrap, item.journal);
      addCardPill(wrap, item.year);
    }
  }

  function parseYearFilter(value){
    const raw = (value || '').toString();
    let remaining = raw;
    const years = new Set();
    const ranges = [];
    const rangeRegex = /((?:19|20)\d{2})\s*[-–—]\s*((?:19|20)\d{2})/g;
    let rangeMatch;

    while ((rangeMatch = rangeRegex.exec(raw)) !== null) {
      const start = Number(rangeMatch[1]);
      const end = Number(rangeMatch[2]);

      if (Number.isFinite(start) && Number.isFinite(end)) {
        ranges.push({
          start: Math.min(start, end),
          end: Math.max(start, end)
        });
      }
    }

    remaining = remaining.replace(rangeRegex, ' ');

    const yearMatches = remaining.match(/(?:19|20)\d{2}/g) || [];
    for (const year of yearMatches) years.add(year);

    return {
      raw: raw.trim(),
      years,
      ranges,
      hasFilter: years.size > 0 || ranges.length > 0
    };
  }

  function yearMatches(itemYear, yearFilter){
    if (!yearFilter.hasFilter) return true;
    if (!itemYear) return false;

    const numericYear = Number(itemYear);
    if (yearFilter.years.has(itemYear)) return true;

    for (const range of yearFilter.ranges) {
      if (numericYear >= range.start && numericYear <= range.end) return true;
    }

    return false;
  }

  function getFilters(){
    return {
      q: norm(input.value),
      rawSearch: (input.value || '').trim(),
      initials: new Set(selectedInitials),
      yearFilter: parseYearFilter(yearInput ? yearInput.value : ''),
      journals: new Set(selectedJournals)
    };
  }

  function hasActiveFilters(filters){
    return Boolean(
      filters.rawSearch ||
      filters.initials.size ||
      filters.yearFilter.hasFilter ||
      filters.journals.size
    );
  }

  function matchesSearch(item, filters){
    return !filters.q || item.search.includes(filters.q);
  }

  function matchesInitials(item, filters){
    if (!filters.initials.size) return true;

    for (const letter of filters.initials) {
      if (item.initials.includes(letter)) return true;
    }

    return false;
  }

  function matchesJournal(item, filters){
    return !filters.journals.size || filters.journals.has(item.journal);
  }

  function itemMatches(item, filters){
    return matchesSearch(item, filters) &&
      matchesInitials(item, filters) &&
      yearMatches(item.year, filters.yearFilter) &&
      matchesJournal(item, filters);
  }

  function itemMatchesIgnoringInitials(item, filters){
    return matchesSearch(item, filters) &&
      yearMatches(item.year, filters.yearFilter) &&
      matchesJournal(item, filters);
  }

  function itemMatchesIgnoringJournal(item, filters){
    return matchesSearch(item, filters) &&
      matchesInitials(item, filters) &&
      yearMatches(item.year, filters.yearFilter);
  }

  function getAvailableInitialCounts(filters){
    const counts = new Map();

    for (const item of paperData) {
      if (!itemMatchesIgnoringInitials(item, filters)) continue;

      for (const letter of item.initials) {
        counts.set(letter, (counts.get(letter) || 0) + 1);
      }
    }

    return counts;
  }

  function getJournalCounts(filters){
    const counts = new Map();

    for (const item of paperData) {
      if (!item.journal) continue;
      if (!itemMatchesIgnoringJournal(item, filters)) continue;
      counts.set(item.journal, (counts.get(item.journal) || 0) + 1);
    }

    return counts;
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
      btn.addEventListener('click', () => {
        if (selectedInitials.has(letter)) {
          selectedInitials.delete(letter);
        } else {
          selectedInitials.add(letter);
        }

        syncInitialInput();
        update();
      });

      letterButtonsWrap.appendChild(btn);
      letterButtons.push(btn);
    }
  }

  function updateLetterButtons(filters){
    const counts = getAvailableInitialCounts(filters);

    for (const btn of letterButtons) {
      const letter = btn.dataset.letter;
      const countForLetter = counts.get(letter) || 0;
      const isActive = selectedInitials.has(letter);
      const hasMatches = countForLetter > 0;

      btn.disabled = !hasMatches && !isActive;
      btn.classList.toggle('is-active', isActive);
      btn.setAttribute('aria-pressed', isActive ? 'true' : 'false');
      btn.title = hasMatches
        ? `${countForLetter} PDF${countForLetter === 1 ? '' : 's'} with author initial ${letter}`
        : `No PDFs found for author initial ${letter} under the current filters`;
    }
  }

  function buildYearOptions(){
    if (!yearOptions) return;

    const years = uniqueSorted(paperData.map(item => item.year)).sort((a, b) => Number(b) - Number(a));
    yearOptions.innerHTML = '';

    for (const year of years) {
      const option = document.createElement('option');
      option.value = year;
      yearOptions.appendChild(option);
    }
  }

  function buildJournalOptions(){
    if (!journalOptionsWrap) return;

    const journals = uniqueSorted(paperData.map(item => item.journal));
    journalOptionsWrap.innerHTML = '';
    journalCheckboxes = [];

    if (journals.length === 0) {
      const emptyMsg = document.createElement('div');
      emptyMsg.className = 'reading-journal-option is-muted';
      emptyMsg.textContent = 'No journal codes detected.';
      journalOptionsWrap.appendChild(emptyMsg);
      return;
    }

    for (const journal of journals) {
      const label = document.createElement('label');
      const checkbox = document.createElement('input');
      const text = document.createElement('span');

      label.className = 'reading-journal-option';
      checkbox.type = 'checkbox';
      checkbox.value = journal;
      checkbox.dataset.journal = journal;
      text.textContent = journal;

      checkbox.addEventListener('change', () => {
        if (checkbox.checked) {
          selectedJournals.add(journal);
        } else {
          selectedJournals.delete(journal);
        }

        update();
      });

      label.appendChild(checkbox);
      label.appendChild(text);
      journalOptionsWrap.appendChild(label);
      journalCheckboxes.push({ journal, checkbox, label, text });
    }
  }

  function updateJournalOptions(filters){
    const counts = getJournalCounts(filters);

    if (journalAll) journalAll.checked = selectedJournals.size === 0;

    for (const option of journalCheckboxes) {
      const countForJournal = counts.get(option.journal) || 0;
      const isActive = selectedJournals.has(option.journal);
      const hasMatches = countForJournal > 0;

      option.checkbox.checked = isActive;
      option.checkbox.disabled = !hasMatches && !isActive;
      option.label.classList.toggle('is-muted', !hasMatches && !isActive);
      option.text.textContent = hasMatches ? `${option.journal} (${countForJournal})` : option.journal;
    }

    if (!journalSummaryText) return;

    if (selectedJournals.size === 0) {
      journalSummaryText.textContent = 'All';
    } else if (selectedJournals.size === 1) {
      journalSummaryText.textContent = Array.from(selectedJournals)[0];
    } else {
      journalSummaryText.textContent = `${selectedJournals.size} selected`;
    }
  }

  function readableFilterSummary(filters){
    const parts = [];

    if (filters.rawSearch) parts.push(`search “${filters.rawSearch}”`);
    if (filters.initials.size) parts.push(`initials ${Array.from(filters.initials).sort().join(', ')}`);
    if (filters.yearFilter.raw) parts.push(`years ${filters.yearFilter.raw}`);
    if (filters.journals.size) parts.push(`journals ${Array.from(filters.journals).sort().join(', ')}`);

    return parts.length ? parts.join('; ') : 'no active filters';
  }

  function renderActiveFilters(filters){
    if (!activeFiltersWrap) return;

    activeFiltersWrap.innerHTML = '';

    if (!hasActiveFilters(filters)) {
      activeFiltersWrap.hidden = true;
      return;
    }

    activeFiltersWrap.hidden = false;

    function addChip(label, onRemove){
      const chip = document.createElement('button');
      const text = document.createElement('span');
      const close = document.createElement('strong');

      chip.type = 'button';
      chip.className = 'reading-filter-chip';
      text.textContent = label;
      close.textContent = '×';

      chip.appendChild(text);
      chip.appendChild(close);
      chip.addEventListener('click', onRemove);
      activeFiltersWrap.appendChild(chip);
    }

    if (filters.rawSearch) {
      addChip(`Search: ${filters.rawSearch}`, () => {
        input.value = '';
        update();
      });
    }

    for (const letter of Array.from(filters.initials).sort()) {
      addChip(`Initial: ${letter}`, () => {
        selectedInitials.delete(letter);
        syncInitialInput();
        update();
      });
    }

    if (filters.yearFilter.raw) {
      addChip(`Year: ${filters.yearFilter.raw}`, () => {
        if (yearInput) yearInput.value = '';
        update();
      });
    }

    for (const journal of Array.from(filters.journals).sort()) {
      addChip(`Journal: ${journal}`, () => {
        selectedJournals.delete(journal);
        update();
      });
    }
  }

  function makeGuideMeta(item){
    const parts = [];
    if (item.authorDisplay) parts.push(item.authorDisplay);

    const tags = [item.journal, item.year].filter(Boolean).join(', ');
    if (tags) parts.push(tags);

    return parts.join(' · ');
  }

  function renderGuide(visibleItems, filters){
    if (!guideList || !guideCount) return;

    guideList.innerHTML = '';

    if (!paperData.length) {
      guideCount.textContent = 'No PDF files found';
      const li = document.createElement('li');
      li.className = 'reading-guide-empty';
      li.textContent = 'Add entries to _data/reading.yml and upload PDFs to reading/library/.';
      guideList.appendChild(li);
      return;
    }

    if (!hasActiveFilters(filters)) {
      guideCount.textContent = `${fmtCount(paperData.length)} PDFs in the library`;
      const li = document.createElement('li');
      li.className = 'reading-guide-empty';
      li.textContent = 'Apply a filter to show a focused PDF directory here.';
      guideList.appendChild(li);
      return;
    }

    guideCount.textContent = `${fmtCount(visibleItems.length)} matching PDF${visibleItems.length === 1 ? '' : 's'}`;

    if (visibleItems.length === 0) {
      const li = document.createElement('li');
      li.className = 'reading-guide-empty';
      li.textContent = 'No PDFs match the current filter combination.';
      guideList.appendChild(li);
      return;
    }

    const shownItems = visibleItems.slice(0, maxGuideItems);

    for (const item of shownItems) {
      const li = document.createElement('li');
      const a = document.createElement('a');
      const meta = document.createElement('span');

      a.textContent = item.file;
      a.href = item.href;
      a.target = '_blank';
      a.rel = 'noopener';

      meta.className = 'reading-guide-meta';
      meta.textContent = makeGuideMeta(item);

      li.appendChild(a);
      if (meta.textContent) li.appendChild(meta);
      guideList.appendChild(li);
    }

    if (visibleItems.length > maxGuideItems) {
      const li = document.createElement('li');
      li.className = 'reading-guide-empty';
      li.textContent = `Showing the first ${fmtCount(maxGuideItems)} of ${fmtCount(visibleItems.length)} matches. Add another filter to narrow the list.`;
      guideList.appendChild(li);
    }
  }

  function update(){
    const filters = getFilters();
    const visibleItems = paperData
      .filter(item => itemMatches(item, filters))
      .sort((a, b) => a.sortKey.localeCompare(b.sortKey));
    const visibleSet = new Set(visibleItems);

    lastVisibleItems = visibleItems;

    for (const el of entries) {
      const item = dataByElement.get(el);

      if (!item) {
        el.hidden = paperData.length !== 0;
        continue;
      }

      el.hidden = !visibleSet.has(item);
    }

    if (count) {
      const base = `${visibleItems.length} / ${paperData.length} papers shown`;
      count.textContent = hasActiveFilters(filters) ? `${base} · ${readableFilterSummary(filters)}` : base;
    }

    if (empty) {
      empty.style.display = visibleItems.length === 0 ? 'block' : 'none';
    }

    renderGuide(visibleItems, filters);
    updateLetterButtons(filters);
    updateJournalOptions(filters);
    renderActiveFilters(filters);
  }

  function getLocalDateStamp(){
    const now = new Date();
    const year = now.getFullYear();
    const month = String(now.getMonth() + 1).padStart(2, '0');
    const day = String(now.getDate()).padStart(2, '0');
    return `${year}-${month}-${day}`;
  }

  function shuffle(items){
    return items
      .map(item => ({ item, randomValue: Math.random() }))
      .sort((a, b) => a.randomValue - b.randomValue)
      .map(obj => obj.item);
  }

  function setActionButtonsEnabled(enabled){
    if (copyBtn) copyBtn.disabled = !enabled;
    if (downloadNamesBtn) downloadNamesBtn.disabled = !enabled;
    if (copyDownloadBtn) copyDownloadBtn.disabled = !enabled;
  }

  function formatSelectedNames(){
    return selectedPDFs
      .map((pdf, index) => `${index + 1}. ${pdf.name}`)
      .join('\n');
  }

  function formatSelectedNamesFile(){
    return [
      `Random PDF Selection Date: ${selectedDate}`,
      `Filter Summary: ${selectedFilterSummary}`,
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
    const filters = getFilters();
    const currentItems = lastVisibleItems.length ? lastVisibleItems : paperData.filter(item => itemMatches(item, filters));

    selectedPDFs = shuffle(currentItems)
      .slice(0, 10)
      .map(item => ({
        name: item.file,
        href: item.href
      }));

    selectedDate = getLocalDateStamp();
    selectedFilterSummary = readableFilterSummary(filters);

    renderRandomList();
    setActionButtonsEnabled(selectedPDFs.length > 0);

    if (randomStatus) {
      randomStatus.textContent = selectedPDFs.length
        ? `Selected ${selectedPDFs.length} PDF name${selectedPDFs.length === 1 ? '' : 's'} from current results on ${selectedDate}.`
        : 'No PDFs were found under the current filters.';
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
      randomStatus.textContent = `Copied ${selectedPDFs.length} PDF name${selectedPDFs.length === 1 ? '' : 's'} to clipboard. Selection date: ${selectedDate}.`;
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
    a.download = `reading-selection-${selectedDate}.txt`;

    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);

    if (showStatus && randomStatus) {
      randomStatus.textContent = `Downloaded selected PDF names as reading-selection-${selectedDate}.txt.`;
    }

    return true;
  }

  async function copyAndDownloadSelectedNames(){
    if (!selectedPDFs.length) return;

    await copySelectedNames(false);
    downloadSelectedNames(false);

    if (randomStatus) {
      randomStatus.textContent = `Copied and downloaded ${selectedPDFs.length} PDF name${selectedPDFs.length === 1 ? '' : 's'} as reading-selection-${selectedDate}.txt.`;
    }
  }

  input.addEventListener('input', update);
  input.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
      input.value = '';
      update();
    }
  });

  if (initialInput) {
    initialInput.addEventListener('input', () => {
      selectedInitials = parseInitialSet(initialInput.value);
      update();
    });
    initialInput.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') {
        selectedInitials.clear();
        syncInitialInput();
        update();
      }
    });
  }

  if (yearInput) {
    yearInput.addEventListener('input', update);
    yearInput.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') {
        yearInput.value = '';
        update();
      }
    });
  }

  if (journalAll) {
    journalAll.addEventListener('change', () => {
      selectedJournals.clear();
      update();
    });
  }

  if (journalDetails) {
    document.addEventListener('click', (event) => {
      if (journalDetails.open && !journalDetails.contains(event.target)) {
        journalDetails.open = false;
      }
    });
  }

  if (resetFiltersBtn) {
    resetFiltersBtn.addEventListener('click', () => {
      input.value = '';
      selectedInitials.clear();
      selectedJournals.clear();
      if (initialInput) initialInput.value = '';
      if (yearInput) yearInput.value = '';
      update();
      input.focus();
    });
  }

  if (randomBtn) randomBtn.addEventListener('click', pickRandomPDFs);
  if (copyBtn) copyBtn.addEventListener('click', () => copySelectedNames(true));
  if (downloadNamesBtn) downloadNamesBtn.addEventListener('click', () => downloadSelectedNames(true));
  if (copyDownloadBtn) copyDownloadBtn.addEventListener('click', copyAndDownloadSelectedNames);

  hydrateCardMeta();
  buildLetterButtons();
  buildYearOptions();
  buildJournalOptions();
  setActionButtonsEnabled(false);
  update();
})();
</script>

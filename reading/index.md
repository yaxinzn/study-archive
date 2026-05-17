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
  grid-template-columns: minmax(0, 1fr) 330px;
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
.reading-clear-btn,
#readingClear,
#readingResetFilters{
  padding: 10px 12px;
  border: 1px solid rgba(0,0,0,.18);
  border-radius: 10px;
  background:#fff;
  font-weight: 650;
  cursor:pointer;
}
.reading-clear-btn:hover,
#readingClear:hover,
#readingResetFilters:hover{
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

/* Filter guide */
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
.reading-filter-group{
  margin: 14px 0;
  padding-top: 12px;
  border-top: 1px solid rgba(0,0,0,.08);
}
.reading-filter-group:first-of-type{
  border-top: 0;
  padding-top: 0;
}
.reading-filter-label{
  display:block;
  margin-bottom: 6px;
  font-size: 13px;
  font-weight: 850;
}
.reading-filter-help{
  margin: 6px 0 0 0;
  font-size: 12px;
  line-height: 1.4;
  opacity: .72;
}
.reading-input-row{
  display: flex;
  gap: 8px;
  align-items: center;
}
.reading-input-row input{
  width: 100%;
  min-width: 0;
  padding: 10px 12px;
  border: 1px solid rgba(0,0,0,.18);
  border-radius: 10px;
  font-size: 15px;
}
#readingInitialInput{
  text-transform: uppercase;
}
.reading-letter-grid{
  display: grid;
  grid-template-columns: repeat(6, 1fr);
  gap: 6px;
  margin: 8px 0 0 0;
}
.reading-letter-btn,
.reading-journal-btn{
  padding: 7px 0;
  border: 1px solid rgba(0,0,0,.16);
  border-radius: 8px;
  background: #fff;
  font-size: 12px;
  font-weight: 750;
  cursor: pointer;
}
.reading-letter-btn:hover:not(:disabled),
.reading-journal-btn:hover:not(:disabled){
  transform: translateY(-1px);
}
.reading-letter-btn.is-active,
.reading-journal-btn.is-active{
  background: #0f3d2e;
  border-color: #0f3d2e;
  color: #fff;
}
.reading-letter-btn:disabled,
.reading-journal-btn:disabled{
  opacity: .32;
  cursor: not-allowed;
}
.reading-journal-grid{
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
  margin-top: 8px;
}
.reading-journal-btn{
  padding: 7px 9px;
}
.reading-active-filters{
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
  margin-top: 8px;
}
.reading-filter-chip{
  display: inline-flex;
  align-items: center;
  gap: 5px;
  max-width: 100%;
  padding: 6px 8px;
  border: 1px solid rgba(0,0,0,.14);
  border-radius: 999px;
  background: rgba(15,61,46,.06);
  font-size: 12px;
  line-height: 1.2;
  cursor: pointer;
}
.reading-filter-chip:hover{
  transform: translateY(-1px);
}
.reading-filter-chip span{
  overflow-wrap: anywhere;
}
.reading-filter-chip strong{
  font-size: 13px;
}
.reading-guide-count{
  margin-top: 10px;
  padding-top: 12px;
  border-top: 1px solid rgba(0,0,0,.08);
  font-size: 13px;
  font-weight: 850;
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
.reading-guide-tags{
  display: flex;
  flex-wrap: wrap;
  gap: 5px;
  margin-top: 5px;
}
.reading-guide-tag{
  padding: 2px 6px;
  border: 1px solid rgba(0,0,0,.12);
  border-radius: 999px;
  font-size: 11px;
  opacity: .82;
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
        <button id="readingClear" type="button">Clear Search</button>
      </div>
      <div class="reading-count" id="readingCount"></div>
      <div class="reading-empty" id="readingEmpty">No matching papers. Try clearing one filter or using a broader keyword.</div>
    </div>

    <div class="reading-random">
      <div class="reading-random-row">
        <button id="readingRandomBtn" type="button">Pick 10 Random PDFs from Current Results</button>
        <button id="readingCopyBtn" type="button" disabled>Copy Selected Names</button>
        <button id="readingDownloadNamesBtn" type="button" disabled>Download Selected Names</button>
        <button id="readingCopyDownloadBtn" type="button" disabled>Copy + Download Names</button>
      </div>

      <div class="reading-random-note">
        Reading check: randomly select up to 10 PDF files from the currently filtered results. If no filters are active, the full library is used.
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
    <div class="reading-guide-title" id="readingGuideTitle">PDF Filter Guide</div>
    <p class="reading-guide-desc">
      Combine author initials, publication years, and journal codes to quickly narrow the library. Journal and year are read from the PDF file name pattern <code>Author_Journal_Year.pdf</code>.
    </p>

    <div class="reading-filter-group">
      <label class="reading-filter-label" for="readingInitialInput">Author Initials</label>
      <div class="reading-input-row">
        <input id="readingInitialInput" type="text" inputmode="latin" placeholder="G R Y" aria-label="Author initials">
        <button id="readingInitialClear" class="reading-clear-btn" type="button">Clear</button>
      </div>
      <p class="reading-filter-help">Enter one or more letters, such as <strong>G</strong>, <strong>GR</strong>, or <strong>G R Y</strong>. Matches any selected initial.</p>
      <div class="reading-letter-grid" id="readingLetterButtons" aria-label="Author initials A to Z"></div>
    </div>

    <div class="reading-filter-group">
      <label class="reading-filter-label" for="readingYearInput">Publication Year</label>
      <div class="reading-input-row">
        <input id="readingYearInput" type="text" inputmode="numeric" list="readingYearOptions" placeholder="2023" aria-label="Publication year">
        <button id="readingYearClear" class="reading-clear-btn" type="button">Clear</button>
      </div>
      <datalist id="readingYearOptions"></datalist>
      <p class="reading-filter-help">Use one year, multiple years, or a range: <strong>2023</strong>, <strong>2020 2023</strong>, or <strong>2020-2024</strong>.</p>
    </div>

    <div class="reading-filter-group">
      <div class="reading-filter-label">Journal</div>
      <p class="reading-filter-help">Journal codes are extracted from the token before the year, such as <strong>RES</strong>, <strong>RFS</strong>, <strong>JFE</strong>, or <strong>QJE</strong>.</p>
      <div class="reading-journal-grid" id="readingJournalButtons" aria-label="Journal filters"></div>
    </div>

    <div class="reading-filter-group">
      <div class="reading-filter-label">Active Filters</div>
      <button id="readingResetFilters" type="button">Reset All Filters</button>
      <div class="reading-active-filters" id="readingActiveFilters"></div>
    </div>

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

  const yearInput = document.getElementById('readingYearInput');
  const yearClearBtn = document.getElementById('readingYearClear');
  const yearOptions = document.getElementById('readingYearOptions');

  const journalButtonsWrap = document.getElementById('readingJournalButtons');
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

  let selectedPDFs = [];
  let selectedDate = '';
  let selectedFilterSummary = '';
  let selectedInitials = new Set();
  let selectedJournals = new Set();
  let letterButtons = [];
  let journalButtons = [];
  let lastVisibleItems = [];

  if (!input) return;

  const alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.split('');
  const maxGuideItems = 80;

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

    return {
      year,
      journal,
      authorParts
    };
  }

  function initialsFromAuthorParts(parts){
    const initials = [];

    for (const part of parts || []) {
      const match = part
        .toString()
        .normalize('NFD')
        .replace(/[\u0300-\u036f]/g, '')
        .match(/[A-Za-z]/);

      if (match) {
        initials.push(match[0].toUpperCase());
      }
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
    return (parts || [])
      .filter(Boolean)
      .join(', ');
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

    for (const year of yearMatches) {
      years.add(year);
    }

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
      if (numericYear >= range.start && numericYear <= range.end) {
        return true;
      }
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
      if (item.initials.includes(letter)) {
        return true;
      }
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

  function buildJournalButtons(){
    if (!journalButtonsWrap) return;

    const journals = uniqueSorted(paperData.map(item => item.journal));
    journalButtonsWrap.innerHTML = '';
    journalButtons = [];

    if (journals.length === 0) {
      const emptyMsg = document.createElement('div');
      emptyMsg.className = 'reading-guide-empty';
      emptyMsg.textContent = 'No journal codes were detected from the PDF file names.';
      journalButtonsWrap.appendChild(emptyMsg);
      return;
    }

    const allBtn = document.createElement('button');
    allBtn.type = 'button';
    allBtn.className = 'reading-journal-btn';
    allBtn.dataset.journal = '__ALL__';
    allBtn.textContent = 'All';
    allBtn.setAttribute('aria-pressed', 'true');
    allBtn.addEventListener('click', () => {
      selectedJournals.clear();
      update();
    });
    journalButtonsWrap.appendChild(allBtn);
    journalButtons.push(allBtn);

    for (const journal of journals) {
      const btn = document.createElement('button');

      btn.type = 'button';
      btn.className = 'reading-journal-btn';
      btn.dataset.journal = journal;
      btn.textContent = journal;
      btn.setAttribute('aria-pressed', 'false');
      btn.addEventListener('click', () => {
        if (selectedJournals.has(journal)) {
          selectedJournals.delete(journal);
        } else {
          selectedJournals.add(journal);
        }

        update();
      });

      journalButtonsWrap.appendChild(btn);
      journalButtons.push(btn);
    }
  }

  function updateJournalButtons(filters){
    const counts = getJournalCounts(filters);

    for (const btn of journalButtons) {
      const journal = btn.dataset.journal;

      if (journal === '__ALL__') {
        const isActive = selectedJournals.size === 0;
        btn.classList.toggle('is-active', isActive);
        btn.setAttribute('aria-pressed', isActive ? 'true' : 'false');
        btn.disabled = false;
        btn.title = 'Show all journals';
        continue;
      }

      const countForJournal = counts.get(journal) || 0;
      const isActive = selectedJournals.has(journal);
      const hasMatches = countForJournal > 0;

      btn.disabled = !hasMatches && !isActive;
      btn.classList.toggle('is-active', isActive);
      btn.setAttribute('aria-pressed', isActive ? 'true' : 'false');
      btn.textContent = hasMatches ? `${journal} (${countForJournal})` : journal;
      btn.title = hasMatches
        ? `${countForJournal} PDF${countForJournal === 1 ? '' : 's'} in ${journal} under the current filters`
        : `No ${journal} PDFs found under the current filters`;
    }
  }

  function readableFilterSummary(filters){
    const parts = [];

    if (filters.rawSearch) {
      parts.push(`search “${filters.rawSearch}”`);
    }

    if (filters.initials.size) {
      parts.push(`initials ${Array.from(filters.initials).sort().join(', ')}`);
    }

    if (filters.yearFilter.raw) {
      parts.push(`years ${filters.yearFilter.raw}`);
    }

    if (filters.journals.size) {
      parts.push(`journals ${Array.from(filters.journals).sort().join(', ')}`);
    }

    return parts.length ? parts.join('; ') : 'no active filters';
  }

  function renderActiveFilters(filters){
    if (!activeFiltersWrap) return;

    activeFiltersWrap.innerHTML = '';

    if (!hasActiveFilters(filters)) {
      const emptyChip = document.createElement('span');
      emptyChip.className = 'reading-filter-help';
      emptyChip.textContent = 'No active filters.';
      activeFiltersWrap.appendChild(emptyChip);
      return;
    }

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
    const meta = [];

    if (item.authorDisplay) {
      meta.push(item.authorDisplay);
    }

    if (item.title) {
      meta.push(item.title);
    }

    return meta.join(' — ');
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
      guideCount.textContent = `${paperData.length} PDFs in the library`;
      const li = document.createElement('li');
      li.className = 'reading-guide-empty';
      li.textContent = 'Choose an author initial, year, journal, or keyword to build a focused PDF list here.';
      guideList.appendChild(li);
      return;
    }

    guideCount.textContent = `${visibleItems.length} matching PDF${visibleItems.length === 1 ? '' : 's'}`;

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
      const tags = document.createElement('span');

      a.textContent = item.file;
      a.href = item.href;
      a.target = '_blank';
      a.rel = 'noopener';

      meta.className = 'reading-guide-meta';
      meta.textContent = makeGuideMeta(item);

      tags.className = 'reading-guide-tags';

      if (item.journal) {
        const journalTag = document.createElement('span');
        journalTag.className = 'reading-guide-tag';
        journalTag.textContent = item.journal;
        tags.appendChild(journalTag);
      }

      if (item.year) {
        const yearTag = document.createElement('span');
        yearTag.className = 'reading-guide-tag';
        yearTag.textContent = item.year;
        tags.appendChild(yearTag);
      }

      if (item.initials.length) {
        const initialTag = document.createElement('span');
        initialTag.className = 'reading-guide-tag';
        initialTag.textContent = `Initials: ${item.initials.join(', ')}`;
        tags.appendChild(initialTag);
      }

      li.appendChild(a);
      if (meta.textContent) li.appendChild(meta);
      if (tags.children.length) li.appendChild(tags);
      guideList.appendChild(li);
    }

    if (visibleItems.length > maxGuideItems) {
      const li = document.createElement('li');
      li.className = 'reading-guide-empty';
      li.textContent = `Showing the first ${maxGuideItems} of ${visibleItems.length} matches. Add another filter to narrow the list.`;
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
        el.style.display = paperData.length === 0 ? '' : 'none';
        continue;
      }

      const ok = visibleSet.has(item);
      el.style.display = ok ? '' : 'none';
    }

    if (count) {
      count.textContent = `${visibleItems.length} / ${paperData.length} papers shown · ${readableFilterSummary(filters)}`;
    }

    if (empty) {
      empty.style.display = visibleItems.length === 0 ? 'block' : 'none';
    }

    renderGuide(visibleItems, filters);
    updateLetterButtons(filters);
    updateJournalButtons(filters);
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

    const hasSelection = selectedPDFs.length > 0;
    setActionButtonsEnabled(hasSelection);

    if (randomStatus) {
      if (hasSelection) {
        randomStatus.textContent = `Selected ${selectedPDFs.length} PDF name${selectedPDFs.length === 1 ? '' : 's'} from current results on ${selectedDate}.`;
      } else {
        randomStatus.textContent = 'No PDFs were found under the current filters.';
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
    selectedInitials = parseInitialSet(initialInput.value);
    update();
  });

  initialInput && initialInput.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
      selectedInitials.clear();
      syncInitialInput();
      update();
    }
  });

  initialClearBtn && initialClearBtn.addEventListener('click', () => {
    selectedInitials.clear();
    syncInitialInput();
    update();
    initialInput && initialInput.focus();
  });

  yearInput && yearInput.addEventListener('input', update);

  yearInput && yearInput.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
      yearInput.value = '';
      update();
    }
  });

  yearClearBtn && yearClearBtn.addEventListener('click', () => {
    if (yearInput) {
      yearInput.value = '';
      update();
      yearInput.focus();
    }
  });

  resetFiltersBtn && resetFiltersBtn.addEventListener('click', () => {
    input.value = '';
    selectedInitials.clear();
    selectedJournals.clear();

    if (initialInput) initialInput.value = '';
    if (yearInput) yearInput.value = '';

    update();
    input.focus();
  });

  randomBtn && randomBtn.addEventListener('click', pickRandomPDFs);
  copyBtn && copyBtn.addEventListener('click', () => copySelectedNames(true));
  downloadNamesBtn && downloadNamesBtn.addEventListener('click', () => downloadSelectedNames(true));
  copyDownloadBtn && copyDownloadBtn.addEventListener('click', copyAndDownloadSelectedNames);

  buildLetterButtons();
  buildYearOptions();
  buildJournalButtons();
  setActionButtonsEnabled(false);
  update();
})();
</script>

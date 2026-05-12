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
.reading-callout-title{ font-weight: 850; margin-bottom: 6px; }
.reading-callout p{ margin: 8px 0; }
.reading-small{ opacity: .88; }

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
#readingClear:hover{ transform: translateY(-1px); }
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
#readingRandomBtn{
  padding: 10px 12px;
  border: 1px solid rgba(0,0,0,.18);
  border-radius: 10px;
  background:#fff;
  font-weight: 650;
  cursor:pointer;
}
#readingRandomBtn:hover{ transform: translateY(-1px); }
.reading-random-note{
  margin-top: 8px;
  opacity: .78;
  font-size: 13px;
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
.reading-title{ font-weight: 800; }
.reading-file{ margin-top: 10px; }
.reading-desc{ margin-top: 8px; opacity: .90; }
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
  </div>
  <div class="reading-random-note">
    Reading check: randomly select 10 PDF files from the library.
  </div>
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
  const randomList = document.getElementById('readingRandomList');

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

    if (count) count.textContent = `${shown} / ${entries.length} papers`;
    if (empty) empty.style.display = (shown === 0) ? 'block' : 'none';
  }

  function pickRandomPDFs(){
    if (!randomList) return;

    const pdfs = Array.from(document.querySelectorAll('.reading-file a'))
      .map(a => ({
        name: a.textContent.trim(),
        href: a.getAttribute('href')
      }))
      .filter(x => x.name);

    const shuffled = pdfs
      .map(x => ({ x, r: Math.random() }))
      .sort((a, b) => a.r - b.r)
      .map(o => o.x)
      .slice(0, 10);

    randomList.innerHTML = '';

    if (shuffled.length === 0) {
      randomList.innerHTML = '<li>No PDFs found.</li>';
      return;
    }

    for (const pdf of shuffled) {
      const li = document.createElement('li');
      const a = document.createElement('a');

      a.textContent = pdf.name;
      a.href = pdf.href;

      li.appendChild(a);
      randomList.appendChild(li);
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

  update();
})();
</script>

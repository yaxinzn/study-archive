---
layout: sc
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
.reading-count{ margin-top: 8px; opacity: .78; font-size: 13px; }
.reading-empty{
  display:none;
  margin-top: 8px;
  padding: 10px 12px;
  border: 1px dashed rgba(0,0,0,.18);
  border-radius: 10px;
  background: rgba(0,0,0,.02);
  opacity: .85;
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
.reading-meta{ opacity: .86; margin-top: 4px; }
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
  <div class="reading-empty" id="readingEmpty">No matching papers. Try a different keyword (e.g., author surname).</div>
</div>

## Library


<div class="reading-entry">
  <div class="reading-title">Kilic & Tuzel (JFE, 2026) — Investing in Misallocation.</div>
  <div class="reading-meta">Paper-reading note PDF</div>

  <p class="reading-file"><strong>File:</strong>
    <a href="{{ site.baseurl }}/reading/library/Kilic_Tuzel_JFE_2026_StudyNotes.pdf">Kilic_Tuzel_JFE_2026_StudyNotes.pdf</a>
  </p>

  <p class="reading-desc">This file summarizes the paper’s core mechanism and provides a structured walkthrough of its reduced-form regressions, structural model equations, and detailed interpretations of every table and figure.</p>
</div>


<div class="reading-entry">
  <div class="reading-title">He & Song (RFS, 2026) — Agency MBS as Safe Assets</div>
  <div class="reading-meta">Paper-reading note PDF</div>

  <p class="reading-file"><strong>File:</strong>
    <a href="{{ site.baseurl }}/reading/library/He_Song_RFS_2026.pdf">He_Song_RFS_2026.pdf</a>
  </p>

  <p class="reading-desc">This file summarizes the paper’s core mechanism and provides a structured walkthrough of its reduced-form regressions, structural model equations, and detailed interpretations of every table and figure.</p>
</div>


<div class="reading-entry">
  <div class="reading-title">Korteweg (JF, 2010) — The Net Benefits to Leverage</div>
  <div class="reading-meta">Paper-reading note PDF</div>

  <p class="reading-file"><strong>File:</strong>
    <a href="{{ site.baseurl }}/reading/library/Korteweg_JF_2010.pdf">Korteweg_JF_2010.pdf</a>
  </p>

  <p class="reading-desc">This file summarizes the paper’s core mechanism and provides a structured walkthrough of its reduced-form regressions, structural model equations, and detailed interpretations of every table and figure.</p>
</div>


<div class="reading-entry">
  <div class="reading-title">Keys, Mukherjee, Seru & Vig (QJE, 2010) — Did Securitization Lead to Lax Screening?</div>
  <div class="reading-meta">Paper-reading note PDF</div>

  <p class="reading-file"><strong>File:</strong>
    <a href="{{ site.baseurl }}/reading/library/Keys_Mukherjee_Seru_and_Vig_QJE_2010.pdf">Keys_Mukherjee_Seru_and_Vig_QJE_2010.pdf</a>
  </p>

  <p class="reading-desc">This file distills the RD identification around the FICO=620 securitization cutoff, clarifies the hard- vs. soft-information screening mechanism, and provides a structured walkthrough of the key equations and the interpretation of the main tables and figures (first-stage volume jump, balance tests, delinquency results, policy interaction, and falsification tests).</p>
</div>


<div class="reading-entry">
  <div class="reading-title">Dunne, Klimek, Roberts & Xu (RAND J Econ, 2013) — Entry, Exit, and the Determinants of Market Structure</div>
  <div class="reading-meta">Paper-reading note PDF</div>

  <p class="reading-file"><strong>File:</strong>
    <a href="{{ site.baseurl }}/reading/library/Dunne__Klimek__Roberts__and_Xu__RAND_J__Econ___2013_.pdf">Dunne__Klimek__Roberts__and_Xu__RAND_J__Econ___2013_.pdf</a>
  </p>

  <p class="reading-desc">This file summarizes the paper’s dynamic entry–exit framework (Pakes–Olley–Bresnahan style), walks through reduced-form profit estimation and structural cost/entry components, and interprets the key tables/figures (entry/exit transitions and the entry-subsidy counterfactual).</p>
</div>

<script>
(function(){
  const input = document.getElementById('readingQuery');
  const clearBtn = document.getElementById('readingClear');
  const entries = Array.from(document.querySelectorAll('.reading-entry'));
  const count = document.getElementById('readingCount');
  const empty = document.getElementById('readingEmpty');
  if (!input) return;

  function norm(x){ return (x || '').toLowerCase().replace(/\s+/g,' ').trim(); }

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

  for (const el of entries) {
    if (!el.getAttribute('data-search')) el.setAttribute('data-search', el.textContent);
  }

  input.addEventListener('input', update);
  clearBtn && clearBtn.addEventListener('click', () => { input.value=''; update(); input.focus(); });
  input.addEventListener('keydown', (e) => { if (e.key === 'Escape') { input.value=''; update(); } });
  update();
})();
</script>

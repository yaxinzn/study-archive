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
  margin: 16px 0 22px 0;
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
.reading-callout p{ margin: 8px 0; }
.reading-small{ opacity: .88; }
.reading-card{
  margin: 16px 0;
  padding: 14px 16px;
  border: 1px solid rgba(0,0,0,.10);
  border-radius: 10px;
  background: #fff;
}
.reading-card-title{
  font-weight: 800;
}
.reading-meta{
  opacity: .85;
  margin-top: 4px;
}

/* --- Reading search --- */
.reading-search{
  margin: 16px 0 22px 0;
  padding: 12px 14px;
  border: 1px solid rgba(0,0,0,.10);
  border-radius: 10px;
  background: #fff;
}
.reading-search-row{
  display: flex;
  gap: 10px;
  flex-wrap: wrap;
  align-items: center;
}
#readingQuery{
  flex: 1 1 360px;
  padding: 10px 12px;
  border: 1px solid rgba(0,0,0,.18);
  border-radius: 10px;
  font-size: 15px;
}
#readingClear{
  padding: 10px 12px;
  border: 1px solid rgba(0,0,0,.18);
  border-radius: 10px;
  background: #fff;
  font-weight: 650;
  cursor: pointer;
}
#readingClear:hover{ transform: translateY(-1px); }
.reading-count{
  margin-top: 8px;
  opacity: .78;
  font-size: 13px;
}
.reading-empty{
  display: none;
  margin-top: 8px;
  padding: 10px 12px;
  border: 1px dashed rgba(0,0,0,.18);
  border-radius: 10px;
  background: rgba(0,0,0,.02);
  opacity: .85;
}

</style>

<div style="opacity:.86; margin-top:4px;">Paper-reading note PDF</div>

  <p style="margin-top:10px;">
    <strong>File:</strong>
    <a href="{{ site.baseurl }}/reading/library/Kilic_Tuzel_JFE_2026_StudyNotes.pdf">Kilic_Tuzel_JFE_2026_StudyNotes.pdf</a>
  </p>

  <p style="opacity:.90; margin-top:6px;">
    This file summarizes the paper’s core mechanism and provides a structured walkthrough of its reduced-form regressions, structural model equations, and detailed interpretations of every table and figure.
  </p>
</div>


<script>
(function(){
  const input = document.getElementById('readingQuery');
  const clearBtn = document.getElementById('readingClear');
  const entries = Array.from(document.querySelectorAll('.reading-entry'));
  const count = document.getElementById('readingCount');
  const empty = document.getElementById('readingEmpty');

  if (!input || entries.length === 0) {
    if (count) count.textContent = '';
    return;
  }

  function norm(x){ return (x || '').toLowerCase().replace(/\s+/g,' ').trim(); }

  function updateReadingFilter(){
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

  // Precompute searchable text once
  for (const el of entries) {
    if (!el.getAttribute('data-search')) {
      el.setAttribute('data-search', el.textContent);
    }
  }

  input.addEventListener('input', updateReadingFilter);
  clearBtn && clearBtn.addEventListener('click', () => { input.value=''; updateReadingFilter(); input.focus(); });

  // ESC clears
  input.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') { input.value=''; updateReadingFilter(); }
  });

  updateReadingFilter();
  window.updateReadingFilter = updateReadingFilter;
})();
</script>


<div class="reading-search" style="margin:16px 0 22px 0; padding:12px 14px; border:1px solid rgba(0,0,0,.10); border-radius:10px; background:#fff;">
  <div style="display:flex; gap:10px; flex-wrap:wrap; align-items:center;">
    <input id="readingQuery" type="search" placeholder="Search by author / title / keywords…" autocomplete="off"
           style="flex:1 1 360px; padding:10px 12px; border:1px solid rgba(0,0,0,.18); border-radius:10px; font-size:15px;">
    <button id="readingClear" type="button"
            style="padding:10px 12px; border:1px solid rgba(0,0,0,.18); border-radius:10px; background:#fff; font-weight:650; cursor:pointer;">
      Clear
    </button>
  </div>
  <div id="readingCount" style="margin-top:8px; opacity:.78; font-size:13px;"></div>
  <div id="readingEmpty" style="display:none; margin-top:8px; padding:10px 12px; border:1px dashed rgba(0,0,0,.18); border-radius:10px; background:rgba(0,0,0,.02); opacity:.85;">
    No matching papers.
  </div>
</div>


## Library




<div class="reading-entry" style="margin:16px 0; padding:14px 16px; border:1px solid rgba(0,0,0,.10); border-left:4px solid #0f3d2e; border-radius:10px; background:#fff;">
  <div style="font-weight:800;">Kilic &amp; Tuzel (2026) — Investing in Misallocation (Quick Notes)</div>
  <div style="opacity:.86; margin-top:4px;">Paper-reading note PDF</div>

  <p style="margin-top:10px;">
    <strong>File:</strong>
    <a href="{{ site.baseurl }}/reading/library/Kilic_Tuzel_JFE_2026_StudyNotes.pdf">Kilic_Tuzel_JFE_2026_StudyNotes.pdf</a>
  </p>

  <p style="opacity:.90; margin-top:6px;">This file summarizes the paper’s core mechanism and provides a structured walkthrough of its reduced-form regressions, structural model equations, and detailed interpretations of every table and figure.</p>
</div>

<div class="reading-entry" style="margin:16px 0; padding:14px 16px; border:1px solid rgba(0,0,0,.10); border-left:4px solid #0f3d2e; border-radius:10px; background:#fff;">
  <div style="font-weight:800;">He &amp; Song (RFS, 2026) — Agency MBS as Safe Assets (Quick Notes)</div>
  <div style="opacity:.86; margin-top:4px;">Paper-reading note PDF</div>

  <p style="margin-top:10px;">
    <strong>File:</strong>
    <a href="{{ site.baseurl }}/reading/library/He_Song_RFS_2026.pdf">He_Song_RFS_2026.pdf</a>
  </p>

  <p style="opacity:.90; margin-top:6px;">This file summarizes the paper’s core mechanism and provides a structured walkthrough of its reduced-form regressions, structural model equations, and detailed interpretations of every table and figure.</p>
</div>

<div class="reading-entry" style="margin:16px 0; padding:14px 16px; border:1px solid rgba(0,0,0,.10); border-left:4px solid #0f3d2e; border-radius:10px; background:#fff;">
  <div style="font-weight:800;">Korteweg (JF, 2010) — The Net Benefits to Leverage (Quick Notes)</div>
  <div style="opacity:.86; margin-top:4px;">Paper-reading note PDF</div>

  <p style="margin-top:10px;">
    <strong>File:</strong>
    <a href="{{ site.baseurl }}/reading/library/Korteweg_JF_2010.pdf">Korteweg_JF_2010.pdf</a>
  </p>

  <p style="opacity:.90; margin-top:6px;">This file summarizes the paper’s core mechanism and provides a structured walkthrough of its reduced-form regressions, structural model equations, and detailed interpretations of every table and figure.</p>
</div>

<div class="reading-entry" style="margin:16px 0; padding:14px 16px; border:1px solid rgba(0,0,0,.10); border-left:4px solid #0f3d2e; border-radius:10px; background:#fff;">
  <div style="font-weight:800;">Keys, Mukherjee, Seru &amp; Vig (QJE, 2010) — Did Securitization Lead to Lax Screening? (Quick Notes)</div>
  <div style="opacity:.86; margin-top:4px;">Paper-reading note PDF</div>

  <p style="margin-top:10px;">
    <strong>File:</strong>
    <a href="{{ site.baseurl }}/reading/library/Keys_Mukherjee_Seru_and_Vig_QJE_2010.pdf">Keys_Mukherjee_Seru_and_Vig_QJE_2010.pdf</a>
  </p>

  <p style="opacity:.90; margin-top:6px;">This file distills the RD identification around the FICO=620 securitization cutoff, clarifies the hard- vs. soft-information screening mechanism, and provides a structured walkthrough of the key equations and the interpretation of the main tables and figures (first-stage volume jump, balance tests, delinquency results, policy interaction, and falsification tests).</p>
</div>

<div class="reading-entry" style="margin:16px 0; padding:14px 16px; border:1px solid rgba(0,0,0,.10); border-left:4px solid #0f3d2e; border-radius:10px; background:#fff;">
  <div style="font-weight:800;">Dunne, Klimek, Roberts &amp; Xu (RAND J Econ, 2013) — Entry, Exit, and the Determinants of Market Structure (Quick Notes)</div>
  <div style="opacity:.86; margin-top:4px;">Paper-reading note PDF</div>

  <p style="margin-top:10px;">
    <strong>File:</strong>
    <a href="{{ site.baseurl }}/reading/library/Dunne__Klimek__Roberts__and_Xu__RAND_J__Econ___2013_.pdf">Dunne__Klimek__Roberts__and_Xu__RAND_J__Econ___2013_.pdf</a>
  </p>

  <p style="opacity:.90; margin-top:6px;">This file summarizes the paper’s dynamic entry–exit framework (Pakes–Olley–Bresnahan style), walks through reduced-form profit estimation and structural cost/entry components, and interprets the key tables/figures (entry/exit transitions and the entry-subsidy counterfactual).</p>
</div>
<div style="opacity:.86; margin-top:4px;">Paper-reading note PDF</div>

  <p style="margin-top:10px;">
    <strong>File:</strong>
    <a href="{{ site.baseurl }}/reading/library/Dunne__Klimek__Roberts__and_Xu__RAND_J__Econ___2013_.pdf">Dunne__Klimek__Roberts__and_Xu__RAND_J__Econ___2013_.pdf</a>
  </p>

  <p style="opacity:.90; margin-top:6px;">
    This file summarizes the paper’s dynamic entry–exit framework (Pakes–Olley–Bresnahan style), walks through the reduced-form profit estimation and the structural cost/entry components, and interprets the key tables and figures (state transitions, entry/exit probabilities, and the entry-subsidy counterfactual).
  </p>
</div>


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
</style>

<div class="reading-callout">
  <div class="reading-callout-title">What this page is for</div>
  <p>
    This page is designed to give you a <strong>quick reading</strong> of papers.
    Each entry is short and operational: the goal is to extract <strong>identification</strong>,
    <strong>key variables</strong>, and <strong>replication-ready hooks</strong>.
  </p>
  <p class="reading-small">
    My reading notes are a living document. If anything is unclear or incorrect, please tell me—I will revise and improve it.
  </p>
</div>


## Library






<div style="margin:16px 0; padding:14px 16px; border:1px solid rgba(0,0,0,.10); border-left:4px solid #0f3d2e; border-radius:10px; background:#fff;">
  <div style="font-weight:800;">He &amp; Song (RFS, 2026) — Agency MBS as Safe Assets (Quick Notes)</div>
  <div style="opacity:.86; margin-top:4px;">Paper-reading note PDF</div>

  <p style="margin-top:10px;">
    <strong>File:</strong>
    <a href="{{ site.baseurl }}/reading/library/He_Song_RFS_2026.pdf">He_Song_RFS_2026.pdf</a>
  </p>

  <p style="opacity:.90; margin-top:6px;">
    This file summarizes the paper’s core mechanism and provides a structured walkthrough of its reduced-form regressions, structural model equations, and detailed interpretations of every table and figure.
  </p>
</div>


<div class="reading-card">
  <div class="reading-card-title">
    Dunne, Klimek, Roberts, and Xu (2013) — Entry, exit, and the determinants of market structure
  </div>
  <div class="reading-meta">
    Dynamic structural entry–exit model (POB-style); application to dentists vs chiropractors; counterfactual entry subsidy.
  </div>

  <p style="margin-top:10px;">
    PDF notes:
    <a href="{{ site.baseurl }}/reading/library/Dunne__Klimek__Roberts__and_Xu__RAND_J__Econ___2013_.pdf">
      Dunne__Klimek__Roberts__and_Xu__RAND_J__Econ___2013_.pdf
    </a>
  </p>

  <details style="margin-top:10px;">
    <summary><strong>Quick reading (1–2 minutes)</strong></summary>
    <ul>
      <li><strong>Core question:</strong> how competition (profits vs n), fixed costs (exit), and entry costs (entry) jointly determine market structure.</li>
      <li><strong>Primitives:</strong> reduced-form profit function π(s), fixed cost distribution, entry cost distribution.</li>
      <li><strong>State:</strong> s=(n,z). z follows Markov; n evolves via entry/exit.</li>
      <li><strong>Estimation logic:</strong> (i) estimate profits; (ii) discretize states + transitions; (iii) infer cost parameters from observed entry/exit.</li>
      <li><strong>Counterfactual:</strong> lowering entry costs increases entry but can also raise exit and reduce incumbent value; net change in n is not “entry only”.</li>
    </ul>
  </details>
</div>


<div style="margin:16px 0; padding:14px 16px; border:1px solid rgba(0,0,0,.10); border-left:4px solid #0f3d2e; border-radius:10px; background:#fff;">
  <div style="font-weight:800;">Kilic &amp; Tuzel (2026) — Investing in Misallocation (Quick Notes)</div>
  <div style="opacity:.86; margin-top:4px;">Paper-reading note PDF</div>

  <p style="margin-top:10px;">
    <strong>File:</strong>
    <a href="{{ site.baseurl }}/reading/library/Kilic_Tuzel_JFE_2026_StudyNotes.pdf">Kilic_Tuzel_JFE_2026_StudyNotes.pdf</a>
  </p>

  <p style="opacity:.90; margin-top:6px;">
    This file summarizes the paper’s core mechanism and provides a structured walkthrough of its reduced-form regressions, structural model equations, and detailed interpretations of every table and figure.
  </p>
</div>


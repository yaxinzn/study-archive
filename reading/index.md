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
  --reading-green-dark:#0a2d22;
  --reading-green-soft:rgba(15,61,46,.06);
  --reading-green-softer:rgba(15,61,46,.035);
  --reading-border:rgba(0,0,0,.10);
  --reading-border-strong:rgba(0,0,0,.16);
  --reading-text:#111827;
  --reading-muted:rgba(17,24,39,.64);
  --reading-bg:#fff;
  --reading-panel:#fbfcfb;
  --reading-shadow:0 14px 34px rgba(0,0,0,.08);
  --reading-radius:14px;
}

html{
  scroll-behavior:smooth;
}
body{
  background:
    radial-gradient(circle at 18% 0%, rgba(15,61,46,.055), transparent 34%),
    linear-gradient(180deg, #fbfcfb 0%, #fff 260px);
}
.reading-page{
  max-width:1180px;
  margin:0 auto;
}
.reading-page *{
  box-sizing:border-box;
}

.reading-library-view[hidden],
.reading-study-view[hidden],
.reading-active-filters[hidden],
.reading-game-answer[hidden],
.reading-game-result[hidden],
.reading-game-control[hidden]{
  display:none !important;
}

.reading-hero,
.reading-panel,
.reading-picker,
.reading-side,
.reading-entry,
.reading-study-hero,
.reading-game-setup,
.reading-game-panel,
.reading-game-card,
.reading-game-result{
  border:1px solid var(--reading-border);
  border-radius:var(--reading-radius);
  background:var(--reading-bg);
}

.reading-primary-btn,
.reading-secondary-btn,
.reading-soft-btn,
.reading-random-row button,
.reading-filter-chip,
.reading-letter-btn,
.reading-game-control,
.reading-game-option{
  border:1px solid var(--reading-border-strong);
  border-radius:10px;
  background:#fff;
  color:var(--reading-text);
  cursor:pointer;
  font-weight:760;
  text-decoration:none;
}

.reading-primary-btn,
.reading-secondary-btn,
.reading-soft-btn{
  display:inline-flex;
  align-items:center;
  justify-content:center;
  min-height:40px;
  padding:9px 12px;
  white-space:nowrap;
}
.reading-primary-btn{
  border-color:var(--reading-green);
  background:var(--reading-green);
  color:#fff !important;
}
.reading-soft-btn{
  border-color:transparent;
  background:var(--reading-green-soft);
  color:var(--reading-green);
}
.reading-primary-btn:hover,
.reading-secondary-btn:hover,
.reading-soft-btn:hover,
.reading-random-row button:hover:not(:disabled),
.reading-filter-chip:hover,
.reading-letter-btn:hover:not(:disabled),
.reading-game-control:hover:not(:disabled),
.reading-game-option:hover:not(:disabled){
  transform:translateY(-1px);
}

/* Dashboard stats and utility toolbar */
.reading-stats{
  display:grid;
  grid-template-columns:repeat(4, minmax(0,1fr));
  gap:10px;
  margin:0 0 16px 0;
}
.reading-stat-card{
  border:1px solid var(--reading-border);
  border-radius:13px;
  background:rgba(255,255,255,.86);
  padding:12px 13px;
  box-shadow:0 8px 22px rgba(0,0,0,.035);
}
.reading-stat-label{
  color:var(--reading-muted);
  font-size:11px;
  font-weight:850;
  letter-spacing:.055em;
  text-transform:uppercase;
}
.reading-stat-value{
  margin-top:4px;
  color:var(--reading-text);
  font-size:20px;
  font-weight:920;
  line-height:1.1;
}
.reading-stat-sub{
  margin-top:3px;
  color:var(--reading-muted);
  font-size:12px;
  line-height:1.3;
}
.reading-library-toolbar{
  position:sticky;
  top:0;
  z-index:20;
  display:flex;
  gap:10px;
  align-items:center;
  justify-content:space-between;
  margin:0 0 14px 0;
  padding:10px;
  border:1px solid var(--reading-border);
  border-radius:14px;
  background:rgba(255,255,255,.92);
  backdrop-filter:blur(12px);
  box-shadow:0 10px 30px rgba(0,0,0,.055);
}
.reading-toolbar-left,
.reading-toolbar-right{
  display:flex;
  align-items:center;
  gap:8px;
  min-width:0;
  flex-wrap:wrap;
}
.reading-toolbar-label{
  color:var(--reading-muted);
  font-size:12px;
  font-weight:850;
}
.reading-sort-select{
  min-height:36px;
  max-width:210px;
  padding:7px 34px 7px 10px;
  border:1px solid rgba(0,0,0,.16);
  border-radius:10px;
  background:#fff;
  color:var(--reading-text);
  font-weight:720;
}
.reading-toolbar-btn{
  min-height:36px;
  padding:7px 10px;
  border:1px solid var(--reading-border-strong);
  border-radius:10px;
  background:#fff;
  color:var(--reading-text);
  cursor:pointer;
  font-size:13px;
  font-weight:780;
}
.reading-toolbar-btn:hover{
  transform:translateY(-1px);
}
.reading-toolbar-btn.is-active{
  border-color:var(--reading-green);
  background:var(--reading-green-soft);
  color:var(--reading-green);
}
.reading-page.is-compact .reading-entry{
  margin:8px 0;
  padding:10px 12px;
}
.reading-page.is-compact .reading-title{
  font-size:14px;
}
.reading-page.is-compact .reading-author,
.reading-page.is-compact .reading-file{
  margin-top:5px;
  font-size:13px;
}
.reading-page.is-compact .reading-note{
  margin-top:6px;
}

/* Hero */
.reading-hero{
  display:flex;
  gap:18px;
  justify-content:space-between;
  align-items:center;
  margin:18px 0 14px 0;
  padding:20px 22px;
  border-left:5px solid var(--reading-green);
  background:
    linear-gradient(135deg, rgba(15,61,46,.065), rgba(255,255,255,.96) 42%),
    #fff;
  box-shadow:0 14px 34px rgba(0,0,0,.055);
}
.reading-hero-title{
  margin:0;
  color:var(--reading-text);
  font-size:24px;
  font-weight:950;
  line-height:1.18;
  letter-spacing:-.015em;
}
.reading-hero-copy{
  margin:6px 0 0 0;
  max-width:760px;
  color:var(--reading-muted);
  line-height:1.55;
}
.reading-hero-actions{
  display:flex;
  flex:0 0 auto;
  gap:8px;
  flex-wrap:wrap;
  justify-content:flex-end;
}

/* Filters */
.reading-panel{
  margin:0 0 18px 0;
  padding:16px;
  background:rgba(255,255,255,.94);
  box-shadow:0 10px 28px rgba(0,0,0,.04);
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
  max-width:780px;
  color:var(--reading-muted);
  font-size:13px;
  line-height:1.45;
}
.reading-filter-stack{
  display:grid;
  gap:10px;
}
.reading-filter-row-main{
  display:grid;
  grid-template-columns:minmax(0,1fr);
  gap:10px;
}
.reading-filter-row-small{
  display:grid;
  grid-template-columns:minmax(145px,.9fr) minmax(170px,1fr) minmax(120px,.7fr);
  gap:10px;
  max-width:640px;
  align-items:end;
}
.reading-field{
  display:block;
  min-width:0;
}
.reading-field span,
.reading-field-label,
.reading-game-label{
  display:block;
  margin:0 0 5px 0;
  color:rgba(17,24,39,.78);
  font-size:12px;
  font-weight:850;
  letter-spacing:.01em;
}
.reading-field input,
.reading-journal-summary,
.reading-game-select{
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
.reading-journal-select:focus-within .reading-journal-summary,
.reading-game-select:focus{
  outline:2px solid rgba(15,61,46,.15);
  border-color:rgba(15,61,46,.48);
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

/* Initial picker and active filters */
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
  grid-template-columns:minmax(0,1fr) 320px;
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
  padding:15px 17px;
  border-left:4px solid var(--reading-green);
  box-shadow:0 10px 24px rgba(0,0,0,.035);
  transition:transform .12s ease, box-shadow .12s ease, border-color .12s ease;
}
.reading-entry:hover{
  transform:translateY(-1px);
  box-shadow:0 14px 32px rgba(0,0,0,.065);
  border-left-color:var(--reading-green-dark);
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
  font-weight:900;
  line-height:1.35;
  font-size:15.5px;
  letter-spacing:-.01em;
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
  display:inline-flex;
  align-items:center;
  max-width:100%;
  padding:2px 7px;
  border-radius:8px;
  background:rgba(37,99,235,.06);
  overflow-wrap:anywhere;
  text-decoration:none;
  font-weight:720;
}
.reading-file a:hover{
  background:rgba(37,99,235,.11);
  text-decoration:underline;
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
  padding:16px;
  background:rgba(255,255,255,.94);
  box-shadow:0 10px 28px rgba(0,0,0,.04);
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

/* Study games */
.reading-study-view{
  max-width:900px;
  margin:0 auto;
}
.reading-study-hero{
  display:flex;
  gap:16px;
  justify-content:space-between;
  align-items:flex-start;
  margin:16px 0 16px 0;
  padding:16px 18px;
  border-left:4px solid var(--reading-green);
}
.reading-study-title{
  margin:0;
  color:var(--reading-text);
  font-size:22px;
  font-weight:900;
  line-height:1.22;
}
.reading-study-copy{
  margin:6px 0 0 0;
  max-width:680px;
  color:var(--reading-muted);
  line-height:1.55;
}
.reading-game-setup{
  padding:15px;
  margin:0 0 14px 0;
}
.reading-game-setup-grid{
  display:grid;
  grid-template-columns:minmax(0,1fr) 170px 130px auto;
  gap:10px;
  align-items:end;
}
.reading-game-deck-status{
  min-height:40px;
  padding:10px 12px;
  border:1px solid rgba(0,0,0,.08);
  border-radius:10px;
  background:var(--reading-green-softer);
  color:var(--reading-muted);
  font-size:13px;
  line-height:1.4;
}
.reading-game-mode-note{
  margin:10px 0 0 0;
  color:var(--reading-muted);
  font-size:13px;
  line-height:1.45;
}
.reading-game-panel{
  padding:15px;
}
.reading-game-status-row{
  display:grid;
  grid-template-columns:minmax(0,1fr) 150px;
  gap:12px;
  align-items:center;
  margin-bottom:12px;
}
.reading-game-progress-shell{
  height:8px;
  overflow:hidden;
  border-radius:999px;
  background:rgba(0,0,0,.07);
}
.reading-game-progress-fill{
  width:0%;
  height:100%;
  background:var(--reading-green);
  transition:width .18s ease;
}
.reading-game-score{
  color:var(--reading-muted);
  font-size:13px;
  font-weight:760;
  text-align:right;
}
.reading-game-card{
  min-height:235px;
  padding:18px;
  background:linear-gradient(180deg, #fff 0%, rgba(15,61,46,.025) 100%);
}
.reading-game-prompt{
  color:var(--reading-green);
  font-size:12px;
  font-weight:900;
  letter-spacing:.02em;
  text-transform:uppercase;
}
.reading-game-question{
  margin:10px 0 0 0;
  color:var(--reading-text);
  font-size:20px;
  font-weight:880;
  line-height:1.42;
}
.reading-game-question.is-note{
  font-size:16px;
  font-weight:650;
  color:rgba(17,24,39,.86);
}
.reading-game-options{
  display:grid;
  grid-template-columns:1fr 1fr;
  gap:9px;
  margin-top:16px;
}
.reading-game-option{
  min-height:46px;
  padding:10px 12px;
  text-align:left;
  line-height:1.35;
  overflow-wrap:anywhere;
}
.reading-game-option.is-correct{
  border-color:var(--reading-green);
  background:var(--reading-green-soft);
  color:var(--reading-green);
}
.reading-game-option.is-wrong{
  border-color:rgba(180,0,0,.28);
  background:rgba(180,0,0,.055);
  color:#7f1d1d;
}
.reading-game-option:disabled,
.reading-game-control:disabled{
  cursor:default;
  opacity:.50;
  transform:none;
}
.reading-game-answer{
  margin-top:16px;
  padding:12px;
  border:1px solid rgba(0,0,0,.08);
  border-radius:12px;
  background:#fff;
}
.reading-game-answer-title{
  margin:0 0 8px 0;
  color:var(--reading-text);
  font-size:14px;
  font-weight:900;
}
.reading-game-answer-row{
  display:grid;
  grid-template-columns:94px minmax(0,1fr);
  gap:8px;
  margin:6px 0;
  color:rgba(17,24,39,.82);
  font-size:13px;
  line-height:1.4;
}
.reading-game-answer-row strong{
  color:rgba(17,24,39,.66);
}
.reading-game-answer-row a{
  overflow-wrap:anywhere;
}
.reading-game-answer-row.is-long{
  grid-template-columns:1fr;
  gap:3px;
  margin-top:9px;
}
.reading-game-answer-row.is-long span{
  display:block;
  padding:9px 10px;
  border:1px solid rgba(0,0,0,.06);
  border-radius:10px;
  background:rgba(15,61,46,.025);
  line-height:1.58;
}
.reading-game-controls{
  display:flex;
  flex-wrap:wrap;
  gap:8px;
  margin-top:14px;
}
.reading-game-control{
  min-height:38px;
  padding:8px 11px;
  font-size:13px;
}
.reading-game-control.is-primary{
  border-color:var(--reading-green);
  background:var(--reading-green);
  color:#fff;
}
.reading-game-feedback{
  min-height:22px;
  margin-top:10px;
  color:var(--reading-muted);
  font-size:13px;
  line-height:1.45;
}
.reading-game-feedback.is-good{
  color:var(--reading-green);
  font-weight:760;
}
.reading-game-feedback.is-bad{
  color:#7f1d1d;
  font-weight:760;
}
.reading-game-result{
  margin-top:14px;
  padding:13px;
  background:var(--reading-green-softer);
}
.reading-game-result-title{
  margin:0 0 6px 0;
  color:var(--reading-text);
  font-weight:900;
}
.reading-game-result-copy{
  margin:4px 0 0 0;
  color:var(--reading-muted);
  font-size:13px;
  line-height:1.45;
}
.reading-game-missed-list{
  margin:8px 0 0 20px;
}
.reading-game-missed-list li{
  margin:5px 0;
}

@media (max-width:980px){
  .reading-content-grid{
    grid-template-columns:1fr;
  }
  .reading-stats{
    grid-template-columns:repeat(2, minmax(0,1fr));
  }
  .reading-library-toolbar{
    position:static;
  }
  .reading-side{
    position:static;
    max-height:none;
  }
  .reading-game-setup-grid{
    grid-template-columns:1fr 1fr;
  }
}
@media (max-width:720px){
  .reading-stats{
    grid-template-columns:1fr;
  }
  .reading-library-toolbar,
  .reading-toolbar-left,
  .reading-toolbar-right{
    display:block;
  }
  .reading-toolbar-right{
    margin-top:8px;
  }
  .reading-toolbar-btn,
  .reading-sort-select{
    width:100%;
    margin-top:6px;
  }
  .reading-hero,
  .reading-panel-head,
  .reading-entry-top,
  .reading-picker summary,
  .reading-study-hero,
  .reading-game-status-row{
    display:block;
  }
  .reading-hero-actions{
    justify-content:flex-start;
    margin-top:10px;
  }
  .reading-secondary-btn{
    margin-top:10px;
  }
  .reading-filter-row-small,
  .reading-game-setup-grid,
  .reading-game-options{
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
  .reading-game-score{
    margin-top:8px;
    text-align:left;
  }
  .reading-game-question{
    font-size:18px;
  }
  .reading-game-answer-row{
    grid-template-columns:1fr;
    gap:2px;
  }
}
</style>

<div class="reading-page" id="readingPage">
  {% assign items = site.data.reading %}

  <div class="reading-library-view" id="readingLibraryView">
    <section class="reading-hero">
      <div>
        <h1 class="reading-hero-title">Paper Reading &amp; Quick Notes</h1>
        <p class="reading-hero-copy">Search the library, narrow by journal/year/author initials, open PDFs quickly, and turn the current results into a practice deck.</p>
      </div>
      <div class="reading-hero-actions">
        <a class="reading-soft-btn" href="#readingFilters">Find papers</a>
        <a class="reading-primary-btn" id="readingOpenGames" href="#study-games">Practice papers</a>
      </div>
    </section>

    <section class="reading-stats" aria-label="Reading library statistics">
      <div class="reading-stat-card">
        <div class="reading-stat-label">Library</div>
        <div class="reading-stat-value" id="readingStatTotal">—</div>
        <div class="reading-stat-sub">total papers</div>
      </div>
      <div class="reading-stat-card">
        <div class="reading-stat-label">Current view</div>
        <div class="reading-stat-value" id="readingStatShown">—</div>
        <div class="reading-stat-sub">matching results</div>
      </div>
      <div class="reading-stat-card">
        <div class="reading-stat-label">Journals</div>
        <div class="reading-stat-value" id="readingStatJournals">—</div>
        <div class="reading-stat-sub">detected codes</div>
      </div>
      <div class="reading-stat-card">
        <div class="reading-stat-label">Years</div>
        <div class="reading-stat-value" id="readingStatYears">—</div>
        <div class="reading-stat-sub">publication range</div>
      </div>
    </section>

    <section class="reading-panel" id="readingFilters" aria-label="Paper search and filters">
      <div class="reading-panel-head">
        <div>
          <h2 class="reading-panel-title">Find papers</h2>
          <p class="reading-panel-note">Use search for broad keywords; use initials, year, and journal for precise review sets. The practice mode uses exactly the filtered results.</p>
        </div>
        <button id="readingResetFilters" class="reading-secondary-btn" type="button">Clear all</button>
      </div>

      <div class="reading-filter-stack">
        <div class="reading-filter-row-main">
          <label class="reading-field reading-field-search" for="readingQuery">
            <span>Search</span>
            <input id="readingQuery" type="search" placeholder="Author / title / keyword / PDF file…" autocomplete="off">
          </label>
        </div>

        <div class="reading-filter-row-small">
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

        <div class="reading-library-toolbar" aria-label="Library controls">
          <div class="reading-toolbar-left">
            <span class="reading-toolbar-label">Sort</span>
            <select class="reading-sort-select" id="readingSortSelect" aria-label="Sort papers">
              <option value="title">Title A–Z</option>
              <option value="year_desc">Year newest</option>
              <option value="year_asc">Year oldest</option>
              <option value="journal">Journal</option>
              <option value="file">PDF name</option>
            </select>
          </div>
          <div class="reading-toolbar-right">
            <button class="reading-toolbar-btn" id="readingCompactToggle" type="button" aria-pressed="false">Compact cards</button>
            <button class="reading-toolbar-btn" id="readingCopyVisibleBtn" type="button">Copy current PDF names</button>
          </div>
        </div>

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
                 data-file="{{ p.file | escape }}"
                 data-desc="{{ p.desc | strip_html | escape }}">
              <div class="reading-entry-top">
                <div>
                  <div class="reading-title">{{ p.title }}</div>
                  {% if paper_authors and paper_authors != "" %}
                    <p class="reading-author"><strong>Author:</strong> {{ paper_authors }}</p>
                  {% endif %}
                  <p class="reading-file">
                    <strong>File:</strong>
                    <a href="{% include pdf_href.html pdf=p.file %}">{% include pdf_label.html pdf=p.file %}</a>
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

  <section class="reading-study-view" id="readingStudyView" aria-label="Paper practice games" hidden>
    <div class="reading-study-hero">
      <div>
        <h2 class="reading-study-title">Paper Practice</h2>
        <p class="reading-study-copy">A simple study mode for memorizing titles, PDFs, journals, years, and quick notes. It uses the current filtered results as the deck.</p>
      </div>
      <a class="reading-secondary-btn" id="readingBackToLibrary" href="#library">Back to library</a>
    </div>

    <div class="reading-game-setup">
      <div class="reading-game-setup-grid">
        <div class="reading-game-deck-status" id="readingGameDeckStatus">Deck loading…</div>

        <label for="readingGameMode">
          <span class="reading-game-label">Mode</span>
          <select class="reading-game-select" id="readingGameMode">
            <option value="flashcard">Flashcards</option>
            <option value="title_pdf">Title → PDF</option>
            <option value="note_title">Note → Paper</option>
            <option value="journal_year">Journal &amp; Year</option>
          </select>
        </label>

        <label for="readingGameRoundCount">
          <span class="reading-game-label">Rounds</span>
          <select class="reading-game-select" id="readingGameRoundCount">
            <option value="10">10</option>
            <option value="15">15</option>
            <option value="25">25</option>
            <option value="all">All</option>
          </select>
        </label>

        <button class="reading-primary-btn" id="readingGameStart" type="button">Start</button>
      </div>
      <p class="reading-game-mode-note" id="readingGameModeNote">Flashcards show the paper topic first, then reveal the full title, PDF, journal, year, authors, and full summary.</p>
    </div>

    <div class="reading-game-panel">
      <div class="reading-game-status-row">
        <div class="reading-game-progress-shell" aria-hidden="true">
          <div class="reading-game-progress-fill" id="readingGameProgress"></div>
        </div>
        <div class="reading-game-score" id="readingGameScore">Not started</div>
      </div>

      <div class="reading-game-card" id="readingGameCard">
        <div class="reading-game-prompt" id="readingGamePrompt">Choose a mode and start</div>
        <div class="reading-game-question" id="readingGameQuestion">Use filters first if you want to practice a smaller set of papers.</div>
        <div class="reading-game-options" id="readingGameOptions"></div>

        <div class="reading-game-answer" id="readingGameAnswer" hidden>
          <div class="reading-game-answer-title">Answer &amp; summary</div>
          <div id="readingGameAnswerRows"></div>
        </div>

        <div class="reading-game-controls">
          <button class="reading-game-control is-primary" id="readingGameReveal" type="button" disabled>Reveal</button>
          <button class="reading-game-control" id="readingGameKnow" type="button" hidden>I knew it</button>
          <button class="reading-game-control" id="readingGameMiss" type="button" hidden>Review again</button>
          <button class="reading-game-control is-primary" id="readingGameNext" type="button" hidden>Next</button>
          <button class="reading-game-control" id="readingGameRestart" type="button" disabled>Restart</button>
        </div>

        <div class="reading-game-feedback" id="readingGameFeedback" aria-live="polite"></div>
      </div>

      <div class="reading-game-result" id="readingGameResult" hidden>
        <div class="reading-game-result-title" id="readingGameResultTitle">Session complete</div>
        <p class="reading-game-result-copy" id="readingGameResultCopy"></p>
        <div class="reading-random-row">
          <button id="readingGameCopyMissed" type="button">Copy missed PDFs</button>
        </div>
        <ol class="reading-game-missed-list" id="readingGameMissedList"></ol>
      </div>
    </div>
  </section>
</div>

<script>
(function(){
  const libraryView = document.getElementById('readingLibraryView');
  const studyView = document.getElementById('readingStudyView');
  const openGamesBtn = document.getElementById('readingOpenGames');
  const backToLibraryBtn = document.getElementById('readingBackToLibrary');

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

  const statTotal = document.getElementById('readingStatTotal');
  const statShown = document.getElementById('readingStatShown');
  const statJournals = document.getElementById('readingStatJournals');
  const statYears = document.getElementById('readingStatYears');
  const sortSelect = document.getElementById('readingSortSelect');
  const compactToggle = document.getElementById('readingCompactToggle');
  const copyVisibleBtn = document.getElementById('readingCopyVisibleBtn');

  const gameDeckStatus = document.getElementById('readingGameDeckStatus');
  const gameModeSelect = document.getElementById('readingGameMode');
  const gameRoundCount = document.getElementById('readingGameRoundCount');
  const gameStartBtn = document.getElementById('readingGameStart');
  const gameModeNote = document.getElementById('readingGameModeNote');
  const gameProgress = document.getElementById('readingGameProgress');
  const gameScore = document.getElementById('readingGameScore');
  const gamePrompt = document.getElementById('readingGamePrompt');
  const gameQuestion = document.getElementById('readingGameQuestion');
  const gameOptions = document.getElementById('readingGameOptions');
  const gameAnswer = document.getElementById('readingGameAnswer');
  const gameAnswerRows = document.getElementById('readingGameAnswerRows');
  const gameRevealBtn = document.getElementById('readingGameReveal');
  const gameKnowBtn = document.getElementById('readingGameKnow');
  const gameMissBtn = document.getElementById('readingGameMiss');
  const gameNextBtn = document.getElementById('readingGameNext');
  const gameRestartBtn = document.getElementById('readingGameRestart');
  const gameFeedback = document.getElementById('readingGameFeedback');
  const gameResult = document.getElementById('readingGameResult');
  const gameResultTitle = document.getElementById('readingGameResultTitle');
  const gameResultCopy = document.getElementById('readingGameResultCopy');
  const gameMissedList = document.getElementById('readingGameMissedList');
  const gameCopyMissedBtn = document.getElementById('readingGameCopyMissed');

  if (!input) return;

  const alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.split('');
  const maxGuideItems = 45;

  const gameModeText = {
    flashcard: 'Flashcards show only the paper topic first; the full title, PDF, journal, year, authors, and full summary appear after reveal.',
    title_pdf: 'Title → PDF shows the paper topic only, then asks users to identify the correct PDF file.',
    note_title: 'Note → Paper shows a quick-note excerpt and uses short paper topics as choices.',
    journal_year: 'Journal & Year shows the paper topic only, then asks users to recall the journal code and publication year.'
  };

  let selectedPDFs = [];
  let selectedDate = '';
  let selectedFilterSummary = '';
  let compactMode = false;
  let selectedInitials = new Set();
  let selectedJournals = new Set();
  let letterButtons = [];
  let journalCheckboxes = [];
  let lastVisibleItems = [];

  let gameQueue = [];
  let gameIndex = 0;
  let gameCorrect = 0;
  let gameMissed = [];
  let gameCurrent = null;
  let gameAnswered = false;

  function fmtCount(value){
    return Number(value || 0).toLocaleString('en-US');
  }

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


  function pdfLabelFromValue(value){
    let raw = (value || '').toString().trim();
    if (!raw) return '';

    const noQuery = raw.split('?')[0].split('#')[0];
    const lastPart = noQuery.split('/').filter(Boolean).pop() || raw;

    let decoded = lastPart;
    try {
      decoded = decodeURIComponent(lastPart);
    } catch (err) {
      decoded = lastPart;
    }

    return decoded
      .replace(/\.pdf$/i, '')
      .replace(/\s+/g, ' ')
      .trim();
  }

  function uniqueSorted(values){
    return Array.from(new Set(values.filter(Boolean))).sort((a, b) => a.localeCompare(b));
  }

  function excerpt(text, maxLength){
    const value = (text || '').replace(/\s+/g, ' ').trim();
    if (value.length <= maxLength) return value;
    return value.slice(0, Math.max(0, maxLength - 1)).trim() + '…';
  }

  function practiceTitle(title){
    const value = (title || '').replace(/\s+/g, ' ').trim();
    if (!value) return '';

    function tidyTopic(topic){
      return (topic || '')
        .replace(/^\s*[-–—:;|]+\s*/, '')
        .replace(/\s+/g, ' ')
        .trim();
    }

    // Standard format: Authors (JOURNAL, YEAR) - Paper Topic
    // Also handles missing separators: Authors (JOURNAL, YEAR) Paper Topic
    const afterJournalYear = value.match(/\([^)]*(?:19|20)\d{2}[^)]*\)\s*(?:[-–—:;|]\s*)?(.+)$/);
    if (afterJournalYear && tidyTopic(afterJournalYear[1])) return tidyTopic(afterJournalYear[1]);

    // Fallback for entries that use a parenthetical marker without a year
    // but still include a separator, for example: Authors (JOURNAL) - Topic.
    const afterParenthesis = value.match(/\([^)]*\)\s*[-–—:;|]\s*(.+)$/);
    if (afterParenthesis && tidyTopic(afterParenthesis[1])) return tidyTopic(afterParenthesis[1]);

    // Final fallback: remove the author prefix before a spaced dash.
    const dashParts = value.split(/\s+[-–—]\s+/);
    if (dashParts.length > 1) return tidyTopic(dashParts.slice(1).join(' - '));

    return value;
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
    const descNode = el.querySelector('.reading-desc');
    const author = (el.getAttribute('data-author') || '').trim();
    const title = (el.getAttribute('data-title') || (titleNode ? titleNode.textContent : '') || '').trim();

    // rawFile may be a Dropbox URL after migration.
    // linkLabel is the visible short label rendered by pdf_label.html.
    // item.file is intentionally kept as the short display name so that
    // Matching PDFs, Pick PDFs, Copy names, Download names, and Paper Practice
    // all show Bernanke_Gertler_AER_1989 instead of the long Dropbox URL.
    const rawFile = (el.getAttribute('data-file') || '').trim();
    const linkLabel = (link ? link.textContent : '').trim();
    const file = pdfLabelFromValue(linkLabel || rawFile);
    const fileRaw = rawFile || file;

    const desc = (el.getAttribute('data-desc') || (descNode ? descNode.textContent : '') || '').trim();
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
      fileRaw,
      meta.journal,
      meta.year,
      desc,
      el.textContent
    ].join(' ');

    return {
      el,
      author,
      authorDisplay,
      title,
      shortTitle: practiceTitle(title),
      file,
      fileRaw,
      desc,
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

  function compareBySortMode(a, b){
    const mode = sortSelect ? sortSelect.value : 'title';

    if (mode === 'year_desc' || mode === 'year_asc') {
      const ay = Number(a.year || 0);
      const by = Number(b.year || 0);
      const diff = mode === 'year_desc' ? by - ay : ay - by;
      if (diff !== 0) return diff;
      return a.sortKey.localeCompare(b.sortKey);
    }

    if (mode === 'journal') {
      return `${a.journal || 'ZZZ'} ${a.year || ''} ${a.sortKey}`.localeCompare(`${b.journal || 'ZZZ'} ${b.year || ''} ${b.sortKey}`);
    }

    if (mode === 'file') {
      return norm(a.file).localeCompare(norm(b.file));
    }

    return a.sortKey.localeCompare(b.sortKey);
  }

  function getFilteredItems(){
    const filters = getFilters();
    return paperData
      .filter(item => itemMatches(item, filters))
      .sort(compareBySortMode);
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

  function updateStats(visibleItems){
    if (statTotal) statTotal.textContent = fmtCount(paperData.length);
    if (statShown) statShown.textContent = fmtCount(visibleItems.length);

    if (statJournals) {
      statJournals.textContent = fmtCount(uniqueSorted(paperData.map(item => item.journal)).length);
    }

    if (statYears) {
      const years = paperData
        .map(item => Number(item.year))
        .filter(year => Number.isFinite(year) && year > 0);

      if (years.length) {
        const minYear = Math.min.apply(null, years);
        const maxYear = Math.max.apply(null, years);
        statYears.textContent = minYear === maxYear ? String(maxYear) : `${minYear}–${maxYear}`;
      } else {
        statYears.textContent = '—';
      }
    }
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
    const visibleItems = getFilteredItems();
    const visibleSet = new Set(visibleItems);

    lastVisibleItems = visibleItems;
    updateStats(visibleItems);

    for (const el of entries) {
      const item = dataByElement.get(el);

      if (!item) {
        el.hidden = paperData.length !== 0;
        continue;
      }

      el.hidden = !visibleSet.has(item);
    }

    if (count) {
      const base = `${fmtCount(visibleItems.length)} / ${fmtCount(paperData.length)} papers shown`;
      count.textContent = hasActiveFilters(filters) ? `${base} · ${readableFilterSummary(filters)}` : base;
    }

    if (empty) {
      empty.style.display = visibleItems.length === 0 ? 'block' : 'none';
    }

    renderGuide(visibleItems, filters);
    updateLetterButtons(filters);
    updateJournalOptions(filters);
    renderActiveFilters(filters);
    refreshGameDeckStatus();
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

  async function copyText(text){
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
  }

  async function copyVisiblePDFNames(){
    const items = lastVisibleItems.length ? lastVisibleItems : getFilteredItems();

    if (!items.length) {
      if (randomStatus) randomStatus.textContent = 'No current PDF names to copy.';
      return;
    }

    const text = items.map((item, index) => `${index + 1}. ${item.file}`).join('\n');
    await copyText(text);

    if (randomStatus) {
      randomStatus.textContent = `Copied ${items.length} current PDF name${items.length === 1 ? '' : 's'} to clipboard.`;
    }
  }

  async function copySelectedNames(showStatus = true){
    if (!selectedPDFs.length) return false;

    await copyText(formatSelectedNames());

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

  function getCurrentDeckForMode(mode){
    const filters = getFilters();
    let deck = getFilteredItems();

    if (mode === 'note_title') {
      deck = deck.filter(item => item.desc && norm(item.desc).length >= 40);
    }

    if (mode === 'journal_year') {
      deck = deck.filter(item => item.journal || item.year);
    }

    return { deck, filters };
  }

  function refreshGameDeckStatus(){
    if (!gameDeckStatus || !gameModeSelect) return;

    const mode = gameModeSelect.value;
    const result = getCurrentDeckForMode(mode);
    const filterText = readableFilterSummary(result.filters);
    const label = result.deck.length === 1 ? 'paper' : 'papers';

    gameDeckStatus.textContent = `${fmtCount(result.deck.length)} ${label} in practice deck · ${filterText}`;
    if (gameStartBtn) gameStartBtn.disabled = result.deck.length === 0;
  }

  function setGameModeNote(){
    if (!gameModeNote || !gameModeSelect) return;
    gameModeNote.textContent = gameModeText[gameModeSelect.value] || gameModeText.flashcard;
  }

  function openStudyView(event){
    if (event) event.preventDefault();

    if (libraryView) libraryView.hidden = true;
    if (studyView) studyView.hidden = false;
    if (window.location.hash !== '#study-games') {
      window.history.pushState(null, '', '#study-games');
    }

    refreshGameDeckStatus();
    resetGameCard();
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }

  function showLibraryView(event){
    if (event) event.preventDefault();

    if (studyView) studyView.hidden = true;
    if (libraryView) libraryView.hidden = false;

    if (window.location.hash === '#study-games') {
      window.history.pushState(null, '', window.location.pathname + window.location.search + '#library');
    }

    setTimeout(() => {
      const target = document.getElementById('library');
      if (target) target.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }, 0);
  }

  function resetGameState(){
    gameQueue = [];
    gameIndex = 0;
    gameCorrect = 0;
    gameMissed = [];
    gameCurrent = null;
    gameAnswered = false;
  }

  function resetGameCard(){
    resetGameState();
    if (gameProgress) gameProgress.style.width = '0%';
    if (gameScore) gameScore.textContent = 'Not started';
    if (gamePrompt) gamePrompt.textContent = 'Choose a mode and start';
    if (gameQuestion) {
      gameQuestion.textContent = 'Use filters first if you want to practice a smaller set of papers.';
      gameQuestion.classList.remove('is-note');
    }
    if (gameOptions) gameOptions.innerHTML = '';
    if (gameAnswer) gameAnswer.hidden = true;
    if (gameAnswerRows) gameAnswerRows.innerHTML = '';
    if (gameFeedback) {
      gameFeedback.textContent = '';
      gameFeedback.className = 'reading-game-feedback';
    }
    if (gameRevealBtn) {
      gameRevealBtn.hidden = false;
      gameRevealBtn.disabled = true;
    }
    if (gameKnowBtn) gameKnowBtn.hidden = true;
    if (gameMissBtn) gameMissBtn.hidden = true;
    if (gameNextBtn) gameNextBtn.hidden = true;
    if (gameRestartBtn) gameRestartBtn.disabled = true;
    if (gameResult) gameResult.hidden = true;
  }

  function updateGameScore(){
    const total = gameQueue.length;
    const currentRound = Math.min(gameIndex + 1, total);
    const completed = gameAnswered ? currentRound : gameIndex;
    const percent = total ? Math.round((completed / total) * 100) : 0;

    if (gameProgress) gameProgress.style.width = `${percent}%`;
    if (gameScore) {
      gameScore.textContent = total
        ? `Round ${currentRound} / ${total} · ${gameCorrect} correct`
        : 'Not started';
    }
  }

  function gameTag(item){
    return [item.journal || 'Unknown journal', item.year || 'Unknown year'].join(' · ');
  }

  function displayPracticeTitle(item){
    return item.shortTitle || item.title || item.file;
  }

  function answerValue(item, mode){
    if (mode === 'title_pdf') return item.file;
    if (mode === 'note_title') return displayPracticeTitle(item);
    if (mode === 'journal_year') return gameTag(item);
    return displayPracticeTitle(item);
  }

  function makeOptions(correctItem, mode){
    const correctValue = answerValue(correctItem, mode);
    const seen = new Set([correctValue]);
    const candidates = shuffle(paperData)
      .filter(item => item !== correctItem)
      .map(item => answerValue(item, mode))
      .filter(value => {
        if (!value || seen.has(value)) return false;
        seen.add(value);
        return true;
      })
      .slice(0, 3);

    return shuffle([correctValue].concat(candidates));
  }

  function addAnswerRow(label, content, isLink, isLong){
    if (!gameAnswerRows || !content) return;

    const row = document.createElement('div');
    const strong = document.createElement('strong');
    const value = isLink ? document.createElement('a') : document.createElement('span');

    row.className = 'reading-game-answer-row';
    if (isLong) row.classList.add('is-long');
    strong.textContent = label;

    if (isLink) {
      value.textContent = content.text;
      value.href = content.href;
      value.target = '_blank';
      value.rel = 'noopener';
    } else {
      value.textContent = content;
    }

    row.appendChild(strong);
    row.appendChild(value);
    gameAnswerRows.appendChild(row);
  }

  function renderAnswer(item){
    if (!gameAnswer || !gameAnswerRows) return;

    gameAnswerRows.innerHTML = '';
    addAnswerRow('Practice title', displayPracticeTitle(item));
    addAnswerRow('Full title', item.title, false, true);
    addAnswerRow('PDF', { text: item.file, href: item.href }, true);
    addAnswerRow('Journal', item.journal || 'Unknown');
    addAnswerRow('Year', item.year || 'Unknown');
    if (item.authorDisplay) addAnswerRow('Authors', item.authorDisplay);
    if (item.desc) addAnswerRow('Summary', item.desc, false, true);

    gameAnswer.hidden = false;
  }

  function setFeedback(text, state){
    if (!gameFeedback) return;
    gameFeedback.textContent = text || '';
    gameFeedback.className = 'reading-game-feedback';
    if (state) gameFeedback.classList.add(state);
  }

  function markMissed(item){
    if (!item) return;
    if (!gameMissed.some(existing => existing.file === item.file)) {
      gameMissed.push(item);
    }
  }

  function finishMultipleChoice(isCorrect){
    if (!gameCurrent || gameAnswered) return;

    gameAnswered = true;
    if (isCorrect) {
      gameCorrect += 1;
      setFeedback('Correct.', 'is-good');
    } else {
      markMissed(gameCurrent);
      setFeedback('Review this one again.', 'is-bad');
    }

    renderAnswer(gameCurrent);
    if (gameNextBtn) gameNextBtn.hidden = false;
    if (gameRestartBtn) gameRestartBtn.disabled = false;
    updateGameScore();
  }

  function renderOptions(item, mode){
    if (!gameOptions) return;

    gameOptions.innerHTML = '';
    const correctValue = answerValue(item, mode);
    const options = makeOptions(item, mode);

    for (const value of options) {
      const btn = document.createElement('button');
      btn.type = 'button';
      btn.className = 'reading-game-option';
      btn.textContent = value;
      btn.addEventListener('click', () => {
        if (gameAnswered) return;

        const isCorrect = value === correctValue;
        btn.classList.add(isCorrect ? 'is-correct' : 'is-wrong');

        for (const optionBtn of gameOptions.querySelectorAll('.reading-game-option')) {
          optionBtn.disabled = true;
          if (optionBtn.textContent === correctValue) {
            optionBtn.classList.add('is-correct');
          }
        }

        finishMultipleChoice(isCorrect);
      });
      gameOptions.appendChild(btn);
    }
  }

  function renderRound(){
    if (gameIndex >= gameQueue.length) {
      finishGame();
      return;
    }

    const mode = gameModeSelect ? gameModeSelect.value : 'flashcard';
    const item = gameQueue[gameIndex];
    gameCurrent = item;
    gameAnswered = false;

    if (gameResult) gameResult.hidden = true;
    if (gameAnswer) gameAnswer.hidden = true;
    if (gameAnswerRows) gameAnswerRows.innerHTML = '';
    if (gameOptions) gameOptions.innerHTML = '';
    if (gameNextBtn) gameNextBtn.hidden = true;
    if (gameKnowBtn) gameKnowBtn.hidden = true;
    if (gameMissBtn) gameMissBtn.hidden = true;
    if (gameRevealBtn) {
      gameRevealBtn.hidden = mode !== 'flashcard';
      gameRevealBtn.disabled = mode !== 'flashcard';
    }
    if (gameRestartBtn) gameRestartBtn.disabled = false;
    setFeedback('', '');

    if (gameQuestion) gameQuestion.classList.remove('is-note');

    if (mode === 'flashcard') {
      if (gamePrompt) gamePrompt.textContent = 'Recall from the paper topic';
      if (gameQuestion) gameQuestion.textContent = displayPracticeTitle(item);
    } else if (mode === 'title_pdf') {
      if (gamePrompt) gamePrompt.textContent = 'Choose the correct PDF';
      if (gameQuestion) gameQuestion.textContent = displayPracticeTitle(item);
      renderOptions(item, mode);
    } else if (mode === 'note_title') {
      if (gamePrompt) gamePrompt.textContent = 'Which paper matches this note?';
      if (gameQuestion) {
        gameQuestion.textContent = excerpt(item.desc, 360);
        gameQuestion.classList.add('is-note');
      }
      renderOptions(item, mode);
    } else if (mode === 'journal_year') {
      if (gamePrompt) gamePrompt.textContent = 'Recall journal and year';
      if (gameQuestion) gameQuestion.textContent = displayPracticeTitle(item);
      renderOptions(item, mode);
    }

    updateGameScore();
  }

  function startGame(){
    const mode = gameModeSelect ? gameModeSelect.value : 'flashcard';
    const result = getCurrentDeckForMode(mode);
    let deck = result.deck;

    if (!deck.length) {
      resetGameCard();
      setFeedback('No papers are available for this mode under the current filters.', 'is-bad');
      refreshGameDeckStatus();
      return;
    }

    const roundValue = gameRoundCount ? gameRoundCount.value : '10';
    const roundLimit = roundValue === 'all' ? deck.length : Math.min(deck.length, Number(roundValue) || 10);

    resetGameState();
    gameQueue = shuffle(deck).slice(0, roundLimit);
    gameIndex = 0;
    gameCorrect = 0;
    gameMissed = [];

    if (gameResult) gameResult.hidden = true;
    renderRound();
  }

  function revealFlashcard(){
    if (!gameCurrent || gameAnswered) return;

    renderAnswer(gameCurrent);
    setFeedback('Mark whether you knew it without looking.', '');
    if (gameRevealBtn) gameRevealBtn.hidden = true;
    if (gameKnowBtn) gameKnowBtn.hidden = false;
    if (gameMissBtn) gameMissBtn.hidden = false;
  }

  function resolveFlashcard(knewIt){
    if (!gameCurrent || gameAnswered) return;

    gameAnswered = true;
    if (knewIt) {
      gameCorrect += 1;
      setFeedback('Marked as known.', 'is-good');
    } else {
      markMissed(gameCurrent);
      setFeedback('Added to review list.', 'is-bad');
    }

    if (gameKnowBtn) gameKnowBtn.hidden = true;
    if (gameMissBtn) gameMissBtn.hidden = true;
    if (gameNextBtn) gameNextBtn.hidden = false;
    updateGameScore();
  }

  function nextRound(){
    if (!gameQueue.length) return;

    gameIndex += 1;
    if (gameIndex >= gameQueue.length) {
      finishGame();
    } else {
      renderRound();
    }
  }

  function finishGame(){
    const total = gameQueue.length;
    const accuracy = total ? Math.round((gameCorrect / total) * 100) : 0;

    if (gameProgress) gameProgress.style.width = '100%';
    if (gameScore) gameScore.textContent = total ? `${gameCorrect} / ${total} correct` : 'Not started';
    if (gamePrompt) gamePrompt.textContent = 'Session complete';
    if (gameQuestion) {
      gameQuestion.textContent = total
        ? `Accuracy: ${accuracy}%. ${gameMissed.length ? 'Review the missed papers below.' : 'No missed papers in this round.'}`
        : 'Start a session to practice the library.';
      gameQuestion.classList.remove('is-note');
    }
    if (gameOptions) gameOptions.innerHTML = '';
    if (gameAnswer) gameAnswer.hidden = true;
    if (gameRevealBtn) gameRevealBtn.hidden = true;
    if (gameKnowBtn) gameKnowBtn.hidden = true;
    if (gameMissBtn) gameMissBtn.hidden = true;
    if (gameNextBtn) gameNextBtn.hidden = true;
    setFeedback('', '');
    renderGameResult(total, accuracy);
  }

  function renderGameResult(total, accuracy){
    if (!gameResult || !gameMissedList) return;

    gameResult.hidden = false;
    if (gameResultTitle) gameResultTitle.textContent = 'Session complete';
    if (gameResultCopy) {
      gameResultCopy.textContent = total
        ? `${gameCorrect} / ${total} correct (${accuracy}%). ${gameMissed.length} paper${gameMissed.length === 1 ? '' : 's'} marked for review.`
        : 'No session was started.';
    }

    gameMissedList.innerHTML = '';

    if (!gameMissed.length) {
      const li = document.createElement('li');
      li.textContent = 'No missed papers.';
      gameMissedList.appendChild(li);
      if (gameCopyMissedBtn) gameCopyMissedBtn.disabled = true;
      return;
    }

    if (gameCopyMissedBtn) gameCopyMissedBtn.disabled = false;

    for (const item of gameMissed) {
      const li = document.createElement('li');
      const a = document.createElement('a');
      a.textContent = item.file;
      a.href = item.href;
      a.target = '_blank';
      a.rel = 'noopener';
      li.appendChild(a);
      gameMissedList.appendChild(li);
    }
  }

  async function copyMissedPDFs(){
    if (!gameMissed.length) return;

    const text = gameMissed
      .map((item, index) => `${index + 1}. ${item.file}`)
      .join('\n');

    await copyText(text);
    setFeedback(`Copied ${gameMissed.length} missed PDF name${gameMissed.length === 1 ? '' : 's'} to clipboard.`, 'is-good');
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

  if (sortSelect) sortSelect.addEventListener('change', update);
  if (compactToggle) {
    compactToggle.addEventListener('click', () => {
      compactMode = !compactMode;
      const page = document.getElementById('readingPage');
      if (page) page.classList.toggle('is-compact', compactMode);
      compactToggle.classList.toggle('is-active', compactMode);
      compactToggle.setAttribute('aria-pressed', compactMode ? 'true' : 'false');
      compactToggle.textContent = compactMode ? 'Comfortable cards' : 'Compact cards';
    });
  }
  if (copyVisibleBtn) copyVisibleBtn.addEventListener('click', copyVisiblePDFNames);

  if (randomBtn) randomBtn.addEventListener('click', pickRandomPDFs);
  if (copyBtn) copyBtn.addEventListener('click', () => copySelectedNames(true));
  if (downloadNamesBtn) downloadNamesBtn.addEventListener('click', () => downloadSelectedNames(true));
  if (copyDownloadBtn) copyDownloadBtn.addEventListener('click', copyAndDownloadSelectedNames);

  if (openGamesBtn) openGamesBtn.addEventListener('click', openStudyView);
  if (backToLibraryBtn) backToLibraryBtn.addEventListener('click', showLibraryView);
  if (gameModeSelect) {
    gameModeSelect.addEventListener('change', () => {
      setGameModeNote();
      refreshGameDeckStatus();
      resetGameCard();
    });
  }
  if (gameStartBtn) gameStartBtn.addEventListener('click', startGame);
  if (gameRestartBtn) gameRestartBtn.addEventListener('click', startGame);
  if (gameRevealBtn) gameRevealBtn.addEventListener('click', revealFlashcard);
  if (gameKnowBtn) gameKnowBtn.addEventListener('click', () => resolveFlashcard(true));
  if (gameMissBtn) gameMissBtn.addEventListener('click', () => resolveFlashcard(false));
  if (gameNextBtn) gameNextBtn.addEventListener('click', nextRound);
  if (gameCopyMissedBtn) gameCopyMissedBtn.addEventListener('click', copyMissedPDFs);

  window.addEventListener('hashchange', () => {
    if (window.location.hash === '#study-games') {
      openStudyView();
    } else if (!studyView.hidden) {
      showLibraryView();
    }
  });

  hydrateCardMeta();
  buildLetterButtons();
  buildYearOptions();
  buildJournalOptions();
  setActionButtonsEnabled(false);
  setGameModeNote();
  resetGameCard();
  update();

  if (window.location.hash === '#study-games') {
    openStudyView();
  }
})();
</script>

---
title: Study Cycles
---

<style>
:root{
  --accent: #b08a2e; /* gold (close to Weebly) */
  --ink: #111827;
  --muted: rgba(17,24,39,.72);
  --nav: rgba(17,24,39,.40);
  --nav-active: rgba(17,24,39,.82);
  --max: 980px;
}

.sc-container{ max-width: var(--max); margin: 0 auto; padding: 0 18px; }

/* Top header (centered like Weebly) */
.sc-top{
  padding-top: 22px;
  padding-bottom: 10px;
  text-align: center;
}
.sc-name{
  font-family: Georgia, "Times New Roman", serif;
  font-size: 46px;
  margin: 0;
  letter-spacing: .01em;
}
.sc-name a{ text-decoration: none; color: #1f2a44; }
.sc-name .last{ color: var(--accent); }

.sc-nav{
  margin-top: 12px;
  display: flex;
  justify-content: center;
  gap: 26px;
  flex-wrap: wrap;
}
.sc-nav a{
  text-decoration: none;
  text-transform: uppercase;
  letter-spacing: .14em;
  font-size: 12px;
  color: var(--nav);
}
.sc-nav a:hover{ color: var(--nav-active); }
.sc-nav a.current{ color: var(--nav-active); font-weight: 700; }

/* Hero banner (Weebly-like: centered block, photo overlay) */
.sc-hero{
  margin: 18px auto 0;
  border-radius: 6px;
  overflow: hidden;
}
.sc-hero-inner{
  padding: 52px 18px 48px 18px;
  text-align: center;
  background-image:
    linear-gradient(135deg, rgba(0,0,0,.55), rgba(0,0,0,.35)),
    url("{{ site.baseurl }}/assets/studycycles-banner.jpg");
  background-size: cover;
  background-position: center;
}
.sc-hero h1{
  margin: 0;
  font-family: Georgia, "Times New Roman", serif;
  font-size: 58px;
  color: #fff;
}
.sc-hero h2{
  margin: 10px 0 0 0;
  font-family: Georgia, "Times New Roman", serif;
  font-size: 34px;
  color: var(--accent);
  font-weight: 700;
}
.sc-hero p{
  margin: 14px auto 0;
  max-width: 760px;
  color: rgba(255,255,255,.92);
  font-size: 16px;
  line-height: 1.6;
}

/* Buttons (subtle, Weebly-ish) */
.sc-btns{ margin-top: 18px; display: flex; justify-content: center; gap: 12px; flex-wrap: wrap; }
.sc-btn{
  display: inline-block;
  padding: 10px 14px;
  border-radius: 10px;
  text-decoration: none;
  font-weight: 650;
  border: 1px solid rgba(255,255,255,.24);
  background: rgba(255,255,255,.08);
  color: #fff;
}
.sc-btn:hover{ text-decoration:none; transform: translateY(-1px); }
.sc-btn.gold{
  border-color: rgba(176,138,46,.55);
  background: rgba(176,138,46,.18);
}

/* Body typography */
.sc-main{ padding: 34px 0 68px 0; }
.sc-main h2{
  font-family: Georgia, "Times New Roman", serif;
  font-size: 34px;
  margin: 30px 0 10px 0;
  color: #0f3d2e;
}
.sc-main p{ color: var(--muted); font-size: 16px; line-height: 1.78; }
.sc-main li{ color: var(--muted); line-height: 1.72; }
.sc-main a{ color: #1d4ed8; }
.sc-main a:hover{ text-decoration: underline; }
.sc-sep{ height: 1px; background: rgba(0,0,0,.08); margin: 34px 0; }
</style>

<div class="sc-container sc-top">
  <div class="sc-name">
    <a href="https://yaxinzn.weebly.com/">Yaxin <span class="last">Zheng</span></a>
  </div>

  <nav class="sc-nav" aria-label="Site">
    <a href="https://yaxinzn.weebly.com/">Home</a>
    <a href="https://yaxinzn.weebly.com/research-framework.html">Research Framework</a>
    <a href="https://yaxinzn.weebly.com/research-agenda.html">Research Agenda</a>
    <a class="current" href="{{ site.baseurl }}/">Study Cycles</a>
    <a href="https://yaxinzn.weebly.com/about.html">About</a>
    <a href="https://yaxinzn.weebly.com/contact.html">Contact</a>
  </nav>
</div>

<div class="sc-container sc-hero">
  <div class="sc-hero-inner">
    <h1>Study Cycles</h1>
    <h2>Weekly study loops across core fields</h2>
    <p>
      Weekly loops across micro, macro, econometrics, empirical IO, asset pricing, corporate finance, and macro-finance.
    </p>

    <div class="sc-btns">
      <a class="sc-btn gold" href="{{ site.baseurl }}/updates/">View Updates (NEWS)</a>
      <a class="sc-btn" href="https://github.com/yaxinzn/study-archive">View on GitHub</a>
    </div>
  </div>
</div>

<div class="sc-container sc-main" markdown="1">

## Method: the 7-day loop (Saturday = review)
I study in repeating seven-day cycles. Each week is a complete loop, and **Saturday is reserved for review**: consolidating notes, reconnecting ideas across topics, and updating reading maps. I then restart the cycle—refining summaries, re-deriving core results, and iterating until the foundations are internalized.

<div class="sc-sep"></div>

## Materials
- **[Micro](materials/micro/)** — preferences, uncertainty, general equilibrium, mechanisms  
- **[Macro](materials/macro/)** — growth, business cycles, monetary frameworks  
- **[Econometrics](materials/econometrics/)** — identification, estimation, inference, robustness  
- **[Math Foundations](materials/math-foundations/)** — linear algebra, probability, optimization, analysis  
- **[TFP Measurement](materials/tfp-measurement/)** — production functions, OP/LP/ACF, implementation  
- **[Empirical IO](materials/eio/)** — demand, costs, conduct, entry/exit, counterfactual analysis  
- **[Asset Pricing (Theory)](materials/ap-theory/)** — SDF, no-arbitrage, equilibrium pricing  
- **[Asset Pricing (Empirical)](materials/ap-empirical/)** — factors, predictability, anomalies, methods  
- **[Corporate Finance (Theory)](materials/cf-theory/)** — contracting, capital structure, governance  
- **[Corporate Finance (Empirical)](materials/cf-empirical/)** — causal designs, measurement, firm behavior  
- **[Macro-Finance](materials/macro-finance/)** — risk premia, term structure, policy transmission  

<div class="sc-sep"></div>

## Use these materials
If this study style—or any of the materials here—ends up being helpful, you’re very welcome to **reuse the notes** or **adapt the structure** in whatever way fits your learning goals.

</div>

---
title: Study Cycles
---

<style>
:root{
  --accent: #b08a2e;          /* gold */
  --ink: #111827;
  --muted: #4b5563;
  --max: 980px;
}

/* Layout */
.sc-wrap{ color: var(--ink); }
.sc-container{ max-width: var(--max); margin: 0 auto; padding: 0 18px; }

/* Top bar (matches main site vibe) */
.sc-topbar{
  padding-top: 18px;
  padding-bottom: 10px;
  display: flex;
  align-items: flex-end;
  justify-content: space-between;
  gap: 18px;
}
.sc-brand{
  font-family: Georgia, "Times New Roman", serif;
  font-size: 40px;
  line-height: 1;
  letter-spacing: .01em;
  margin: 0;
}
.sc-brand a{ text-decoration: none; color: #1f2a44; }
.sc-brand .last{ color: var(--accent); }

.sc-nav{
  display: flex;
  flex-wrap: wrap;
  gap: 18px;
  justify-content: flex-end;
}
.sc-nav a{
  text-decoration: none;
  text-transform: uppercase;
  letter-spacing: .14em;
  font-size: 12px;
  color: rgba(17,24,39,.55);
}
.sc-nav a:hover{ color: rgba(17,24,39,.85); }
.sc-nav a.current{ color: rgba(17,24,39,.85); font-weight: 700; }

/* Hero banner (like your Research Agenda header) */
.sc-hero{
  border-radius: 10px;
  overflow: hidden;
  margin: 10px auto 0;
}
.sc-hero-inner{
  padding: 48px 18px 42px 18px;
  text-align: center;

  /* If you add an image at assets/studycycles-banner.jpg it will appear automatically */
  background-image:
    linear-gradient(135deg, rgba(0,0,0,.55), rgba(0,0,0,.35)),
    url("{{ site.baseurl }}/assets/studycycles-banner.jpg");
  background-size: cover;
  background-position: center;
}

.sc-hero h1{
  margin: 0;
  font-family: Georgia, "Times New Roman", serif;
  font-size: 56px;
  color: #fff;
  letter-spacing: .01em;
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
  color: rgba(255,255,255,.9);
  font-size: 16px;
  line-height: 1.55;
}

/* Buttons */
.sc-btns{ margin-top: 18px; display: flex; justify-content: center; gap: 12px; flex-wrap: wrap; }
.sc-btn{
  display: inline-block;
  padding: 10px 14px;
  border-radius: 10px;
  text-decoration: none;
  font-weight: 650;
  border: 1px solid rgba(255,255,255,.22);
  background: rgba(255,255,255,.08);
  color: #fff;
}
.sc-btn:hover{ text-decoration: none; transform: translateY(-1px); }
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
.sc-main h3{
  font-family: Georgia, "Times New Roman", serif;
  font-size: 24px;
  margin: 26px 0 10px 0;
  color: #123a2a;
}
.sc-main p{ color: var(--muted); font-size: 16px; line-height: 1.75; }
.sc-main li{ color: var(--muted); line-height: 1.7; }
.sc-main a{ color: #1d4ed8; }
.sc-main a:hover{ text-decoration: underline; }

/* Subtle section separator */
.sc-sep{ height: 1px; background: rgba(0,0,0,.08); margin: 34px 0; }
</style>

<div class="sc-wrap">
  <div class="sc-container sc-topbar">
    <div class="sc-brand">
      <a href="https://yaxinzn.github.io/">
        Yaxin <span class="last">Zheng</span>
      </a>
    </div>

    <nav class="sc-nav" aria-label="Site">
      <a href="https://yaxinzn.github.io/">Home</a>
      <a href="https://yaxinzn.github.io/research-framework/">Research Framework</a>
      <a href="https://yaxinzn.github.io/research-agenda/">Research Agenda</a>
      <a class="current" href="{{ site.baseurl }}/">Study Cycles</a>
      <a href="https://yaxinzn.github.io/about/">About</a>
      <a href="https://yaxinzn.github.io/contact/">Contact</a>
    </nav>
  </div>

  <div class="sc-container sc-hero">
    <div class="sc-hero-inner">
      <h1>Study Cycles</h1>
      <h2>Weekly loops across core fields</h2>
      <p>
        A living study archive—re-deriving, reorganizing, and returning until the key ideas become intuitive and usable.
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
</div>

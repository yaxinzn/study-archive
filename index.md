---
layout: null
permalink: /
---

<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Study Cycles | Yaxin Zheng</title>

<style>
:root{
  --accent: #b08a2e;  /* gold */
  --ink: #111827;
  --muted: rgba(17,24,39,.72);
  --nav: rgba(17,24,39,.40);
  --nav-active: rgba(17,24,39,.82);
  --max: 980px;
}

body{ margin:0; background:#fff; color:var(--ink); font-family: system-ui, -apple-system, Segoe UI, Roboto, Arial, sans-serif; }
a{ color:#1d4ed8; text-decoration:none; }
a:hover{ text-decoration:underline; }

.sc-container{ max-width: var(--max); margin: 0 auto; padding: 0 18px; }

/* Top header (Weebly-like: centered name + centered nav) */
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
.sc-name a{ color:#1f2a44; text-decoration:none; }
.sc-name .last{ color: var(--accent); }

.sc-nav{
  margin-top: 12px;
  display: flex;
  justify-content: center;
  gap: 26px;
  flex-wrap: wrap;
}
.sc-nav a{
  text-transform: uppercase;
  letter-spacing: .14em;
  font-size: 12px;
  color: var(--nav);
}
.sc-nav a:hover{ color: var(--nav-active); text-decoration:none; }
.sc-nav a.current{ color: var(--nav-active); font-weight: 700; }

/* Hero banner (single, centered; no duplicate theme banner) */
.sc-hero{
  margin: 18px auto 0;
  border-radius: 6px;
  overflow: hidden;
}
.sc-hero-inner{
  padding: 52px 18px 48px 18px;
  text-align: center;

  /* If assets/studycycles-banner.jpg exists, it will show; otherwise gradient still works */
  background-image:
    linear-gradient(135deg, rgba(0,0,0,.40), rgba(0,0,0,.25)),
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

/* Buttons */
.sc-btns{ margin-top: 18px; display: flex; justify-content: center; gap: 12px; flex-wrap: wrap; }
.sc-btn{
  display:inline-block;
  padding:10px 14px;
  border-radius:10px;
  border:1px solid rgba(255,255,255,.24);
  background: rgba(255,255,255,.08);
  color:#fff;
  font-weight:650;
}
.sc-btn:hover{ text-decoration:none; transform: translateY(-1px); }
.sc-btn.gold{
  border-color: rgba(176,138,46,.55);
  background: rgba(176,138,46,.18);
}

/* Body */
.sc-main{ padding: 34px 0 68px 0; }
.sc-main h2{
  font-family: Georgia, "Times New Roman", serif;
  font-size: 34px;
  margin: 30px 0 10px 0;
  color: #0f3d2e;
}
.sc-main p{ color: var(--muted); font-size: 16px; line-height: 1.78; }
.sc-main li{ color: var(--muted); line-height: 1.72; }
.sc-sep{ height: 1px; background: rgba(0,0,0,.08); margin: 34px 0; }
</style>
</head>

<body>
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
      <p>Weekly loops across micro, macro, econometrics, empirical IO, asset pricing, corporate finance, and macro-finance.</p>

      <div class="sc-btns">
        <a class="sc-btn gold" href="{{ site.baseurl }}/updates/">View Updates (NEWS)</a>
        <a class="sc-btn" href="https://github.com/yaxinzn/study-archive">View on GitHub</a>
      </div>
    </div>
  </div>

  <div class="sc-container sc-main">
    <h2>Method: the 7-day loop (Saturday = review)</h2>
    <p>
      I study in repeating seven-day cycles. Each week is a complete loop, and <strong>Saturday is reserved for review</strong>:
      consolidating notes, reconnecting ideas across topics, and updating reading maps. I then restart the cycle—refining summaries,
      re-deriving core results, and iterating until the foundations are internalized.
    </p>

    <div class="sc-sep"></div>

    <h2>Materials</h2>
    <ul>
      <li><strong><a href="{{ site.baseurl }}/materials/micro/">Micro</a></strong> — preferences, uncertainty, general equilibrium, mechanisms</li>
      <li><strong><a href="{{ site.baseurl }}/materials/macro/">Macro</a></strong> — growth, business cycles, monetary frameworks</li>
      <li><strong><a href="{{ site.baseurl }}/materials/econometrics/">Econometrics</a></strong> — identification, estimation, inference, robustness</li>
      <li><strong><a href="{{ site.baseurl }}/materials/math-foundations/">Math Foundations</a></strong> — linear algebra, probability, optimization, analysis</li>
      <li><strong><a href="{{ site.baseurl }}/materials/tfp-measurement/">TFP Measurement</a></strong> — production functions, OP/LP/ACF, implementation</li>
      <li><strong><a href="{{ site.baseurl }}/materials/eio/">Empirical IO</a></strong> — demand, costs, conduct, entry/exit, counterfactual analysis</li>
      <li><strong><a href="{{ site.baseurl }}/materials/ap-theory/">Asset Pricing (Theory)</a></strong> — SDF, no-arbitrage, equilibrium pricing</li>
      <li><strong><a href="{{ site.baseurl }}/materials/ap-empirical/">Asset Pricing (Empirical)</a></strong> — factors, predictability, anomalies, methods</li>
      <li><strong><a href="{{ site.baseurl }}/materials/cf-theory/">Corporate Finance (Theory)</a></strong> — contracting, capital structure, governance</li>
      <li><strong><a href="{{ site.baseurl }}/materials/cf-empirical/">Corporate Finance (Empirical)</a></strong> — causal designs, measurement, firm behavior</li>
      <li><strong><a href="{{ site.baseurl }}/materials/macro-finance/">Macro-Finance</a></strong> — risk premia, term structure, policy transmission</li>
    </ul>

    <div class="sc-sep"></div>

    <h2>Use these materials</h2>
    <p>
      If this study style—or any of the materials here—ends up being helpful, you’re very welcome to reuse the notes or adapt the structure
      in whatever way fits your learning goals.
    </p>
  </div>
</body>
</html>

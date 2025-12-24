---
title: Study Cycles
---

<style>
.page-grid{
  display: grid;
  grid-template-columns: 290px 1fr;
  gap: 28px;
  align-items: start;
}
@media (max-width: 900px){
  .page-grid{ grid-template-columns: 1fr; }
}

.news-box{
  border: 1px solid rgba(0,0,0,.12);
  border-radius: 10px;
  padding: 16px 16px 10px 16px;
  background: #fff;
  position: sticky;
  top: 16px;
}
@media (max-width: 900px){
  .news-box{ position: static; }
}

.news-title{
  text-align: center;
  letter-spacing: .12em;
  font-weight: 700;
  margin: 2px 0 12px 0;
  position: relative;
}
.news-title:before,
.news-title:after{
  content: "";
  position: absolute;
  top: 50%;
  width: 36%;
  height: 1px;
  background: rgba(0,0,0,.15);
}
.news-title:before{ left: 0; }
.news-title:after{ right: 0; }

.news-item{
  padding: 10px 0;
  border-top: 1px solid rgba(0,0,0,.10);
}
.news-item:first-of-type{
  border-top: none;
  padding-top: 0;
}
.news-date{ font-weight: 700; }
.news-note{ margin-top: 4px; }
</style>

<div class="page-grid">

<aside class="news-box">
  <div class="news-title">NEWS</div>

  {% if site.data.news and site.data.news.size > 0 %}
    {% for n in site.data.news limit:8 %}
      <div class="news-item">
        <div><span class="news-date">{{ n.date }}</span>: {{ n.title }}</div>
        {% if n.note %}
          <div class="news-note">{{ n.note }}</div>
        {% endif %}
      </div>
    {% endfor %}
  {% else %}
    <div class="news-item">
      <div><span class="news-date">—</span> No updates yet.</div>
      <div class="news-note">This box will auto-fill after you enable the NEWS generator.</div>
    </div>
  {% endif %}
</aside>

<div markdown="1">

# Study Cycles

**Updates:** see **[NEWS / update log]({{ site.baseurl }}/updates/)**.

**Updates:** see **[NEWS / update log](updates/)**.

I maintain this section as a living study archive—my way of learning the literature deeply and systematically across the core fields that shape modern financial economics. The goal is mastery through repetition: reading, re-deriving, reorganizing, and returning until the key ideas become intuitive and usable.

## Method: the 7-day loop (Saturday = review)
I study in repeating seven-day cycles. Each week is a complete loop, and **Saturday is reserved for review**: consolidating notes, reconnecting ideas across topics, and updating reading maps. I then restart the cycle—refining summaries, re-deriving core results, and iterating until the foundations are internalized.

## Materials
- **[Micro](materials/micro/)** — preferences, uncertainty, general equilibrium, mechanisms
- **[Macro](materials/macro/)** — growth, business cycles, monetary frameworks
- **[Econometrics](materials/econometrics/)** — identification, estimation, inference, robustness
- **[Math Foundations](materials/math-foundations/)** — linear algebra, probability, optimization, analysis
- **[Empirical IO](materials/eio/)** — demand, costs, conduct, entry/exit, counterfactual analysis
- **[Asset Pricing (Theory)](materials/ap-theory/)** — SDF, no-arbitrage, equilibrium pricing
- **[Asset Pricing (Empirical)](materials/ap-empirical/)** — factors, predictability, anomalies, methods
- **[Corporate Finance (Theory)](materials/cf-theory/)** — contracting, capital structure, governance
- **[Corporate Finance (Empirical)](materials/cf-empirical/)** — causal designs, measurement, firm behavior
- **[Macro-Finance](materials/macro-finance/)** — risk premia, term structure, policy transmission

## Use these materials
If this study style—or any of the materials here—ends up being helpful, you’re very welcome to **join me**, **reuse the notes**, or **adapt the structure** in whatever way fits your learning goals.

</div>
</div>

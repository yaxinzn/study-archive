---
layout: minimal
title: Updates
permalink: /updates/
hero_title: Updates
hero_subtitle: Change log
hero_desc: Commit-based update history for Study Cycles (newest → oldest).
hide_name: true

---
<style>
.news-box{
  border: 1px solid rgba(0,0,0,.12);
  border-radius: 10px;
  padding: 18px 18px 10px 18px;
  margin: 18px 0 26px 0;
  background: #fff;
  max-height: 70vh;
  overflow-y: auto;
}
.news-title{
  text-align: center;
  letter-spacing: .12em;
  font-weight: 700;
  margin: 2px 0 14px 0;
  position: relative;
}
.news-title:before,
.news-title:after{
  content: "";
  position: absolute;
  top: 50%;
  width: 38%;
  height: 1px;
  background: rgba(0,0,0,.15);
}
.news-title:before{ left: 0; }
.news-title:after{ right: 0; }
.news-item{
  padding: 12px 0;
  border-top: 1px solid rgba(0,0,0,.10);
}
.news-item:first-of-type{
  border-top: none;
  padding-top: 0;
}
.news-date{ font-weight: 700; }
.news-note{ margin-top: 6px; }
</style>

<div class="news-box">
  <div class="news-title">NEWS</div>

  {% assign news_count = 0 %}
  {% if site.data.news_manual %}
    {% assign news_count = news_count | plus: site.data.news_manual.size %}
  {% endif %}
  {% if site.data.news %}
    {% assign news_count = news_count | plus: site.data.news.size %}
  {% endif %}

  {% if news_count > 0 %}
    {% if site.data.news_manual %}
      {% for n in site.data.news_manual %}
        <div class="news-item">
          <div><span class="news-date">{{ n.date }}</span>: {{ n.title }}</div>
          {% if n.note %}
            <div class="news-note">{{ n.note }}</div>
          {% endif %}
        </div>
      {% endfor %}
    {% endif %}

    {% if site.data.news %}
      {% for n in site.data.news %}
        <div class="news-item">
          <div><span class="news-date">{{ n.date }}</span>: {{ n.title }}</div>
          {% if n.note %}
            <div class="news-note">{{ n.note }}</div>
          {% endif %}
        </div>
      {% endfor %}
    {% endif %}
  {% else %}
    <div class="news-item">
      <div><span class="news-date">—</span> No updates yet.</div>
    </div>
  {% endif %}
</div>

<p style="margin-top:18px;">
  <a href="{{ site.baseurl }}/">← Back to Study Cycles</a>
</p>

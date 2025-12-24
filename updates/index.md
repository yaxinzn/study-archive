---
title: Updates
---

<style>
.news-box{
  border: 1px solid rgba(0,0,0,.12);
  border-radius: 10px;
  padding: 18px 18px 10px 18px;
  margin: 18px 0 26px 0;
  background: #fff;
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

# Updates

<div class="news-box">
  <div class="news-title">NEWS</div>

  {% if site.data.news and site.data.news.size > 0 %}
    {% for n in site.data.news %}
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
    </div>
  {% endif %}
</div>

<p style="margin-top:18px;">
  <a href="{{ site.baseurl }}/">← Back to Study Cycles</a>
</p>

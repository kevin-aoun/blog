---
title: Home
layout: home
nav_order: 1
---

# Kevin's Notes

Welcome. This is a place to park ideas before they evaporate.

## Timeline

{% assign notes = site.pages | where_exp: "p", "p.date" | sort: "date" | reverse %}
{% if notes == empty %}
No notes yet.
{% else %}
<ul class="timeline">
{% for note in notes %}
  <li>
    <time>{{ note.date | date: "%Y-%m-%d" }}</time> &mdash;
    <a href="{{ note.url | relative_url }}">{{ note.title }}</a>
    {% if note.parent %}<span class="timeline-section">{{ note.parent }}</span>{% endif %}
    {% if note.description %}<em class="timeline-desc">{{ note.description }}</em>{% endif %}
  </li>
{% endfor %}
</ul>
{% endif %}

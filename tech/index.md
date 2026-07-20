---
title: Tech
permalink: /tech/
---

# Tech

Build logs, half-baked architectures, and notes-to-self.

{% assign notes = site.pages | where: "parent", page.title | sort: "date" | reverse %}
{% if notes == empty %}
No notes yet.
{% else %}
<ul class="post-list">
{% for note in notes %}
  <li>
    <a class="post-link" href="{{ note.url | relative_url }}">{{ note.title }}</a>{% if note.parent %}<span class="tag tag--{{ note.parent | downcase }}">{{ note.parent }}</span>{% endif %}{% if note.legacy %}<span class="tag tag--legacy">Legacy</span>{% endif %}
    {% if note.date %}<div class="post-meta"><time datetime="{{ note.date | date_to_xmlschema }}">{{ note.date | date: "%b %-d, %Y" }}</time></div>{% endif %}
    {% if note.description %}<p class="post-desc">{{ note.description }}</p>{% endif %}
  </li>
{% endfor %}
</ul>
{% endif %}

---
title: About
permalink: /about/
---

# About

I'm an AI engineer with 3 years of hands-on experience, from POCs to cloud deployments and startups. I have worked across domains like browser agents, voice AI, finetuning transformers for translation, reinforcement learning, and computer vision.

<p class="human-badge"><span class="badge-ic">{% include_relative assets/icons/human-made.svg %}</span> Human made blog</p>

I don't let AI write my posts. Sure, I use it to brainstorm ideas and to polish how I deliver them, but never in full control. It is an assistant, not a replacement for my own judgement and critical thinking. And when I do lean on a model to help me write, you will see a disclaimer on that post.

## My stack

<ul class="stack">
  <li class="stack-item"><span class="stack-role">Main LLM</span><span class="stack-tool"><span class="tool-ic tool-ic--claude">{% include_relative assets/icons/claude.svg %}</span>Claude Fable 5 / <span class="tool-ic">{% include_relative assets/icons/openai.svg %}</span>GPT Sol 5</span></li>
  <li class="stack-item"><span class="stack-role">Workhorse LLM</span><span class="stack-tool"><span class="tool-ic">{% include_relative assets/icons/gemini.svg %}</span>Gemini 3.1 Flash Lite</span></li>
  <li class="stack-item"><span class="stack-role">Harness</span><span class="stack-tool"><span class="tool-ic">{% include_relative assets/icons/pi.svg %}</span>Pi</span></li>
  <li class="stack-item"><span class="stack-role">IDE</span><span class="stack-tool"><span class="tool-ic">{% include_relative assets/icons/zed.svg %}</span>Zed</span></li>
  <li class="stack-item"><span class="stack-role">Notes</span><span class="stack-tool"><span class="tool-ic tool-ic--obsidian">{% include_relative assets/icons/obsidian.svg %}</span>Obsidian + <span class="tool-ic tool-ic--md">{% include_relative assets/icons/markdown.svg %}</span>Markdown</span></li>
</ul>

<div class="stack-notes">
  <p><span class="stack-notes-label">Main LLM</span> is for research and heavy tasks. I run it as a critique loop, where GPT reviews and critiques Fable and we iterate on the feedback.</p>
  <p><span class="stack-notes-label">Workhorse LLM</span> is what I reach for inside the solutions I design, when I need something quick, multimodal, and cheap.</p>
</div>

## Skills

<div class="skills-head">
  <p>Reusable Claude Code skills I have built. Each card links to its source, so you can read it or download it.</p>
  <a class="skills-all" href="https://github.com/kevin-aoun?tab=repositories" target="_blank" rel="noopener">More on GitHub</a>
</div>

<div class="skills">
{% for skill in site.data.skills %}
  <div class="skill-card">
    <a class="skill-card__main" href="{{ skill.url }}" target="_blank" rel="noopener" aria-label="{{ skill.name }} on GitHub"></a>
    <span class="skill-name">{{ skill.name }}</span>
    <span class="skill-desc">{{ skill.desc }}</span>
    {% if skill.credit_name %}
    <span class="skill-credit">Shared with me by <a href="{{ skill.credit_url }}" target="_blank" rel="noopener">{{ skill.credit_name }}</a></span>
    {% endif %}
    <span class="skill-link">View + download</span>
  </div>
{% endfor %}
</div>

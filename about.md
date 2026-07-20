---
title: About
permalink: /about/
---

# About

I'm an AI engineer with 3 years of hands-on experience, from POCs to cloud deployments and startups. I have worked across domains like browser agents, voice AI, finetuning transformers for translation, reinforcement learning, and computer vision.

<p class="human-badge"><span class="badge-ic">{% include_relative assets/icons/human-made.svg %}</span> Human made blog</p>

I don't write my posts with AI. I believe AI is an assistant, not a replacement for your own engineering judgement and critical thinking. You can hand it the busywork, gathering information and fact-checking it, or implementing a plan you already made, but it should never be in the driver's seat.

## My stack

<ul class="stack">
  <li class="stack-item"><span class="stack-role">Main LLM</span><span class="stack-tool"><span class="tool-ic tool-ic--claude">{% include_relative assets/icons/claude.svg %}</span>Claude Fable 5 / <span class="tool-ic">{% include_relative assets/icons/openai.svg %}</span>GPT Sol 5</span></li>
  <li class="stack-item"><span class="stack-role">Harness</span><span class="stack-tool"><span class="tool-ic">{% include_relative assets/icons/terminal.svg %}</span>Claude Code</span></li>
  <li class="stack-item"><span class="stack-role">IDE</span><span class="stack-tool"><span class="tool-ic">{% include_relative assets/icons/zed.svg %}</span>Zed</span></li>
  <li class="stack-item"><span class="stack-role">Notes</span><span class="stack-tool"><span class="tool-ic tool-ic--obsidian">{% include_relative assets/icons/obsidian.svg %}</span>Obsidian + <span class="tool-ic tool-ic--md">{% include_relative assets/icons/markdown.svg %}</span>Markdown</span></li>
</ul>

## Skills

<div class="skills-head">
  <p>Reusable Claude Code skills I have built. Each card links to its source, so you can read it or download it.</p>
  <a class="skills-all" href="https://github.com/kevin-aoun/skills" target="_blank" rel="noopener">All skills on GitHub</a>
</div>

<div class="skills">
{% for skill in site.data.skills %}
  <a class="skill-card" href="{{ skill.url }}" target="_blank" rel="noopener">
    <span class="skill-name">{{ skill.name }}</span>
    <span class="skill-desc">{{ skill.desc }}</span>
    <span class="skill-link">View + download</span>
  </a>
{% endfor %}
</div>

# Kevin's Notes

A minimal, self-contained Jekyll site. No remote theme — just a handful of
layouts and one stylesheet, built to look like the [shadcn/ui](https://ui.shadcn.com)
docs: a toggleable left sidebar, content centered with wide margins, the Geist
typeface, a near-black background with silver text, and a single orange accent
used sparingly.

You write Markdown; Cloudflare builds and hosts the site on every push to `main`.

## What's in here

```
blog/
├── _config.yml            # site settings, sidebar nav, footer links
├── _layouts/
│   ├── default.html       # the shell: header, sidebar, content, footer
│   └── note.html          # a dated note (title, description, date/author)
├── assets/css/style.scss  # the entire design system (CSS variables + rules)
├── index.md               # home — a reverse-chronological list of notes
├── about.md               # a top-level page
├── tech/                  # a section + its notes
│   ├── index.md
│   ├── putting-llms-and-genai-to-work.md   # no extras -> just the file
│   └── durable-agents.md                   # has extras -> sibling folder below
│       └── durable-agents/                 # same name as the note, holds its extras
│           ├── lab/                        # runnable code for the post
│           └── *.png                       # images the post embeds
├── essays/                # another section, same pattern
│   ├── index.md
│   └── ai.md
│       └── ai/assets/                      # ai.md's images
├── Gemfile                # for previewing locally (optional)
└── README.md              # this file
```

There's no JavaScript framework and no build step beyond Jekyll — the sidebar
toggle is ~15 lines of inline vanilla JS, and the ↗ / sidebar / GitHub glyphs
are inlined [Lucide](https://lucide.dev) SVGs (no icon library to load).

Notes are plain pages, not a Jekyll collection — a note is just a Markdown
file with `layout: note` in its front matter, living directly under its
section folder (`tech/`, `essays/`, …). If a note needs images or runnable
code, give it a same-named sibling folder next to it (e.g. `durable-agents.md`
+ `durable-agents/`) rather than nesting the note itself inside a folder.
Image paths in the post body are written relative to the note's own URL
(e.g. `durable-agents/lab/assets/foo.png`), so that folder name has to match
the note's permalink, not just its filename.

---

## Writing a note

Create a Markdown file (folders are just tidiness). Add front matter:

```yaml
---
title: "My New Idea"
layout: note        # gives you the dated note header
parent: Tech        # makes it appear under "Tech" in the sidebar + section page
date: 2026-07-17
author: Kevin Aoun
description: "One-line summary shown in listings and under the title."
legacy: true        # optional — shows a small "Legacy" badge
---
```

- `parent` links a note to a section. Sections themselves are defined in
  `_config.yml` under `nav:` (a section entry has a `section:` key matching the
  `parent` value).
- Notes with a `date` are listed newest-first on the home page and on their
  section page.
- Pages without `layout: note` (like `about.md`) just get the plain shell.

## Editing the chrome

| Want to… | Do this |
| --- | --- |
| Change the sidebar items | edit `nav:` in `_config.yml` |
| Change the footer links | edit `social:` in `_config.yml` |
| Retune colors / spacing / fonts | edit the `:root` variables at the top of `assets/css/style.scss` |
| Change the site title | `title:` in `_config.yml` |

The palette lives in one place — the CSS custom properties in `:root`:
`--background` (`#02040a`), `--foreground`/`--heading` (silver),
`--accent` (`#d9401a`, used only for the title dot, the active note indicator,
and text selection), plus `--border`, `--radius`, and the layout widths.

---

## Publish it

Cloudflare Workers builds it from GitHub on every push to `main` and serves it at
https://blog.kevinaoun.dev (the Worker `blog`, configured in `wrangler.jsonc`):

- Build command: `bundle exec jekyll build` (Cloudflare runs `bundle install` itself).
- Deploy command: `npx wrangler deploy`.
- Ruby is pinned to 3.3 in `.ruby-version`: the `github-pages` gem (Jekyll 3) breaks on
  Ruby 3.4, which no longer ships `bigdecimal` and `csv` by default.

GitHub Pages serves only redirects now, from the `gh-pages` branch: every old
kevin-aoun.github.io/blog page sends readers to the same page here.

## Preview locally (optional)

```bash
bundle install
bundle exec jekyll serve
# open http://localhost:4000/
```

The `Gemfile` uses the `github-pages` gem so local builds match production.

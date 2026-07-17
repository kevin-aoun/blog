# Kevin's Notes — a GitHub Pages blog

A minimal, self-contained Jekyll site. No remote theme — just a handful of
layouts and one stylesheet, built to look like the [shadcn/ui](https://ui.shadcn.com)
docs: a toggleable left sidebar, content centered with wide margins, the Geist
typeface, a near-black background with silver text, and a single orange accent
used sparingly.

You write Markdown; GitHub builds and hosts the site for free.

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
├── philosophy/index.md    # a section landing page (lists its notes)
├── tech/                  # a section + its notes
│   ├── index.md
│   ├── putting-llms-and-genai-to-work.md
│   └── genai-cash-in-the-code.md
├── Gemfile                # for previewing locally (optional)
└── README.md              # this file
```

There's no JavaScript framework and no build step beyond Jekyll — the sidebar
toggle is ~15 lines of inline vanilla JS, and the ↗ / sidebar / GitHub glyphs
are inlined [Lucide](https://lucide.dev) SVGs (no icon library to load).

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

1. Push this repo to GitHub.
   - Site at `https://USERNAME.github.io/blog` → repo named `blog`, keep
     `baseurl: "/blog"` in `_config.yml`.
   - Site at `https://USERNAME.github.io` → repo named `USERNAME.github.io`,
     set `baseurl: ""`.
2. **Settings → Pages → Build and deployment → Source: Deploy from a branch**,
   pick `main` / `/ (root)`, save.
3. Wait ~1 minute. No Actions to configure.

## Preview locally (optional)

```bash
bundle install
bundle exec jekyll serve
# open http://localhost:4000/blog/
```

The `Gemfile` uses the `github-pages` gem so local builds match production.

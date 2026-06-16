# Kevin's Notes — a GitHub Pages blog

A minimal Jekyll site using the [just-the-docs](https://just-the-docs.com)
theme. It gives you a **nested, collapsible left sidebar** and **full-text
search** with almost no configuration. You write Markdown; GitHub builds and
hosts the site for free.

## What's in here

```
blog-starter/
├── _config.yml              # site + theme settings
├── index.md                 # home page
├── about.md                 # a simple top-level page
├── philosophy/
│   ├── index.md             # section landing (a sidebar parent)
│   ├── arendt-on-action.md  # a note nested under Philosophy
│   └── the-vita-activa.md
├── tech/
│   ├── index.md
│   ├── notes-on-rag.md
│   └── thinking-in-priors.md
├── Gemfile                  # for previewing locally (optional)
├── .gitignore
└── README.md                # this file
```

All the content files are **dummies** — open any of them, see how it's built,
then replace the text with your own.

---

## Publish it (the only steps that matter)

1. Create a repository on GitHub.
   - For a site at `https://USERNAME.github.io`, name the repo exactly
     `USERNAME.github.io` and leave `baseurl: ""` in `_config.yml`.
   - For a site at `https://USERNAME.github.io/blog`, name the repo `blog`
     and set `baseurl: "/blog"` in `_config.yml`.
2. Put these files in the repo and push:
   ```bash
   cd blog-starter
   git init
   git add .
   git commit -m "Initial blog"
   git branch -M main
   git remote add origin https://github.com/USERNAME/REPO.git
   git push -u origin main
   ```
3. On GitHub: **Settings → Pages → Build and deployment → Source: Deploy from
   a branch**, pick `main` / `/ (root)`, save.
4. Wait ~1 minute. Your site is live. Edit `url:` and the `USERNAME`
   placeholders in `_config.yml` to match your repo.

That's it — no build step to run, no Actions to configure.

---

## Add a new note

Create a Markdown file anywhere (folders are just for your own tidiness — the
sidebar is built from front matter, not file location). At the top of the file,
add a front-matter block:

```yaml
---
title: My New Idea
parent: Tech          # omit this line for a top-level entry
nav_order: 3          # controls position within its section
---
```

Then write Markdown below it. Push, and it appears in the sidebar.

### How the sidebar nesting works

- A **section** is any page with `has_children: true` (see `philosophy/index.md`).
- A **child** points at its section with `parent: <that section's title>`.
- `nav_order` sorts entries within the same level.
- You can go deeper (a child can itself be a `parent`) — just-the-docs supports
  multiple levels.

---

## Preview locally (optional)

You don't need this — editing on GitHub works fine — but if you want to see
changes before pushing:

```bash
# one-time: install Ruby + bundler, then
bundle install
bundle exec jekyll serve
# open http://localhost:4000
```

The `Gemfile` uses the `github-pages` gem so your local build matches what
GitHub produces.

---

## Common tweaks

| Want to… | Do this in `_config.yml` |
| --- | --- |
| Switch to a light theme | `color_scheme: light` |
| Change the site title | `title: ...` |
| Turn off search | `search_enabled: false` |
| Change the top-right link | edit the `aux_links:` block |

### Dated blog posts instead of (or alongside) notes

just-the-docs is page-based, not date-based. If you also want a classic
reverse-chronological blog feed, create a `_posts/` folder with files named
`YYYY-MM-DD-title.md`. They won't auto-populate the sidebar, but you can list
them on a page with a small Liquid loop. Say the word and I'll add that.

### Rendering math (LaTeX)

`thinking-in-priors.md` includes an equation that won't render until you enable
MathJax. The quickest way is to add a small include with the MathJax script —
ask if you want that wired in.

---

Built to be replaced. Delete the dummy notes, keep the structure, and start
writing.

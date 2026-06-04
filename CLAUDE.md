# CLAUDE.md — Alignment Foundry

Working guide for Claude when developing in this repo. Read this before
adding or editing site pages.

## What this repo is

The published Jekyll site for **The Alignment Foundry** (the workspace behind
[alexsmoy.com](https://alexsmoy.com)). Source lives in `/docs` and is deployed
by the default GitHub Pages pipeline from the `main` branch, `/docs` folder.
Live at <https://alexsmoy.github.io/alignment-foundry/> (note the
`/alignment-foundry` baseurl — every absolute in-site path includes it).

## Two kinds of pages

1. **Jekyll-managed pages** — `index.md`, `about.md`, `projects.md`,
   `resources.md`, `reports/index.md`, `404.html`. These share the site chrome
   via `_layouts/` + `_includes/` (`nav.html`, `footer.html`, `head.html`,
   `scripts.html`). The nav/footer here are centralized — edit the include once.

2. **Standalone interactive HTML pages** — the one-page briefings in
   `docs/reports/*.html` and the field references in `docs/resources/*.html`
   (plus the ICM Workspace Explorer). Each is a self-contained HTML file with
   its own inline `<style>` and `<script>`; they do **not** use the Jekyll
   layouts, so their nav/footer must be maintained per-file to the standard
   below.

## Brand system (do not deviate)

- **Palette:** deep blue `#0A2342`, deep aqua `#14786C`, charcoal `#1C1C1E`,
  aquamarine `#67FCF1`, light teal `#96E5AC`, white `#FFFFFF`. Brand gradient:
  `linear-gradient(135deg,#0A2342 0%,#14786C 55%,#67FCF1 100%)`.
- **Type:** Hanken Grotesk (weights 400/500/700) via Google Fonts.
- **Motion:** layered hero backdrops, accent "eyebrow" rules, scroll-reveal
  fade-ups, accent-bar cards. Always honor `prefers-reduced-motion` and degrade
  gracefully without JS.
- The shared styles live in `docs/assets/css/style.scss`. The standalone pages
  reuse the same tokens/aesthetic inline.

The **canonical reference** for a standalone page's structure and chrome is the
latest report: `docs/reports/2026-06-microsoft-build-agent-first.html`. Match it.

## Standalone page nav + footer standard (REQUIRED)

Every standalone report/resource/project HTML page MUST include all three of
these, mirroring the Microsoft Build 2026 report:

1. **Home link on the brand** — the logo + wordmark is a single link back to
   the site home:
   ```html
   <a class="nav-brand" href="/alignment-foundry/" aria-label="The Alignment Foundry &mdash; home">
     <svg class="nav-logo" ...>…</svg>Alex S. Moy &mdash; AI Alignment Report
   </a>
   ```
   (Use `&mdash; Field Reference` as the wordmark suffix for resources.)
   It must be an `<a>`, never a `<div>`.

2. **"Back to all …" link in the nav** — the final `<li>` in `.nav-links`:
   - Reports → `<li><a class="nav-back" href="/alignment-foundry/reports/">&larr; All reports</a></li>`
   - Resources → `<li><a class="nav-back" href="/alignment-foundry/resources/">&larr; All resources</a></li>`
   - Projects → `<li><a class="nav-back" href="/alignment-foundry/projects/">&larr; All projects</a></li>`

3. **"Back to all …" link in the footer** — prepend it to the footer's last
   `<p>` so it survives on mobile (where `.nav-links` is hidden):
   ```html
   <p><a href="/alignment-foundry/reports/">&larr; All reports</a> &middot; <!-- existing meta --></p>
   ```

Required supporting CSS (add once per standalone file, next to the existing
`.nav-links a:hover` rule):
```css
.nav-brand{text-decoration:none;transition:opacity .2s}
.nav-brand:hover{opacity:.82}
.nav-back{font-size:13px;font-weight:700;color:var(--aquamarine);text-decoration:none;display:flex;align-items:center;gap:6px;transition:gap .2s}
.nav-back:hover{gap:10px}
footer a{color:var(--aquamarine);text-decoration:none;font-weight:700}
```

> **Enforced in CI.** `.github/workflows/standalone-nav-check.yml` runs
> `.github/scripts/check_standalone_nav.py` on every PR that touches
> `docs/reports/**` or `docs/resources/**`. It fails the build if a top-level
> `reports/*.html` or `resources/*.html` page is missing the home link, the
> nav back link, the footer back link, or the supporting CSS. Run it locally
> with `python3 .github/scripts/check_standalone_nav.py` before pushing.

## Jekyll page conventions

- Section headings (`##`) automatically render with an accent rule — no markup
  needed.
- Page hero/eyebrow: set `eyebrow:` in front matter (falls back to the title).
  Example: `eyebrow: Executive Briefings for AI Leaders`.
- Card grids: wrap link cards in `<div class="card-grid">` and add
  `class="card reveal" data-stagger="N"` (N = 0,1,2,…) for the staggered
  scroll-reveal entrance. Category label goes in `<p class="card-meta">`.
- When you publish a new standalone report/resource, also add a `.card` for it
  to the relevant index (`reports/index.md` or `resources.md`).

## Checklist — adding a new report or resource

Run through ALL of these before committing a new standalone HTML page:

- [ ] Built from the Microsoft Build report's structure; brand palette + Hanken
      Grotesk only.
- [ ] `<a class="nav-brand" href="/alignment-foundry/">` home link with logo.
- [ ] `.nav-back` "← All reports/resources/projects" link as the last nav item.
- [ ] Footer "← All …" link prepended to the last footer `<p>`.
- [ ] The four `.nav-brand`/`.nav-back`/`footer a` CSS rules are present.
- [ ] `prefers-reduced-motion` is respected; page works with JS disabled.
- [ ] A `.card` entry added to the matching index page (`reports/index.md` or
      `resources.md`) with `reveal` + `data-stagger`.
- [ ] All in-site links use the `/alignment-foundry/...` baseurl.
- [ ] Site still builds (see below).

## Build / verify locally

```bash
cd docs
bundle install
bundle exec jekyll build      # or: bundle exec jekyll serve
```

If the `jekyll` binstub is unavailable, build via the API:
```bash
cd docs && bundle exec ruby -e "require 'jekyll'; Jekyll::Site.new(Jekyll.configuration({'source'=>'.','destination'=>'_site'})).process"
```

To preview standalone pages with correct asset paths under `file://`/local
server, build with `'baseurl'=>''` into a scratch dir and serve that dir.
Build output (`_site/`, `_preview/`) is gitignored — never commit it.

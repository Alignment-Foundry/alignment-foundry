# Alignment Foundry

> *The workshop behind the work. Build ideas, industry insights, and resources for enterprise AI alignment.*

AI doesn't fail because of technology. It fails because leaders, teams, and strategies aren't aligned. This repo is where I build toward solving that problem, in public.

**Alignment Foundry** is the workspace behind [alexsmoy.com](https://alexsmoy.com). It hosts the tools, ideas, and thinking I'm developing at the intersection of enterprise AI strategy, Centers of Excellence, and coalition-building.

The published site lives at **[alexsmoy.github.io/alignment-foundry](https://alexsmoy.github.io/alignment-foundry)**.

---

## What's Here

### 🔧 Projects
Workspace experiments, prototypes, and GitHub Pages projects exploring how enterprise leaders can harness AI as a tool, not a takeover. Early-stage, honest, and in progress.

### 📊 Reports
Curated one-page interactive briefings on major industry conferences and enterprise AI trend reports. Self-contained HTML, built to be skimmed in five minutes.

### 📚 Resources
Published frameworks and reference material, the practical artifacts that help leaders ground AI transformation in governance, accountability, and people.

### 📬 Industry Newsletters *(coming soon)*
Curated insights on enterprise AI transformation, governance, and change management. Mechanics TBD.

---

## Repository Structure

The published Jekyll site lives in `/docs`, built and served by the default GitHub Pages pipeline (no custom Actions workflow):

```
.
├── docs/                    # Jekyll source for the published site
│   ├── _config.yml
│   ├── Gemfile              # pinned to the github-pages gem
│   ├── _layouts/            # custom brand layouts (no upstream theme)
│   ├── _includes/           # head, nav, footer
│   ├── assets/css/          # brand palette + Hanken Grotesk typography
│   ├── reports/             # self-contained interactive HTML briefings
│   ├── index.md             # homepage
│   ├── about.md
│   ├── projects.md
│   ├── resources.md
│   └── 404.html
├── README.md
└── LICENSE
```

GitHub Pages is configured to deploy from the `main` branch, `/docs` folder.

## Local Development

```bash
cd docs
bundle install
bundle exec jekyll serve
```

Site preview at <http://localhost:4000/alignment-foundry/>.

---

## Philosophy

When leaders are equipped and organizations are united, AI delivers more than growth. It creates legacy.

Everything in this repo is guided by one principle: **AI should be a tool, not a takeover.** That means building systems with governance, grounding innovation in accountability, and always keeping people at the center of transformation.

---

## License

**Code and tools** in this repository are licensed under the [MIT License](./LICENSE).

**Written content**, including newsletters, articles, and frameworks, is licensed under [Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)](https://creativecommons.org/licenses/by-nc/4.0/). You're welcome to share and adapt written content with attribution, but not for commercial use without permission.

---

## Connect

**Alex S. Moy**, Enterprise AI Strategist · Architect of AI Alignment

- 🌐 [alexsmoy.com](https://alexsmoy.com)
- 💼 [LinkedIn](https://linkedin.com/in/alexsmoy)

> *Lead with faith. Empower people. Transform through alignment.*

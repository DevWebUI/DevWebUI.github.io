# DevWebUI site

> Landing page for DevWebUI, a free daemon that starts, stops and monitors local dev servers via GUI or MCP.

<!-- odin:about HAND-OWNED above the GENERATED marker. Edit freely; `odin codex about --ingest` carries it back into Odin's Codex. -->

## What it is

A static landing page for DevWebUI, an open-source GUI and MCP control plane for local dev servers. Describes the product's features, comparison with competitors (PM2, hotel, exo), and links to the GitHub repository. Deployed to devwebui.lunarwerx.com via GitHub Pages with zero build dependencies.

## Things not to forget

_The intricacies worth remembering: the gotchas, the half-built parts, the decisions whose
reason lives nowhere else. Odin never overwrites this section._

- Product version, site VERSION file, and the JSON-LD softwareVersion in index.html are three separate hardcoded copies that must be bumped together by hand - they were already out of sync (pricing.md said 0.8.7 while VERSION said 0.1.0). anchors: `VERSION:1`
- robots.txt allowlists AI answer/search crawlers one by one by name (OAI-SearchBot, ChatGPT-User, GPTBot, ClaudeBot, etc.) instead of relying on a wildcard rule, a deliberate choice explained in its own comment so a citation-worthy crawler is never one managed rule change away from losing access. anchors: `robots.txt:6`
- The floating Discord badge markup in index.html is a generated copy shared across the whole LunarWerx site fleet - its own inline comment warns not to hand-edit it here but to change the canonical source and re-run the install script instead. anchors: `index.html:625`
- Brand and media assets (icon.svg, favicon.ico, logo-dark.svg, screenshot.png, share-card.png) sit at the repo root next to index.html - there is no assets/ subdirectory, so new images should be dropped at root and referenced with a root-relative path. anchors: `README.md:9`
- The 'How it works' section walks through using DevWebUI (drop a .devwebui config, open the pane) but assumes the tool is already installed - actual install steps only exist inside the FAQ answers, so a top-to-bottom reader hits usage before installation. anchors: `index.html:457`
- The whole site is one self-contained index.html with no build step, no package manager and no module structure - that is also why the repo carries no generated codemap. anchors: `README.md:6`
- pricing.md lives at the repo root, not under docs/ despite the name - docs/ is reserved for project documentation (README plus the todo/ list), so pricing and AI-discovery files (llms.txt, llms-full.txt, pricing.md, robots.txt, sitemap.xml) all stay at root alongside index.html. anchors: `pricing.md:1`

<!-- odin:about GENERATED BEGIN - rewritten by `odin codex about --publish`; edit the Codex, not this -->

## What Odin knows about this project

Everything from here down is generated from this project's Codex dossier
(`codex/projects/devwebui-github-io.md` in the Odin clone) and is **rewritten on every publish** -
edit the dossier, not this block. Everything ABOVE the marker is yours.

### At a glance

- **Ships as:** static site - deployed to GitHub Pages
- **Live at:** https://devwebui.lunarwerx.com/
- **Entry points:** `site_root`
- **Deploys via:** github-pages
- **Domain:** process management, dev servers, MCP integration, local-first, open source, GUI + CLI, agent tooling
- **Remote:** https://github.com/DevWebUI/DevWebUI.github.io.git

### Architecture

- `./` - Root contains index.html (main landing page), 404.html (not-found page), CNAME (DNS config), VERSION, and the AI-agent discovery files llms.txt/llms-full.txt/pricing.md/sitemap.xml/robots.txt
- `./ (brand assets, root-level - no assets/ subdirectory exists)` - icon.svg, favicon.ico, logo-dark.svg, screenshot.png and share-card.png all live at repo root alongside index.html, not under an ./assets/ path
- `./docs/` - Project documentation only: README describing the docs/todo split, and todo/ for outstanding work. pricing.md is NOT under docs/ - it is a repo-root file.

### Features

11 recorded - 11 shipped, 0 partial, 0 planned. Each `path:line` is where the feature is DEFINED, checked by `odin codex check`.

**Shipped**

- **Landing page hero** - Primary landing page introducing DevWebUI as a GUI and MCP control plane for local dev servers, with headline, tagline and call-to-action. - `index.html:6`, `index.html:417`
- **How it works guide** - Three-step setup guide: drop .devwebui config, open the pane, and control servers via GUI or agents. - `index.html:457`
- **Feature showcase cards** - Six feature cards describing one-click control, MCP integration, project grouping, port conflict detection, error deduplication, and Windows tray app. - `index.html:467`
- **Human vs. agent comparison** - Side-by-side comparison: humans get a GUI with status/CPU/memory/logs; agents get 31 MCP tools for the same daemon. - `index.html:504`
- **Competitor comparison** - Direct feature comparison with PM2 (paid dashboard), hotel (lightweight, no monitoring), and exo; clarifies DevWebUI's free pricing and MCP capabilities. - `index.html:539`
- **FAQ section** - Structured FAQPage with Q&A on pricing, open-source licensing, platform support, and roadmap. - `index.html:343`
- **404 error page** - Branded not-found page with navigation back to home; GitHub Pages serves on 404 errors. - `404.html:1`
- **Metadata and schema markup** - JSON-LD SoftwareApplication, Organization, BreadcrumbList and FAQPage schema for SEO and AI indexing; Open Graph and Twitter card images. - `index.html:289`, `index.html:13`
- **AI agent discovery files (llms.txt, llms-full.txt, pricing.md, AI-crawler robots.txt)** - Machine-readable product briefs (llms.txt, llms-full.txt, pricing.md) plus a robots.txt that explicitly allowlists named AI answer-engine and training crawlers (ChatGPT-User, Claude-SearchBot, PerplexityBot, GPTBot, ClaudeBot, etc.) rather than relying on the wildcard rule, all listed in sitemap.xml, so agents and answer engines can read and cite the product directly. - `llms.txt:1`, `robots.txt:6`, `pricing.md:1`
- **Discord community badge** - A theme-adaptive, dismissible floating widget inviting visitors to join the LunarWerx Discord server; picks a light or dark skin at runtime by measuring the page's own background luminance, shared across the whole LunarWerx fleet of sites. - `index.html:653`
- **Cross-product footer navigation** - Footer nav links out to sibling LunarWerx Studios products (RepoYeti, AgentHydra, ReDesign, SageThumbs, QuickDictate) for fleet cross-promotion. - `index.html:624`

### Where to add a new one

- **A new section or feature card** - Add a <section> with class 'wrap' and a .card or .duo-card structure; follow the existing color/icon pattern (--green, --indigo, --blue, --orange) anchors: `index.html:467`, `index.html:504`
- **Comparison with a new process manager** - Add a .card to the #compare section with an <h3>vs. [tool]</h3> and a <p> describing trade-offs anchors: `index.html:539`
- **A new FAQ question** - Add a Question/Answer pair to the FAQPage mainEntity array in the JSON-LD schema markup anchors: `index.html:343`
- **Update version or product info** - Edit softwareVersion in JSON-LD schema (index.html:300); update VERSION file; mirror in pricing.md:17 anchors: `index.html:300`, `VERSION:1`, `pricing.md:17`

### Gaps and wants

_Withheld: this repository is public, and the gap list is not published outside the private index._
_Read it with `python odin.py codex brief devwebui-github-io` in the Odin clone._

---

_Generated by `odin codex about --publish devwebui-github-io` on 2026-09-09 from a Codex dossier stamped 2026-09-04. Regenerate after the product moves; `odin codex about` reports drift._
<!-- odin:about GENERATED END sha=b88e624610fd -->

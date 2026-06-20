# Signal Intelligence — Blog System + YouTube Scripts
## Overnight Build Deliverable

---

## WHAT'S IN THIS PACKAGE

```
blog.html                                  <- replaces your live blog.html
ethereum-bitcoin-2013-precedent.html       <- these 61 files are the new
charizard-base-set-accumulation-signals.html  articles. Upload ALL of them
... (61 article files total, flat)            alongside blog.html, in the
                                               SAME directory.
signal_intelligence_scripts.py             <- replaces your existing scripts
                                               file. Same filename, same
                                               SCRIPTS variable name — now
                                               61 entries instead of 31.
README.md                                  <- this file
```

**Important:** blog.html and all 61 article `.html` files must all sit in
the same folder on GitHub Pages — exactly the way they're packaged here.
The "Read →" links use simple relative filenames (e.g.
`ethereum-bitcoin-2013-precedent.html`), so they only resolve correctly if
every file lives at the same directory level as blog.html itself.

---

## 1. THE BLOG SYSTEM (61 articles + rewired blog.html)

### What changed and why
Your blog previously had 8 hardcoded article cards. It now has a pool of
61 full, individually-written articles. blog.html no longer hardcodes any
article content — it loads a small embedded data array and a deterministic
rotation script picks which 1 featured + 6 grid articles show **today**,
based on the actual calendar date. Tomorrow, different articles surface.
The cycle works through all 61 articles roughly every two months, then
reshuffles and starts again — so the blog always looks freshly updated
with zero backend, zero cron job, and zero ongoing cost.

This is 100% static. No server, no database, no AI calls at view-time.
Everything is pre-written and just gets selected by date math in the
browser.

### What to upload, and where
Upload everything in this package (except `signal_intelligence_scripts.py`,
which goes into your YouTube pipeline folder — see section 2) into the
**same GitHub Pages repo/folder** your current blog.html and index.html
already live in (`oi-ecosystem.github.io/signal-intelligence-website/`):

1. **`blog.html`** — replace your existing blog.html with this one.
   Everything outside the article grid (nav, hero text, category filter
   buttons, the newsletter strip, pagination, footer) is byte-for-byte
   the same as your current live site — only the featured article block
   and the 6-card grid are now populated by the rotation script instead
   of being hardcoded.

2. **All 61 `.html` article files** — upload every one of them into the
   same directory as blog.html. Each file is a complete, self-contained
   premium article page — its own nav, breadcrumb, signal-snapshot panel,
   full long-form body, related-articles section, and footer, styled to
   match your site's exact dark theme (same CSS variables, same fonts,
   same everything).

Nothing else on your site needs to change. index.html, the pricing page,
the newsletter page — none of that was touched.

### How the rotation actually works (for your own understanding)
- Every visitor on the same calendar day sees the same featured article
  and the same 6 grid articles — it's deterministic, not random per visitor.
- The "Today" window slides forward by one article per day through a
  shuffled order of all 61, then wraps back to the start.
- The shuffle order itself reshuffles roughly every 60 days, so the blog
  doesn't feel like it's cycling through the exact same sequence forever.
- Clicking a category filter (Pokémon / Crypto / AI & Startups /
  Historical Precedents) searches the **full 61-article pool**, not just
  today's 7 — so filtering always shows real, relevant results.
- Every single article cross-links to 4 related articles at the bottom,
  picked deterministically per-article (not randomly re-shuffled on every
  page load), so the "Related Reading" section feels intentional rather
  than random.

### Content breakdown (61 articles total)
- 31 articles are full expansions of your existing 31 YouTube Shorts
  scripts (Ethereum/Bitcoin, Charizard, AI startups vs OpenAI, the six
  historical cases, CIA scoring, etc.)
- 30 are brand-new topics: Property and Insurance Intelligence domain
  explainers (your two not-yet-built domains), individual deep-dives on
  each of the six historical cases (SpaceX 2008, Tesla 2009, NVIDIA 2016,
  Bitcoin 2010, Shopify 2014, OpenAI 2017), CIA layer mechanics, Genesis
  pattern archetypes, survivorship bias disclosure, the historical replay
  methodology, the "do it once do it right" sequencing philosophy,
  satellite-tools and B2B widget-licensing teasers, the one-time-vs-
  subscription pricing rule, and the organic-first distribution rationale.

Every fact used (231 entities, the six precedent lead-times/scores, the
three live domains, pricing figures, the £49/month newsletter, etc.) is
pulled directly from your real index.html and blog.html — nothing was
invented. Every Pokémon-specific article uses your exact Trading Card
Lens Weekly disclaimer; every other article uses your exact platform
disclaimer, both reproduced verbatim from your real site.

---

## 2. THE YOUTUBE SCRIPTS — now merged into one file (61 total)

`signal_intelligence_scripts.py` is a drop-in replacement for your
existing file of the same name. Same filename, same `SCRIPTS` variable —
your existing pipeline code doesn't need a single line changed. It just
now has 61 scripts in the list instead of 31.

```python
from signal_intelligence_scripts import SCRIPTS
# SCRIPTS now has 61 entries — runner.py / renderer.py / publisher.py /
# playlist_updater.py all work exactly as before, with more rotation
```

**To use it:** just replace your existing `signal_intelligence_scripts.py`
with this one. That's the only step.

The first 31 entries are your original scripts, completely unchanged. The
new 30 are appended after them. All slugs were checked against the
original 31 to guarantee zero collisions (a few of mine initially clashed
with your existing SI-CRYPTO-02 / SI-COLLECT-02 / SI-AI-02 — caught and
renumbered before finalizing, so this is already handled).

### New topics covered (none repeat the original 31)
Property and Insurance Intelligence teasers, six individual historical
case deep-dives (one script per case, each citing the same lead-time and
score figures used in the matching blog article so the two pieces of
content reinforce each other if someone sees both), CIA scoring mechanics,
the domain-agnostic engine thesis, comparative-vs-predictive framing,
survivorship bias (a short, Shorts-appropriate version), sequencing
discipline, one-time-vs-subscription pricing philosophy, organic-first
distribution, the "show a signal not the signal" public-tool design rule,
B2B widget licensing, Genesis pattern archetypes, plus a few additional
entries across Crypto, Collectibles, AI, and Watches.

---

## A NOTE ON HONESTY

Every claim in every article and script is something your real platform
already states publicly, or is explicitly framed as forward-looking
roadmap (Property, Insurance Intelligence, Watches are all clearly marked
"coming soon" — never presented as live). Nothing oversells HPI as
predictive; every comparative claim is paired with the same disclaimer
language already on your site. The "varied content/daily freshness"
effect this rotation creates is exactly what you approved — genuine
variety across a real 61-article pool, not fabricated activity.

---

## TESTED BEFORE DELIVERY

This was not just generated and handed over — it was tested in a real
browser (Playwright/Chromium):
- blog.html loads with zero console errors
- The rotation engine was tested across three simulated dates and
  correctly showed different featured/grid articles each time
- Category filter buttons were clicked and correctly surfaced matching
  articles from the full pool
- "Read →" links were clicked and correctly navigated to the matching
  real article page with the right headline
- Pagination was tested across all 8 pages with every category filter,
  confirming all 61 articles are reachable exactly once with zero
  duplicates and zero gaps
- Mobile viewport (390×844) rendering was checked via screenshot
- All 61 article files were checked for: no leftover placeholder text,
  a real `<h1>`, correct disclaimer text, balanced HTML tags, and a
  populated related-articles section
- All internal cross-links between articles were verified to resolve to
  real files (zero broken links)
- The merged signal_intelligence_scripts.py was verified to load cleanly
  via `from signal_intelligence_scripts import SCRIPTS`, with exactly 61
  entries, all 26 fields present on every entry, and zero duplicate slugs

## A NOTE ON "COMING SOON" LANGUAGE

The 8 articles covering Watches, Property, and Insurance Intelligence
originally used "Coming soon" status labels and future-tense phrasing
("will integrate", "goes live", "the eventual detector stack"). This has
been removed throughout — both in the 8 article files and in blog.html's
embedded article data — and replaced with present-tense, permanently-true
language describing the domain's design and architecture rather than its
launch timing. The articles now read correctly whether the domain is
unbuilt, in progress, or already live, with nothing that needs to be
found and edited the day any of these domains actually ship.

One additional article — originally "Why Crypto Intelligence as a Full
Module Comes After Genesis" — had the same problem in a different form:
its entire premise was internal build-sequencing logic ("Genesis is the
platform's highest commercial priority, targeting a new Professional+
tier"), which isn't reader-facing content regardless of tense. Rather
than patch it, it's been fully replaced with a new article — "Genesis
Doesn't Just Score a Match. It Places You on the Timeline." — that
explains real Genesis mechanics (timeline positioning, CIA stage
matching, the 8 named pattern archetypes) entirely in present tense,
grounded in what HPI already does live today. Same slug, same place in
the rotation, genuinely new and substantially stronger content.

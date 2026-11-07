#!/usr/bin/env python3
"""Rebuild the signal333.com blog listing and sitemap from _bot/posts.json.

Run from the repository root:  python3 _bot/build_blog.py
- blog.html: the featured article (newest) and every other article as a static
  card (newest first, real dates), so search engines can see every article.
  Filters and pagination run in a small script on the page.
- sitemap.xml: every page and every article on https://signal333.com.
Nothing else on the page is changed. Not published (Jekyll skips _ folders).
"""
import html, json, os, re, sys
from datetime import datetime, timezone

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "https://signal333.com"
posts = json.load(open(os.path.join(ROOT, "_bot", "posts.json"), encoding="utf-8"))
for p in posts:
    for k in ("slug", "title", "date", "filterBucket", "excerpt", "tags", "snapItems"):
        if k not in p:
            sys.exit(f"posts.json: {p.get('slug')} is missing {k}")
    if not os.path.exists(os.path.join(ROOT, "blog_articles", p["slug"] + ".html")):
        sys.exit(f"posts.json: blog_articles/{p['slug']}.html does not exist")
posts.sort(key=lambda p: p["date"], reverse=True)  # stable: same-day order kept


def nice(d):
    return datetime.strptime(d, "%Y-%m-%d").strftime("%-d %b %Y")


def tags(p):
    return "".join(f'<span class="tag {t["cls"]}">{t["label"]}</span>' for t in p["tags"])


def snaps(p):
    out = []
    for it in p["snapItems"]:
        cls = "snap-match" if it.get("cls") == "accent" else "snap-val"
        out.append(f'<div><div class="snap-label">{it["label"]}</div><div class="{cls}">{it["val"]}</div></div>')
    return "".join(out)


feat = posts[0]
featured = f'''<!-- SI:FEATURED:START (built by _bot/build_blog.py: newest article) -->
    <div class="featured-meta" id="si-featured-meta">{tags(feat)}<span>{nice(feat["date"])}</span></div>
    <div class="featured-title" id="si-featured-title"><a href="blog_articles/{feat["slug"]}.html">{feat["title"]}</a></div>
    <div class="featured-excerpt" id="si-featured-excerpt">{feat["excerpt"]}</div>
    <a href="blog_articles/{feat["slug"]}.html" class="read-link" id="si-featured-link">Read full analysis →</a>
    <!-- SI:FEATURED:END -->'''

cards = []
for p in posts[1:]:
    cards.append(f'''  <div class="article-card" data-bucket="{p["filterBucket"]}">
    <div class="article-tags">{tags(p)}</div>
    <div class="article-title"><a href="blog_articles/{p["slug"]}.html">{p["title"]}</a></div>
    <div class="signal-snap">{snaps(p)}</div>
    <div class="article-excerpt">{p["excerpt"]}</div>
    <div class="article-meta"><time datetime="{p["date"]}">{nice(p["date"])}</time><a href="blog_articles/{p["slug"]}.html" class="read-link">Read →</a></div>
  </div>''')
grid = "<!-- SI:GRID:START (built by _bot/build_blog.py: all other articles, newest first) -->\n" + "\n".join(cards) + "\n<!-- SI:GRID:END -->"

path = os.path.join(ROOT, "blog.html")
s = open(path, encoding="utf-8").read()
for name, block in (("FEATURED", featured), ("GRID", grid)):
    new, n = re.subn(rf"<!-- SI:{name}:START.*?<!-- SI:{name}:END -->", lambda m: block, s, flags=re.S)
    if n != 1:
        sys.exit(f"blog.html: SI:{name} markers not found exactly once")
    s = new
open(path, "w", encoding="utf-8").write(s)

# sitemap
pages = ["", "blog.html", "historical-cases.html", "historical-validation-framework.html", "lenses.html",
         "genesis.html", "newsletter.html", "contact.html", "terms.html", "privacy.html", "disclaimer.html"]
pages = [p for p in pages if p == "" or os.path.exists(os.path.join(ROOT, p))]
today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
urls = []
for p in pages:
    pri = "1.0" if p == "" else ("0.9" if p == "blog.html" else "0.6")
    freq = "daily" if p == "blog.html" else "monthly"
    lm = f"\n    <lastmod>{today}</lastmod>" if p == "blog.html" else ""
    urls.append(f"  <url>\n    <loc>{SITE}/{p}</loc>{lm}\n    <changefreq>{freq}</changefreq>\n    <priority>{pri}</priority>\n  </url>")
for p in posts:
    urls.append(f"  <url>\n    <loc>{SITE}/blog_articles/{p['slug']}.html</loc>\n    <lastmod>{p['date']}</lastmod>\n    <changefreq>monthly</changefreq>\n    <priority>0.7</priority>\n  </url>")
open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8").write(
    '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "\n".join(urls) + "\n</urlset>\n")
print(f"built: {len(posts)} articles, featured {feat['slug']} ({feat['date']})")

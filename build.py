"""Bouwt robertriteco.nl: content.py + static/ -> public/ (alleen standaardbibliotheek).

    python build.py
Lokaal bekijken:  python -m http.server 8780 -d public
"""
import html
import shutil
from pathlib import Path

from content import ARTICLES, CONTACT, PROJECTS, SITE, UI

ROOT = Path(__file__).parent
OUT = ROOT / "public"
FONTS = ("https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..125,500..800"
         "&family=IBM+Plex+Mono:wght@500&family=Public+Sans:wght@400;600;700&display=swap")

e = html.escape


def mark():
    return ('<svg viewBox="0 0 44 28" aria-hidden="true"><defs><clipPath id="mk"><circle cx="15" cy="14" r="12"/></clipPath></defs>'
            '<circle cx="15" cy="14" r="12" fill="none" stroke="currentColor" stroke-width="2"/>'
            '<circle cx="29" cy="14" r="12" fill="none" stroke="currentColor" stroke-width="2"/>'
            '<circle cx="29" cy="14" r="12" clip-path="url(#mk)" fill="var(--accent)"/></svg>')


def venn(t):
    return (f'<svg class="venn" viewBox="0 0 360 230" role="img" aria-label="{e(t["venn_alt"])}">'
            '<defs><clipPath id="vn"><circle cx="130" cy="115" r="100"/></clipPath></defs>'
            '<circle class="ring" cx="130" cy="115" r="100"/><circle class="ring" cx="230" cy="115" r="100"/>'
            '<circle class="lens" cx="230" cy="115" r="100" clip-path="url(#vn)"/>'
            f'<text x="80" y="121" text-anchor="middle">{e(t["venn_data"])}</text>'
            f'<text x="280" y="121" text-anchor="middle">{e(t["venn_ai"])}</text>'
            f'<text class="mono" x="180" y="119" text-anchor="middle">{e(t["venn_tools"])}</text></svg>')


def shot(lang, p, cls="shot"):
    return (f'<img class="{cls}" src="/img/{p["shot"]}" alt="{e(p[lang]["shot_alt"])}" '
            f'width="{p["shot_w"]}" height="{p["shot_h"]}" loading="lazy" decoding="async">')


def proj_path(lang, slug):
    return UI[lang]["paths"]["projects"] + slug + "/"


def page(lang, path, alt_path, title, desc, body, current=""):
    t = UI[lang]
    nav = "".join(
        f'<a href="{t["paths"][k]}"{" aria-current=\"page\"" if k == current else ""}>{e(t["nav"][k])}</a>'
        for k in ("projects", "collab", "thoughts")
    )
    other = "en" if lang == "nl" else "nl"
    full_title = title if title == "Robert Riteco" else f"{title} · Robert Riteco"
    canon = SITE["domain"] + path
    alt = SITE["domain"] + alt_path
    return f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(full_title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{canon}">
<link rel="alternate" hreflang="{lang}" href="{canon}">
<link rel="alternate" hreflang="{other}" href="{alt}">
<meta property="og:title" content="{e(full_title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:type" content="website">
<meta property="og:url" content="{canon}">
<meta property="og:image" content="{SITE["domain"]}/og.png">
<meta name="twitter:card" content="summary_large_image">
<meta name="color-scheme" content="light dark">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="{FONTS}">
<link rel="stylesheet" href="/style.css">
</head>
<body>
<a href="#inhoud" class="mono" style="position:absolute;left:-999px" onfocus="this.style.left='8px'" onblur="this.style.left='-999px'">{e(t["skip"])}</a>
<div class="wrap">
<header class="top">
<a class="brand" href="{t["paths"]["home"]}">{mark()}Robert Riteco</a>
<nav aria-label="Menu">{nav}<a class="lang" href="{alt_path}" hreflang="{other}" lang="{other}">{e(t["other_lang"])}</a></nav>
</header>
<main id="inhoud">
{body}
</main>
<footer>
<p>{e(t["footer_made"])} {e(t["footer_unofficial"])}</p>
<p><a href="{SITE["github"]}/robertriteco-site">{e(t["footer_code"])}</a> · <a href="{SITE["github"]}">GitHub</a></p>
</footer>
</div>
</body>
</html>
"""


def status_tag(lang, p):
    return f'<span class="status {p["status"]} mono">{e(UI[lang][p["status"]])}</span>'


def card(lang, p):
    c = p[lang]
    return (f'<article class="card">{shot(lang, p)}{status_tag(lang, p)}'
            f'<h3><a href="{proj_path(lang, p["slug"])}">{e(c["name"])}</a></h3>'
            f'<p>{e(c["card"])}</p><span class="more">{e(UI[lang]["view_project"])} →</span></article>')


def contact_block(lang):
    t = UI[lang]
    rows = []
    if CONTACT["email"]:
        rows.append(f'<p><span class="mono muted">{e(t["contact_email"])}</span><br>'
                    f'<a href="mailto:{e(CONTACT["email"])}">{e(CONTACT["email"])}</a></p>')
    if CONTACT["linkedin"]:
        rows.append(f'<p><span class="mono muted">{e(t["contact_linkedin"])}</span><br>'
                    f'<a href="{e(CONTACT["linkedin"])}">{e(CONTACT["linkedin"])}</a></p>')
    if not rows:
        rows.append(f'<p class="todo">{e(t["contact_todo"])}</p>')
        print("LET OP: CONTACT in content.py is nog leeg.")
    return '<div class="contact">' + "".join(rows) + "</div>"


def home(lang):
    t = UI[lang]
    feat = next(p for p in PROJECTS if p["featured"])
    fc = feat[lang]
    others = [p for p in PROJECTS if not p["featured"]]
    stats = "".join(f"<li><b>{e(n)}</b><span>{e(l)}</span></li>" for n, l in fc["stats"])
    return f"""
<section class="hero">
<div class="hero-text">
<h1>{e(t["hero_h1"])}</h1>
<p class="lead">{e(t["hero_lead"])}</p>
<p class="muted" style="font-size:.9375rem;margin:0">{e(t["vibe_note"])}</p>
<div class="btnrow"><a class="btn fill" href="{t["paths"]["projects"]}">{e(t["hero_btn1"])}</a><a class="btn" href="{t["paths"]["collab"]}">{e(t["hero_btn2"])}</a></div>
</div>
{venn(t)}
</section>

<section class="feature" aria-labelledby="f-h">
<div class="feature-top">
<div>
<span class="tag mono">{e(t["featured"])} · {e(UI[lang][feat["status"]])}</span>
<h2 id="f-h">{e(fc["name"])}</h2>
<p style="font-size:1.15rem;margin-top:14px">{e(fc["tagline"])}</p>
<div class="btnrow" style="margin-top:22px"><a class="btn" href="{proj_path(lang, feat["slug"])}">{e(t["view_project"])}</a><a class="btn" href="{feat["url"]}">{e(t["open_live"])} ↗</a></div>
</div>
{shot(lang, feat)}
</div>
<ul class="stats">{stats}</ul>
</section>

<section aria-labelledby="m-h">
<div class="sechead"><h2 id="m-h">{e(t["more_projects"])}</h2><a href="{t["paths"]["projects"]}">{e(t["all_projects"])} →</a></div>
<div class="cards">{"".join(card(lang, p) for p in others)}</div>
</section>

<section class="two">
<div class="prose"><h2>{e(t["about_h"])}</h2></div>
<div>{"".join(f"<p>{e(x)}</p>" for x in t["about"])}</div>
</section>

<section class="two">
<div class="prose"><h2>{e(t["collab_h"])}</h2></div>
<div><p>{e(t["collab_teaser"])}</p><p><a href="{t["paths"]["collab"]}">{e(t["collab_link"])} →</a></p></div>
</section>

<section class="two">
<div class="prose"><h2>{e(t["thoughts_h"])}</h2></div>
<div><p>{e(t["thoughts_teaser"])}</p><p><a href="{t["paths"]["thoughts"]}">{e(t["thoughts_link"])} →</a></p></div>
</section>
"""


def projects_index(lang):
    t = UI[lang]
    return f"""
<section class="phead"><h1>{e(t["projects_h"])}</h1><p class="tagline">{e(t["projects_intro"])}</p></section>
<div class="cards">{"".join(card(lang, p) for p in PROJECTS)}</div>
"""


def project_page(lang, p):
    t, c = UI[lang], p[lang]
    secs = "".join(
        f'<section class="psec"><h2>{e(h)}</h2>{"".join(f"<p>{e(x)}</p>" for x in paras)}</section>'
        for h, paras in c["sections"]
    )
    facts = "".join(f"<dt>{e(k)}</dt><dd>{e(v)}</dd>" for k, v in c["facts"])
    return f"""
<section class="phead">
<p class="crumbs"><a href="{t["paths"]["projects"]}">← {e(t["back"])}</a></p>
{status_tag(lang, p)}
<h1>{e(c["name"])}</h1>
<p class="tagline">{e(c["tagline"])}</p>
</section>
{shot(lang, p)}
<div class="pbody">
<div>{secs}</div>
<aside class="facts" aria-label="{e(t["facts_h"])}">
<h3 style="margin-bottom:14px">{e(t["facts_h"])}</h3>
<dl>{facts}</dl>
<a class="btn fill" href="{p["url"]}">{e(t["open_site"])} ↗</a>
<a class="btn" href="{p["code"]}">{e(t["open_code"])} ↗</a>
</aside>
</div>
"""


def collab(lang):
    t = UI[lang]
    items = "".join(f"<li><b>{e(a)}</b> {e(b)}</li>" for a, b in t["collab_items"])
    return f"""
<section class="phead"><h1>{e(t["collab_page_h"])}</h1><p class="tagline">{e(t["collab_page_lead"])}</p></section>
<section class="two">
<div class="prose"><h2>{e(t["collab_list_h"])}</h2></div>
<ul class="ticks">{items}</ul>
</section>
<section class="two">
<div class="prose"><h2>{e(t["collab_how_h"])}</h2></div>
<div><p>{e(t["collab_how"])}</p>{contact_block(lang)}</div>
</section>
"""


def art_path(lang, slug):
    return UI[lang]["paths"]["thoughts"] + slug + "/"


def thoughts(lang):
    t = UI[lang]
    topics = "".join(f"<li>{e(x)}</li>" for x in t["thoughts_topics"])
    if ARTICLES:
        items = "".join(
            f'<article class="card" style="max-width:44rem"><span class="mono muted">{e(a[lang]["date_label"])}</span>'
            f'<h3><a href="{art_path(lang, a["slug"])}">{e(a[lang]["title"])}</a></h3>'
            f'<p>{e(a[lang]["summary"])}</p><span class="more">{e(t["read_more"])} →</span></article>'
            for a in ARTICLES)
        lead = f'<div style="display:grid;gap:20px">{items}</div>'
    else:
        lead = f'<p class="note">{e(t["thoughts_empty"])}</p>'
    return f"""
<section class="phead"><h1>{e(t["thoughts_page_h"])}</h1><p class="tagline">{e(t["thoughts_page_lead"])}</p></section>
{lead}
<section class="two">
<div class="prose"><h2>{e(t["thoughts_more_h"])}</h2></div>
<ul class="ticks">{topics}</ul>
</section>
"""


def article_page(lang, a):
    t, c = UI[lang], a[lang]
    out = []
    for kind, val in c["body"]:
        if kind == "h":
            out.append(f"<h2>{e(val)}</h2>")
        elif kind == "p":
            out.append(f"<p>{e(val)}</p>")
        else:
            out.append('<ul class="ticks">' + "".join(f"<li>{e(x)}</li>" for x in val) + "</ul>")
    return f"""
<article class="article">
<p class="crumbs"><a href="{t["paths"]["thoughts"]}">← {e(t["back_thoughts"])}</a></p>
<span class="mono muted">{e(c["date_label"])}</span>
<h1 style="margin-top:10px">{e(c["title"])}</h1>
<div class="body">{"".join(out)}</div>
</article>
"""


def sitemap(urls):
    rows = "".join(f"<url><loc>{SITE['domain']}{u}</loc></url>" for u in sorted(urls))
    return f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{rows}</urlset>\n'


def write(path, text):
    f = OUT / path.strip("/") / "index.html"
    f.parent.mkdir(parents=True, exist_ok=True)
    f.write_text(text, encoding="utf-8")


def main():
    if OUT.exists():
        shutil.rmtree(OUT)
    shutil.copytree(ROOT / "static", OUT)
    pairs = {"nl": "en", "en": "nl"}
    for lang in ("nl", "en"):
        t, o = UI[lang], UI[pairs[lang]]
        write(t["paths"]["home"], page(lang, t["paths"]["home"], o["paths"]["home"], t["title_home"], t["desc_home"], home(lang)))
        write(t["paths"]["projects"], page(lang, t["paths"]["projects"], o["paths"]["projects"], t["projects_h"], t["projects_intro"], projects_index(lang), "projects"))
        write(t["paths"]["collab"], page(lang, t["paths"]["collab"], o["paths"]["collab"], t["collab_page_h"], t["collab_page_lead"], collab(lang), "collab"))
        write(t["paths"]["thoughts"], page(lang, t["paths"]["thoughts"], o["paths"]["thoughts"], t["thoughts_page_h"], t["thoughts_page_lead"], thoughts(lang), "thoughts"))
        for p in PROJECTS:
            path, alt = proj_path(lang, p["slug"]), proj_path(pairs[lang], p["slug"])
            write(path, page(lang, path, alt, p[lang]["name"], p[lang]["tagline"], project_page(lang, p), "projects"))
        for a in ARTICLES:
            path, alt = art_path(lang, a["slug"]), art_path(pairs[lang], a["slug"])
            write(path, page(lang, path, alt, a[lang]["title"], a[lang]["summary"], article_page(lang, a), "thoughts"))
    urls = []
    for f in OUT.rglob("index.html"):
        rel = f.parent.relative_to(OUT).as_posix()
        urls.append("/" if rel == "." else f"/{rel}/")
    (OUT / "sitemap.xml").write_text(sitemap(urls), encoding="utf-8")
    (OUT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {SITE['domain']}/sitemap.xml\n", encoding="utf-8")
    print("klaar:", sum(1 for _ in OUT.rglob("*.html")), "pagina's in", OUT)


if __name__ == "__main__":
    main()

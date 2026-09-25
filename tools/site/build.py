#!/usr/bin/env python3
"""Build the Spark Media marketing site into static HTML (GitHub Pages, no build step on the server).

    python3 tools/site/build.py

Edit copy here or in tools/site/content.py, run the script, and commit the generated HTML.
Legal page bodies are kept verbatim in tools/site/legal/*.html.
"""
import html
import json
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from content import (  # noqa: E402
    SERVICES, SOLUTIONS, HOME, SERVICES_PAGE, SOLUTIONS_PAGE, INDUSTRIES_PAGE, ABOUT_PAGE, CONTACT_PAGE, PAGE_MEDIA,
)
from icons import icon  # noqa: E402

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
SITE = "https://sparkmedia.ai"
BRAND = "Spark Media"
ASSET_V = "2"
OG_IMAGE = f"{SITE}/assets/images/og-image.png"

FOOTER_DESC = ("Spark Media combines marketing, creative, AI and business systems to help companies "
               "attract customers, respond faster and work smarter.")

e = html.escape


def arrow():
    return icon("arrow")


# ---------------------------------------------------------------- layout

def nav_dropdown(label, key, items, all_href, all_label, current):
    links = "".join(
        f'<a href="{it["href"]}"><span class="d-icon">{icon(it["icon"])}</span>'
        f'<strong>{e(it["nav"])}</strong><small>{e(it["blurb"])}</small></a>'
        for it in items
    )
    cur = " current" if current == key else ""
    return (
        f'<li class="nav-item" data-dropdown>'
        f'<button class="nav-link{cur}" type="button" aria-expanded="false" aria-controls="dd-{key}">{label}{icon("chev", "chev")}</button>'
        f'<div class="dropdown" id="dd-{key}">{links}<a class="d-all" href="{all_href}">{all_label}</a></div>'
        f"</li>"
    )


def header(current):
    def top(href, label, key):
        cur = ' aria-current="page"' if current == key else ""
        return f'<li class="nav-item"><a class="nav-link" href="{href}"{cur}>{label}</a></li>'

    desktop = (
        '<nav class="nav" aria-label="Primary"><ul class="nav-list">'
        + nav_dropdown("Services", "services", SERVICES, "/services/", "View all services", current)
        + nav_dropdown("Solutions", "solutions", SOLUTIONS, "/solutions/", "View all solutions", current)
        + top("/industries/", "Industries", "industries")
        + top("/about/", "About", "about")
        + top("/contact/", "Contact", "contact")
        + "</ul></nav>"
    )

    def group(label, items, all_href):
        links = "".join(f'<a href="{it["href"]}">{e(it["nav"])}</a>' for it in items)
        return (f"<details><summary>{label}{icon('chev')}</summary>"
                f'<a href="{all_href}">Overview</a>{links}</details>')

    mobile = (
        '<nav class="mobile-nav" id="mobile-nav" aria-label="Mobile">'
        + group("Services", SERVICES, "/services/")
        + group("Solutions", SOLUTIONS, "/solutions/")
        + '<a href="/industries/">Industries</a><a href="/about/">About</a><a href="/contact/">Contact</a>'
        + f'<a class="btn btn-primary" href="/contact/">Let’s Talk {arrow()}</a>'
        + "</nav>"
    )
    return (
        '<header class="site-header" data-header><div class="wrap header-inner">'
        f'<a class="brand" href="/" aria-label="{BRAND} home"><img src="/assets/logo/sparkmedia-logo-light.png" alt="{BRAND}" width="600" height="159"></a>'
        + desktop
        + f'<a class="btn btn-primary btn-sm header-cta" href="/contact/">Let’s Talk</a>'
        '<button class="menu-btn" type="button" aria-expanded="false" aria-controls="mobile-nav" aria-label="Open menu" data-menu>'
        f'{icon("menu", "i-open")}{icon("close", "i-close")}</button>'
        "</div></header>"
        + mobile
    )


def footer():
    svc = "".join(f'<li><a href="{s["href"]}">{e(s["nav"])}</a></li>' for s in SERVICES)
    sol = "".join(f'<li><a href="{s["href"]}">{e(s["nav"])}</a></li>' for s in SOLUTIONS)
    return f"""<footer class="site-footer">
  <section class="footer-cta" aria-labelledby="footer-cta-h">
    <div class="wrap">
      <div>
        <h2 id="footer-cta-h">Good marketing should connect to what happens next.</h2>
        <p>Tell us where your customer journey breaks down. We’ll help you find a practical way to connect the pieces.</p>
      </div>
      <div class="btn-row"><a class="btn btn-light" href="/contact/">Start a Conversation {arrow()}</a></div>
    </div>
  </section>
  <div class="wrap">
    <div class="footer-main">
      <div class="footer-brand">
        <a href="/" aria-label="{BRAND} home"><img src="/assets/logo/sparkmedia-logo-white.png" alt="{BRAND}" width="600" height="159" loading="lazy"></a>
        <p>{e(FOOTER_DESC)}</p>
      </div>
      <div class="footer-cols">
        <div class="footer-col"><h3>Services</h3><ul><li><a href="/services/">All services</a></li>{svc}</ul></div>
        <div class="footer-col"><h3>Solutions</h3><ul><li><a href="/solutions/">All solutions</a></li>{sol}</ul></div>
        <div class="footer-col"><h3>Company</h3><ul>
          <li><a href="/industries/">Industries</a></li>
          <li><a href="/about/">About</a></li>
          <li><a href="/contact/">Contact</a></li>
          <li><a href="/book.html">Book a conversation</a></li>
        </ul></div>
      </div>
    </div>
    <div class="footer-legal">
      <div>
        <p>SparkMedia.ai is a DBA of McCormick Solutions, LLC · 8690 Lloyd Ct, Las Vegas, NV 89145</p>
        <p><a href="tel:+17023341443">(702) 334-1443</a> · <a href="mailto:dave@sparkmedia.ai">dave@sparkmedia.ai</a></p>
      </div>
      <div class="row">
        <a href="/privacy.html">Privacy Policy</a>
        <a href="/terms.html">Terms &amp; Conditions</a>
        <span>© <span data-year>2026</span> SparkMedia.ai. All rights reserved.</span>
      </div>
    </div>
  </div>
</footer>"""


def page(path, title, desc, body, current=None, canonical=None, extra_head="", jsonld=None, noindex=False, dark_header=False):
    canonical = canonical or (SITE + path)
    ld = f'<script type="application/ld+json">{json.dumps(jsonld, separators=(",", ":"))}</script>' if jsonld else ""
    robots = '<meta name="robots" content="noindex">' if noindex else ""
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{e(title)}</title>
  <meta name="description" content="{e(desc)}">
  <link rel="canonical" href="{canonical}">
  {robots}
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="{BRAND}">
  <meta property="og:title" content="{e(title)}">
  <meta property="og:description" content="{e(desc)}">
  <meta property="og:url" content="{canonical}">
  <meta property="og:image" content="{OG_IMAGE}">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="theme-color" content="#FFFFFF">
  <link rel="icon" href="/assets/logo/favicon-32x32.png" type="image/png">
  <link rel="apple-touch-icon" href="/assets/logo/apple-touch-icon.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&amp;family=Plus+Jakarta+Sans:wght@600;700;800&amp;display=swap" rel="stylesheet">
  <link rel="stylesheet" href="/css/site.css?v={ASSET_V}">
  <script>document.documentElement.classList.add('js')</script>
  {extra_head}{ld}
</head>
<body{' class="home-page"' if dark_header else ""}>
  <a class="skip" href="#main">Skip to content</a>
  {header(current)}
  <main id="main">
{body}
  </main>
  {footer()}
  <script src="/js/site.js?v={ASSET_V}" defer></script>
</body>
</html>
"""


def write(rel, content):
    out = os.path.join(ROOT, rel)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w") as f:
        f.write(content)
    print("wrote", rel)


# ---------------------------------------------------------------- components

def btn(label, href, kind="primary", arrow_icon=True):
    return f'<a class="btn btn-{kind}" href="{href}">{e(label)}{" " + arrow() if arrow_icon else ""}</a>'


def crumbs(items):
    lis = "".join(
        f'<li><a href="{h}">{e(l)}</a></li>' if h else f'<li aria-current="page">{e(l)}</li>' for l, h in items
    )
    return f'<ol class="crumbs" aria-label="Breadcrumb">{lis}</ol>'


def page_hero(eyebrow, h1, intro, trail=None, buttons="", media=None):
    split = " has-media" if media else ""
    return f"""    <section class="page-hero{split}">
      <div class="wrap page-hero-grid">
        <div class="page-hero-copy">
          {crumbs(trail) if trail else ""}
          <p class="eyebrow">{e(eyebrow)}</p>
          <h1>{e(h1)}</h1>
          <p class="lede">{e(intro)}</p>
          {f'<div class="btn-row">{buttons}</div>' if buttons else ""}
        </div>
        {hero_media(media)}
      </div>
    </section>"""


def paras(text):
    parts = text if isinstance(text, list) else [text]
    return "".join(f"<p>{e(p)}</p>" for p in parts)


def checklist(items):
    return '<ul class="checklist">' + "".join(f"<li>{e(i)}</li>" for i in items) + "</ul>"


def closing(h, copy, cta_label, cta_href="/contact/", secondary=None):
    sec = btn(secondary[0], secondary[1], "ghost-light", False) if secondary else ""
    return f"""    <section class="section">
      <div class="wrap">
        <div class="closing reveal">
          {img_tag("abs-ribbons.jpg", "", cls="closing-bg")}
          <div class="closing-inner">
            <h2>{e(h)}</h2>
            {f"<p>{e(copy)}</p>" if copy else ""}
            <div class="btn-row">{btn(cta_label, cta_href, "light")}{sec}</div>
          </div>
        </div>
      </div>
    </section>"""


def related(title, items):
    links = "".join(f'<a href="{it["href"]}">{e(it["nav"])}{arrow()}</a>' for it in items)
    return f'<h2 class="related-title">{e(title)}</h2><div class="related">{links}</div>'


def img_tag(src, alt, w=1536, h=1024, lazy=True, cls=""):
    c = f' class="{cls}"' if cls else ""
    load = ' loading="lazy"' if lazy else ' fetchpriority="high"'
    return f'<img{c} src="/assets/images/site/{src}" width="{w}" height="{h}" alt="{e(alt)}"{load} decoding="async">'


def hero_media(m):
    if not m:
        return ""
    if m.get("abstract"):
        return f'<div class="hero-media hero-media-abstract" aria-hidden="true">{img_tag(m["img"], "", lazy=False)}</div>'
    chips = "".join(
        f'<div class="chip chip-{i + 1}"><span class="n-icon">{icon(c[0])}</span><span>{e(c[1])}<small>{e(c[2])}</small></span></div>'
        for i, c in enumerate(m.get("chips", []))
    )
    return (f'<div class="hero-media"><div class="hero-photo">{img_tag(m["img"], m["alt"], lazy=False)}</div>'
            f'<div aria-hidden="true">{chips}</div></div>')


def image_band(img, h, p, eyebrow=None):
    eb = f'<p class="eyebrow">{e(eyebrow)}</p>' if eyebrow else ""
    return f"""    <section class="band">
      {img_tag(img, "", cls="band-bg")}
      <div class="wrap band-inner reveal">{eb}<h2>{e(h)}</h2><p>{e(p)}</p></div>
    </section>"""


def related_cards(title, items):
    cards = "".join(
        f'<a class="mini-card" href="{it["href"]}">{img_tag(PAGE_MEDIA[it["key"]]["img"], "")}<span><strong>{e(it["nav"])}</strong><small>{e(it.get("summary", ""))}</small></span>{arrow()}</a>'
        for it in items
    )
    return f'<h2 class="related-title">{e(title)}</h2><div class="mini-cards">{cards}</div>'


# ---------------------------------------------------------------- pages

def build_home():
    h = HOME
    card_imgs = ["svc-web.jpg", "svc-ads.jpg", "svc-ai.jpg", "svc-integration.jpg"]
    card_links = ["/services/websites-branding/", "/services/paid-media/", "/services/ai-agents-automation/", "/services/ai-consulting-integration/"]
    cards = "".join(
        f"""<a class="card card-media reveal" href="{card_links[i]}"><div class="card-img"><div class="card-img-clip">{img_tag(card_imgs[i], "")}</div><span class="icon-tile">{icon(c["icon"])}</span></div><div class="card-body"><h3>{e(c["title"])}</h3><p>{e(c["body"])}</p><span class="link-arrow">Learn more {arrow()}</span></div></a>"""
        for i, c in enumerate(h["cards"])
    )
    journey = "".join(
        f'<li class="reveal"><span class="j-dot">{icon(j[0])}</span><div><strong>{e(j[1])}</strong><span>{e(j[2])}</span></div></li>'
        for j in h["journey"]
    )
    steps = "".join(f'<li class="step reveal"><h3>{e(s[0])}</h3><p>{e(s[1])}</p></li>' for s in h["steps"])
    tools = "".join(
        f'<span class="tool{(" " + t[1]) if t[1] else ""}"><i></i>{e(t[0])}</span>' for t in h["tools"]
    )
    ticker_items = [s["nav"] for s in SERVICES] + [s["nav"] for s in SOLUTIONS]
    ticker = "".join(f"<span>{e(t)}</span>" for t in ticker_items * 2)
    inds = INDUSTRIES_PAGE["items"]
    bento = "".join(
        f"""<a class="bento-item b{i + 1} reveal" href="/industries/">{img_tag(it["img"], it["alt"])}<span class="bento-cap"><small>{e(it["eyebrow"])}</small>{e(it["title"])}</span></a>"""
        for i, it in enumerate(inds)
    )

    body = f"""    <section class="hero hero-dark">
      {img_tag("abs-network.jpg", "", lazy=False, cls="hero-bg")}
      <div class="wrap hero-grid">
        <div>
          <p class="eyebrow">{e(h["eyebrow"])}</p>
          <h1>Make every part of your business <span class="grad-text">work together.</span></h1>
          <p class="lede">{e(h["body"])}</p>
          <div class="btn-row">{btn("Let’s Talk About Your Business", "/contact/", "light")}{btn("Explore What We Do", "/services/", "ghost-light", False)}</div>
        </div>
        {system_diagram()}
      </div>
    </section>

    <div class="ticker" aria-hidden="true"><div class="ticker-track">{ticker}</div></div>

    <section class="section">
      <div class="wrap split split-top">
        <div class="reveal">
          <p class="eyebrow">Why it matters</p>
          <h2>{e(h["intro_h2"])}</h2>
          <div class="intro-art reveal">{img_tag("abs-glass.jpg", "")}</div>
        </div>
        <div class="prose lede reveal">{paras(h["intro_body"])}</div>
      </div>
    </section>

    <section class="section section-soft">
      <div class="wrap">
        <div class="section-head reveal">
          <p class="eyebrow">What we do</p>
          <h2>{e(h["what_h2"])}</h2>
        </div>
        <div class="grid grid-4 reveal-group">{cards}</div>
        <p style="margin-top:32px" class="reveal"><a class="link-arrow" href="/services/">Explore Our Services {arrow()}</a></p>
      </div>
    </section>

    <section class="section">
      <div class="wrap split split-wide">
        <div>
          <div class="reveal">
            <p class="eyebrow">How the pieces connect</p>
            <h2>{e(h["connect_h2"])}</h2>
            <div class="prose lede" style="margin-top:20px">{paras(h["connect_body"])}</div>
            <div class="btn-row" style="margin-top:28px">{btn("See Our Solutions", "/solutions/", "secondary")}</div>
          </div>
          <div class="photo photo-frame photo-accent reveal" style="margin-top:40px;aspect-ratio:3/2">
            {img_tag("journey.jpg", "A business owner checks a phone next to a laptop showing a simple sales dashboard")}
          </div>
        </div>
        <div class="journey-card reveal">
          <ol class="journey">{journey}</ol>
          <p class="caption-note">An illustrative example of a connected customer journey, not a claim about a specific result.</p>
        </div>
      </div>
    </section>

    <section class="section section-dark">
      {img_tag("abs-blocks.jpg", "", cls="section-bg")}
      <div class="wrap stack-grid">
        <div class="reveal">
          <p class="eyebrow">The disconnected stack</p>
          <h2>{e(h["stack_h2"])}</h2>
          <div class="prose lede" style="margin-top:20px">{paras(h["stack_body"])}</div>
          <div class="btn-row" style="margin-top:30px">{btn("Connect My Systems", "/solutions/connect-your-systems/", "light")}</div>
        </div>
        <div class="reveal stack-panel">
          <div class="tool-cloud" aria-label="Examples of tools a growing business may use">{tools}</div>
          <div class="stack-legend" aria-hidden="true">
            <span><i style="background:#C4B1FF"></i>Connected</span>
            <span><i style="background:#4B5373"></i>Works on its own</span>
            <span><i style="background:#E3407F"></i>Handoff breaks</span>
          </div>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="wrap">
        <div class="section-head reveal">
          <p class="eyebrow">Who we work with</p>
          <h2>Different businesses. Connected thinking.</h2>
          <p class="lede">Venues, B2B companies, healthcare and wellness practices, and local service businesses each have their own buying journey. We build around yours.</p>
        </div>
        <div class="bento">{bento}</div>
        <p style="margin-top:28px" class="reveal"><a class="link-arrow" href="/industries/">Explore industries {arrow()}</a></p>
      </div>
    </section>

    <section class="section section-soft">
      <div class="wrap">
        <div class="section-head reveal">
          <p class="eyebrow">Our approach</p>
          <h2>{e(h["approach_h2"])}</h2>
        </div>
        <ol class="steps steps-line reveal-group">{steps}</ol>
      </div>
    </section>

{closing(h["close_h2"], h["close_body"], "Start a Conversation")}"""

    ld = {
        "@context": "https://schema.org",
        "@type": "Organization",
        "name": BRAND,
        "legalName": "McCormick Solutions, LLC",
        "url": SITE + "/",
        "logo": SITE + "/assets/logo/sparkmedia-logo-light.png",
        "description": "Spark Media connects marketing, AI and business systems so companies can attract customers, respond faster and work smarter.",
        "email": "dave@sparkmedia.ai",
        "telephone": "+1-702-334-1443",
        "address": {"@type": "PostalAddress", "streetAddress": "8690 Lloyd Ct", "addressLocality": "Las Vegas",
                    "addressRegion": "NV", "postalCode": "89145", "addressCountry": "US"},
    }
    write("index.html", page("/", "Spark Media | Marketing, AI & Connected Business Systems",
                             "Websites, advertising, AI agents and connected business systems built to turn more opportunities into customers.",
                             body, current="home", jsonld=ld, dark_header=True))


def system_diagram():
    # Nodes around a hub; coordinates are percentages of a square.
    nodes = [
        ("ads", "Ads", "Google · Meta", 20, 14, "p1"),
        ("web", "Website", "Landing pages", 80, 12, ""),
        ("phone", "Phone & text", "Calls · SMS", 90, 50, "p2"),
        ("calendar", "Scheduling", "Bookings", 80, 88, ""),
        ("crm", "CRM", "Pipeline", 22, 86, "p3"),
        ("chart", "Reporting", "What’s working", 9, 50, "p4"),
    ]
    paths, spans = [], []
    for i, (ic, label, sub, x, y, pulse) in enumerate(nodes):
        cx, cy = 50, 50
        mx, my = (x + cx) / 2 + (6 if i % 2 else -6), (y + cy) / 2
        d = f"M{x} {y} Q{mx} {my} {cx} {cy}"
        paths.append(f'<path d="{d}"/><path class="flow d{(i % 4) + 1}" d="{d}"/>')
        cls = f"node pulse {pulse}" if pulse else "node"
        spans.append(
            f'<div class="{cls}" style="left:{x}%;top:{y}%"><span class="n-icon">{icon(ic)}</span><span>{label}<small>{sub}</small></span></div>'
        )
    return f"""<div class="system" role="img" aria-label="Diagram: ads, website, phone and text, scheduling, CRM and reporting all connected through one system">
          <svg class="links" viewBox="0 0 100 100" preserveAspectRatio="none" aria-hidden="true">
            <defs><linearGradient id="flowGrad" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#E3407F"/><stop offset="1" stop-color="#6A36E8"/></linearGradient></defs>
            {"".join(paths)}
          </svg>
          <div class="hub" aria-hidden="true"><div><strong>One connected<br>system</strong><span>AI + automation</span></div></div>
          <div aria-hidden="true">{"".join(spans)}</div>
        </div>"""


def build_services():
    p = SERVICES_PAGE
    cards = "".join(
        f"""<a class="card card-media reveal" href="{s["href"]}"><div class="card-img"><div class="card-img-clip">{img_tag(PAGE_MEDIA[s["key"]]["img"], "")}</div><span class="icon-tile">{icon(s["icon"])}</span></div><div class="card-body"><h3>{e(s["nav"])}</h3><p>{e(s["summary"])}</p><span class="link-arrow">{e(s["link"])} {arrow()}</span></div></a>"""
        for s in SERVICES
    )
    body = f"""{page_hero("Services", p["h1"], p["intro"], [("Home", "/"), ("Services", None)], media=PAGE_MEDIA["services"])}
    <section class="section">
      <div class="wrap">
        <div class="grid grid-3 reveal-group">{cards}</div>
      </div>
    </section>
{image_band("abs-network.jpg", "One team across the whole journey.", "Creative, technical and operational skills working from the same plan, so each piece supports the next.")}
{closing(p["close_h2"], p["close_body"], "Talk Through Your Goals")}"""
    write("services/index.html", page("/services/", "Services | Spark Media",
                                      "Explore Spark Media’s website, advertising, creative, AI automation, CRM and systems integration services.",
                                      body, current="services"))

    for s in SERVICES:
        m = PAGE_MEDIA[s["key"]]
        sections = ""
        for i, blk in enumerate(s["blocks"]):
            if i == 0:
                note = f'<p class="note">{e(s["note"])}</p>' if s.get("note") else ""
                sections += f"""    <section class="section">
      <div class="wrap split split-top">
        <div class="reveal"><h2>{e(blk[0])}</h2><div class="prose lede" style="margin-top:20px">{paras(blk[1])}</div></div>
        <aside class="panel panel-accent reveal"><h3>What we can help with</h3>{checklist(s["help"])}{note}</aside>
      </div>
    </section>
"""
                sections += image_band(m["band"][0], m["band"][1], m["band"][2]) + "\n"
            else:
                sections += f"""    <section class="section">
      <div class="wrap split split-top">
        <div class="reveal"><h2>{e(blk[0])}</h2></div>
        <div class="prose lede reveal">{paras(blk[1])}</div>
      </div>
    </section>
"""
        extra = s.get("extra_link")
        extra_html = f'<p style="margin-top:28px"><a class="link-arrow" href="{extra[1]}">{e(extra[0])} {arrow()}</a></p>' if extra else ""
        rel_solutions = [x for x in SOLUTIONS if x["key"] in s["solutions"]]
        others = [x for x in SERVICES if x["key"] != s["key"]]
        body = f"""{page_hero(s["eyebrow"], s["h1"], s["intro"], [("Home", "/"), ("Services", "/services/"), (s["nav"], None)],
                             btn(s["cta"], "/contact/") + btn("All services", "/services/", "secondary", False), media=m)}
{sections}    <section class="section section-soft">
      <div class="wrap">
        <div class="reveal">{related_cards("Solutions that use this", rel_solutions)}{extra_html}</div>
      </div>
    </section>
{closing(s["close_h2"], s.get("close_body", ""), s["cta"])}
    <section class="section">
      <div class="wrap reveal">{related("Other services", others)}</div>
    </section>"""
        write(f'services/{s["slug"]}/index.html', page(s["href"], s["seo_title"], s["seo_desc"], body, current="services"))


def build_solutions():
    p = SOLUTIONS_PAGE
    cards = "".join(
        f"""<a class="card card-media card-problem reveal" href="{s["href"]}"><div class="card-img"><div class="card-img-clip">{img_tag(PAGE_MEDIA[s["key"]]["img"], "")}</div><span class="icon-tile">{icon(s["icon"])}</span></div><div class="card-body"><span class="q">{e(s["problem"])}</span><p>{e(s["summary"])}</p><span class="link-arrow">{e(s["nav"])} {arrow()}</span></div></a>"""
        for s in SOLUTIONS
    )
    body = f"""{page_hero("Solutions", p["h1"], p["intro"], [("Home", "/"), ("Solutions", None)], media=PAGE_MEDIA["solutions"])}
    <section class="section">
      <div class="wrap">
        <div class="grid grid-2 reveal-group">{cards}</div>
      </div>
    </section>
{closing("Not sure which one fits?", "Most bottlenecks touch more than one of these. Describe what’s happening and we’ll trace it from the customer’s side and your team’s side.", "Talk Through Your Bottleneck")}"""
    write("solutions/index.html", page("/solutions/", "Business Growth Solutions | Spark Media",
                                       "Solve disconnected systems, missed inquiries, slow lead response and inconsistent follow-up with connected marketing and AI.",
                                       body, current="solutions"))

    for s in SOLUTIONS:
        m = PAGE_MEDIA[s["key"]]
        blocks = ""
        for i, blk in enumerate(s["blocks"]):
            blocks += f"""    <section class="section">
      <div class="wrap split split-top">
        <div class="reveal"><h2>{e(blk[0])}</h2></div>
        <div class="prose lede reveal">{paras(blk[1])}</div>
      </div>
    </section>
"""
        blocks += image_band(m["band"][0], m["band"][1], m["band"][2]) + "\n"
        if s.get("steps"):
            steps = "".join(f'<li class="step reveal"><p>{e(t)}</p></li>' for t in s["steps"])
            detail = f"""    <section class="section">
      <div class="wrap">
        <div class="section-head reveal"><p class="eyebrow">How we work</p><h2>Our approach</h2></div>
        <ol class="steps steps-compact steps-line reveal-group">{steps}</ol>
        {f'<p class="lede reveal" style="margin-top:36px;max-width:760px">{e(s["outcome"])}</p>' if s.get("outcome") else ""}
      </div>
    </section>
"""
        else:
            detail = f"""    <section class="section">
      <div class="wrap split split-top">
        <div class="reveal"><p class="eyebrow">Possible components</p><h2>What the system can include</h2><p class="lede" style="margin-top:18px">Every business is different. We choose the pieces that fit your workflow, tools and customers.</p></div>
        <aside class="panel panel-accent reveal">{checklist(s["components"])}</aside>
      </div>
    </section>
"""
        rel = [x for x in SERVICES if x["key"] in s["services"]]
        others = [x for x in SOLUTIONS if x["key"] != s["key"]]
        body = f"""{page_hero("Solutions · " + s["nav"], s["h1"], s["intro"], [("Home", "/"), ("Solutions", "/solutions/"), (s["nav"], None)],
                             btn(s["cta"], "/contact/") + btn("All solutions", "/solutions/", "secondary", False), media=m)}
{blocks}{detail}    <section class="section section-soft">
      <div class="wrap reveal">{related_cards("Services involved", rel)}</div>
    </section>
{closing(s.get("close_h2", "Tell us where it’s getting stuck."), s.get("close_body", "We’ll start with the problem, then bring in the right mix of marketing, AI and systems work."), s["cta"])}
    <section class="section">
      <div class="wrap reveal">{related("Other solutions", others)}</div>
    </section>"""
        write(f'solutions/{s["slug"]}/index.html', page(s["href"], s["seo_title"], s["seo_desc"], body, current="solutions"))


def build_industries():
    p = INDUSTRIES_PAGE
    rows = "".join(
        f"""<article class="industry reveal">
          <div class="photo photo-accent">{img_tag(it["img"], it["alt"])}</div>
          <div><p class="eyebrow">{e(it["eyebrow"])}</p><h2>{e(it["title"])}</h2><p class="lede">{e(it["body"])}</p>
          <ul class="tags">{"".join(f"<li>{e(t)}</li>" for t in it["tags"])}</ul></div>
        </article>"""
        for it in p["items"]
    )
    body = f"""{page_hero("Industries", p["h1"], p["intro"], [("Home", "/"), ("Industries", None)], media=PAGE_MEDIA["industries"])}
    <section class="section">
      <div class="wrap">{rows}</div>
    </section>
{closing(p["close_h2"], p["close_body"], "Tell Us About Your Business")}"""
    write("industries/index.html", page("/industries/", "Industries We Work With | Spark Media",
                                        "Connected marketing and AI solutions for service businesses, healthcare, hospitality, venues and B2B companies.",
                                        body, current="industries"))


def build_about():
    p = ABOUT_PAGE
    principles = "".join(
        f'<article class="principle reveal"><div><span class="p-num">0{i + 1}</span><h2>{e(h)}</h2></div><div class="prose lede">{paras(b)}</div></article>'
        for i, (h, b) in enumerate(p["principles"])
    )
    body = f"""{page_hero("About", p["h1"], p["intro"], [("Home", "/"), ("About", None)], media=PAGE_MEDIA["about"])}
    <section class="section">
      <div class="wrap">
        <div class="photo photo-frame photo-accent reveal" style="aspect-ratio:21/9">
          {img_tag("about-team.jpg", "A small team of marketers and technical specialists working together around a table, with a workflow sketched on the whiteboard behind them")}
        </div>
      </div>
    </section>
    <section class="section">
      <div class="wrap">{principles}</div>
    </section>
{image_band("abs-network.jpg", "Marketing and systems, planned together.", "Each investment should support the next: the campaign, the page, the response and what your team sees afterward.")}
    <section class="section">
      <div class="wrap split split-top">
        <div class="reveal"><p class="eyebrow">Leadership</p><h2>Who you’ll work with.</h2><div class="prose lede" style="margin-top:20px"><p>{e(p["founder"])}</p></div></div>
        <div class="photo photo-frame reveal" style="aspect-ratio:3/2">{img_tag("home-bento.jpg", "A team shares a good moment around a laptop in a bright office")}</div>
      </div>
    </section>
{closing("Let’s see if we’re a fit.", "Tell us about your business and what you want to improve. We’ll be straightforward about where we can help.", "Get to Know Us")}"""
    write("about/index.html", page("/about/", "About Spark Media | Marketing & AI Implementation",
                                   "Meet Spark Media, a marketing and AI implementation partner that connects creative strategy, customer acquisition and business systems.",
                                   body, current="about"))


GHL_FORM = """<iframe
              src="https://api.leadconnectorhq.com/widget/form/CdcCxY5aaiFjtfkqdsdg"
              style="width:100%;height:100%;border:none;border-radius:8px"
              id="inline-CdcCxY5aaiFjtfkqdsdg"
              data-layout="{'id':'INLINE'}"
              data-trigger-type="alwaysShow"
              data-trigger-value=""
              data-activation-type="alwaysActivated"
              data-activation-value=""
              data-deactivation-type="neverDeactivate"
              data-deactivation-value=""
              data-form-name="Contact - SMS Opt-in (sparkmedia.ai)"
              data-height="924"
              data-layout-iframe-id="inline-CdcCxY5aaiFjtfkqdsdg"
              data-form-id="CdcCxY5aaiFjtfkqdsdg"
              data-cookie-consent="true"
              data-cookie-consent-provider="auto"
              title="Contact - SMS Opt-in (sparkmedia.ai)"
            ></iframe>
            <script src="https://link.msgsndr.com/js/form_embed.js"></script>"""

CONTACT_CONSENT = """This form has two separate, optional SMS consent checkboxes. Checking the first allows SparkMedia.ai (McCormick Solutions, LLC) to send non-marketing texts about your inquiry, such as replies, appointment confirmations, and reminders. Checking the second allows us to send marketing and promotional texts. You may choose either, both, or neither. Message frequency varies. Msg &amp; data rates may apply. Reply HELP for help, STOP to opt out. Consent is not a condition of purchase. See our <a href="/privacy.html">Privacy Policy</a> and <a href="/terms.html">Terms &amp; Conditions</a>."""

BOOK_CONSENT = """By providing your phone number and checking the SMS consent box, you agree to receive text messages from SparkMedia.ai (McCormick Solutions, LLC). Message frequency varies. Msg &amp; data rates may apply. Reply HELP for help, STOP to opt out. Consent is not a condition of purchase. See our <a href="/privacy.html">Privacy Policy</a> and <a href="/terms.html">Terms &amp; Conditions</a>."""


def build_contact():
    p = CONTACT_PAGE
    topics = "".join(f"<li>{e(t)}</li>" for t in p["topics"])
    body = f"""{page_hero("Contact", p["h1"], p["intro"], [("Home", "/"), ("Contact", None)], media=PAGE_MEDIA["contact"])}
    <section class="section">
      <div class="wrap contact-grid">
        <div class="form-card">
          <h2>Tell us about your business</h2>
          <p>Share what you’d like help with and the main challenge you’re facing. We’ll follow up to set up a conversation.</p>
          <div class="form-embed" id="ghl-form">
            {GHL_FORM}
          </div>
          <div class="consent">
            {CONTACT_CONSENT}
          </div>
        </div>
        <div class="aside-sticky">
          <div class="aside-card">
            <h3>Prefer to talk?</h3>
            <p>Pick a time that works for you and we’ll come prepared with questions about your goals.</p>
            <a class="btn btn-light" href="/book.html">Book a conversation {arrow()}</a>
          </div>
          <div class="aside-card aside-soft">
            <h3>What we can help with</h3>
            <ul class="checklist" style="margin-top:14px">{topics}</ul>
          </div>
          <div class="aside-card">
            <h3>Reach us directly</h3>
            <ul class="aside-list">
              <li><span>Phone</span><a href="tel:+17023341443">(702) 334-1443</a></li>
              <li><span>Email</span><a href="mailto:dave@sparkmedia.ai">dave@sparkmedia.ai</a></li>
              <li><span>Office</span>McCormick Solutions, LLC dba SparkMedia.ai<br>8690 Lloyd Ct, Las Vegas, NV 89145</li>
            </ul>
          </div>
        </div>
      </div>
    </section>"""
    for path in ("contact/index.html", "contact.html"):
        write(path, page("/contact/", "Contact Spark Media | Let’s Connect Your Growth System",
                         "Talk with Spark Media about website design, advertising, AI automation, CRM and connecting your business software.",
                         body, current="contact"))


def build_book():
    body = f"""{page_hero("Book a conversation", "Pick a time to talk.", "Choose a slot that works for you. We’ll use the time to understand your goals, your customer journey and the tools you rely on today.", [("Home", "/"), ("Contact", "/contact/"), ("Book", None)])}
    <section class="section">
      <div class="wrap narrow" style="max-width:900px">
        <div class="form-card booking-embed">
          <iframe src="https://api.leadconnectorhq.com/widget/booking/CrDctUVUZMiKEAYPEYJ9" style="width:100%; height:700px; border:none; overflow:hidden;" scrolling="no" id="CrDctUVUZMiKEAYPEYJ9" title="Book a conversation with Spark Media"></iframe>
          <script src="https://link.msgsndr.com/js/form_embed.js" type="text/javascript"></script>
          <div class="sms-consent consent">
            {BOOK_CONSENT}
          </div>
        </div>
      </div>
    </section>"""
    write("book.html", page("/book.html", "Book a Conversation | Spark Media",
                            "Book a conversation with Spark Media about your website, advertising, AI automation, CRM or systems integration.",
                            body, current="contact"))


def build_legal():
    meta = {
        "privacy": ("Privacy Policy | SparkMedia.ai", "Privacy Policy for SparkMedia.ai (McCormick Solutions, LLC), including SMS messaging practices."),
        "terms": ("Terms & Conditions | SparkMedia.ai", "Terms & Conditions and SMS Messaging Terms for SparkMedia.ai (McCormick Solutions, LLC)."),
    }
    for key, (title, desc) in meta.items():
        with open(os.path.join(os.path.dirname(__file__), "legal", key + ".html")) as f:
            inner = f.read()
        body = f"""    <section class="section" style="padding-top:64px">
      <div class="wrap">
        <article class="legal">
          {inner}
        </article>
      </div>
    </section>"""
        for path in (f"{key}.html", f"{key}/index.html"):
            write(path, page(f"/{key}.html", title, desc, body))


def build_404():
    body = f"""    <section class="notfound">
      {img_tag("abs-orbs.jpg", "", lazy=False, cls="notfound-bg")}
      <div class="wrap">
        <span class="code">404</span>
        <h1>This page got disconnected.</h1>
        <p>Let’s get you back to the right place.</p>
        <div class="btn-row">{btn("Return Home", "/")}{btn("Contact us", "/contact/", "secondary", False)}</div>
      </div>
    </section>"""
    write("404.html", page("/404.html", "Page not found | Spark Media", "This page got disconnected.", body, noindex=True))


def build_redirects():
    moves = {"industries.html": "/industries/"}
    for src, dest in moves.items():
        write(src, f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Moved | Spark Media</title>
  <meta http-equiv="refresh" content="0; url={dest}">
  <link rel="canonical" href="{SITE}{dest}">
  <meta name="robots" content="noindex">
</head>
<body>
  <p>This page has moved to <a href="{dest}">{SITE}{dest}</a>.</p>
</body>
</html>
""")


def build_sitemap():
    paths = ["/", "/services/"] + [s["href"] for s in SERVICES] + ["/solutions/"] + [s["href"] for s in SOLUTIONS] + [
        "/industries/", "/about/", "/contact/", "/book.html", "/social/", "/blog.html", "/privacy.html", "/terms.html"]
    urls = "\n".join(f"  <url><loc>{SITE}{p}</loc><lastmod>2026-09-25</lastmod></url>" for p in paths)
    write("sitemap.xml", f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{urls}
</urlset>
""")


if __name__ == "__main__":
    build_home()
    build_services()
    build_solutions()
    build_industries()
    build_about()
    build_contact()
    build_book()
    build_legal()
    build_404()
    build_redirects()
    build_sitemap()

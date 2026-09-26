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
    TIERS, OFFER_FAQ, OFFER_STEPS, TRADES, SEARCH_PILLARS, SEARCH_STEPS, SEARCH_FAQ, HOME_SERVICES, SOCIAL, POSTS,
)
from icons import icon  # noqa: E402

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
SITE = "https://sparkmedia.ai"
BRAND = "Spark Media"
ASSET_V = "4"
OG_IMAGE = f"{SITE}/assets/images/og-image.png"

FOOTER_DESC = ("Spark Media combines marketing, creative, AI and business systems to help companies "
               "attract customers, respond faster and work smarter.")

e = html.escape

INDUSTRY_NAV = [
    {"href": "/industries/#hospitality", "icon": "calendar", "nav": "Hospitality & venues", "blurb": "Inquiries, tours and bookings"},
    {"href": "/industries/#b2b", "icon": "integrate", "nav": "B2B & industrial", "blurb": "Longer buying cycles, clear handoffs"},
    {"href": "/industries/#healthcare", "icon": "users", "nav": "Healthcare & wellness", "blurb": "Clear next steps for patients"},
    {"href": "/industries/home-services/", "icon": "phone", "nav": "Home services", "blurb": "Emergency Google calls to your phone"},
]


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
        + nav_dropdown("Industries", "industries", INDUSTRY_NAV, "/industries/", "View all industries", current)
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
        + group("Industries", INDUSTRY_NAV, "/industries/")
        + '<a href="/about/">About</a><a href="/contact/">Contact</a>'
        + f'<a class="btn btn-primary" href="/contact/">Let’s Talk {arrow()}</a>'
        + "</nav>"
    )
    return (
        '<header class="site-header" data-header><div class="wrap header-inner">'
        f'<a class="brand" href="/" aria-label="{BRAND} home"><img src="/assets/logo/sparkmedia-logo-light.png" alt="{BRAND}" width="600" height="159"></a>'
        + desktop
        + f'<a class="btn btn-dark btn-sm header-cta" href="/contact/">Let’s Talk</a>'
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
          <li><a href="/industries/home-services/">Home services</a></li>
          <li><a href="/pricing.html">Home services pricing</a></li>
          <li><a href="/about/">About</a></li>
          <li><a href="/blog.html">Insights</a></li>
          <li><a href="/contact/">Contact</a></li>
          <li><a href="/book.html">Book a conversation</a></li>
        </ul></div>
      </div>
    </div>
    <div class="footer-legal">
      <div>
        <p>SparkMedia.ai is a DBA of McCormick Solutions, LLC</p>
        <p><a href="tel:+17027475589">(702) 747-5589</a></p>
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
            <div class="btn-row">{btn(cta_label, cta_href)}{sec}</div>
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
    path = src if src.startswith("/") else f"/assets/images/site/{src}"
    return f'<img{c} src="{path}" width="{w}" height="{h}" alt="{e(alt)}"{load} decoding="async">'


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
      {img_tag("abs-hero.jpg", "", lazy=False, cls="hero-bg")}
      <div class="wrap hero-grid">
        <div>
          <p class="eyebrow">{e(h["eyebrow"])}</p>
          <h1>Make every part of your business <span class="grad-text">work together.</span></h1>
          <p class="lede">{e(h["body"])}</p>
          <div class="btn-row">{btn("Let’s Talk About Your Business", "/contact/")}{btn("Explore What We Do", "/services/", "ghost-light", False)}</div>
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
            <span><i style="background:#67E8F9"></i>Connected</span>
            <span><i style="background:#475569"></i>Works on its own</span>
            <span><i style="background:#F87171"></i>Handoff breaks</span>
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
        "telephone": "+1-702-747-5589",
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
            <defs><linearGradient id="flowGrad" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#22D3EE"/><stop offset="1" stop-color="#2563EB"/></linearGradient></defs>
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


IND_IDS = ["hospitality", "b2b", "healthcare", "local"]


def build_industries():
    p = INDUSTRIES_PAGE
    rows = "".join(
        f"""<article class="industry reveal" id="{IND_IDS[i]}">
          <div class="photo photo-accent">{img_tag(it["img"], it["alt"])}</div>
          <div><p class="eyebrow">{e(it["eyebrow"])}</p><h2>{e(it["title"])}</h2><p class="lede">{e(it["body"])}</p>
          <ul class="tags">{"".join(f"<li>{e(t)}</li>" for t in it["tags"])}</ul>
          {f'<p style="margin-top:22px"><a class="link-arrow" href="/industries/home-services/">Explore home services {arrow()}</a></p>' if IND_IDS[i] == "local" else ""}</div>
        </article>"""
        for i, it in enumerate(p["items"])
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


# ---------------------------------------------------------------- home services, trades, pricing, audit

TRADE_BY = {t["slug"]: t for t in TRADES}


def tiers_block(cta_href="/audit.html"):
    cards = "".join(
        f"""<article class="tier{' tier-featured' if t.get('featured') else ''} reveal">
          <p class="tier-label">{e(t["label"])}</p>
          <h3>{e(t["name"])}</h3>
          <p class="tier-price"><strong>{e(t["price"])}</strong><span>{e(t["per"])}</span></p>
          <p class="tier-summary">{e(t["summary"])}</p>
          {checklist(t["items"])}
          <div class="btn-row">{btn("Book a strategy call", cta_href, "primary" if t.get("featured") else "secondary", t.get("featured", False))}</div>
        </article>"""
        for t in TIERS
    )
    return f'<div class="tiers reveal-group">{cards}</div>'


def faq_block(items):
    return '<div class="faq">' + "".join(
        f'<details class="faq-item reveal"><summary>{e(q)}{icon("chev")}</summary><p>{e(a)}</p></details>' for q, a in items
    ) + "</div>"


def numbered_steps(items, compact=False):
    cls = "steps steps-3 steps-line" + (" steps-compact" if compact else "")
    return f'<ol class="{cls} reveal-group">' + "".join(
        f'<li class="step reveal"><h3>{e(h)}</h3><p>{e(b)}</p></li>' for h, b in items) + "</ol>"


def trade_cards(slugs, cls="grid grid-3"):
    out = []
    for sl in slugs:
        t = TRADE_BY[sl]
        tag = "$249/mo ring" if t["kind"] == "emergency" else "Google Search + lead capture"
        out.append(f"""<a class="card card-media reveal" href="{t["path"]}"><div class="card-img"><div class="card-img-clip">{img_tag(t["img"], "")}</div></div><div class="card-body"><span class="pill">{e(tag)}</span><h3>{e(t["name"])}</h3><span class="link-arrow">{e(t["name"])} marketing {arrow()}</span></div></a>""")
    return f'<div class="{cls} reveal-group">' + "".join(out) + "</div>"


def build_home_services():
    h = HOME_SERVICES
    media = {"img": "home-services.jpg", "alt": "A home service technician greets a homeowner at the front door, with a service van in the driveway",
             "chips": [("phone", "Incoming call", "From Google Search"), ("calendar", "Job booked", "Today, 2:30 PM")]}
    emergency = [t["slug"] for t in TRADES if t["kind"] == "emergency"]
    search = [t["slug"] for t in TRADES if t["kind"] == "search"]
    body = f"""{page_hero("Industries · Home services", h["h1"], h["intro"], [("Home", "/"), ("Industries", "/industries/"), ("Home services", None)],
                         btn("Book a strategy call", "/audit.html") + btn("See pricing", "/pricing.html", "secondary", False), media=media)}
    <section class="section">
      <div class="wrap">
        <div class="section-head reveal"><p class="eyebrow">Emergency trades</p><h2>When something breaks, they call the first ad they see.</h2>
          <p class="lede">Call-only Google Ads for trades where people pick up the phone the moment there’s a problem. $249/mo. Ad spend extra.</p></div>
        {trade_cards(emergency, "grid grid-5")}
      </div>
    </section>
    <section class="section section-soft">
      <div class="wrap">
        <div class="section-head reveal"><p class="eyebrow">Pricing</p><h2>The phone rings. That’s the product.</h2>
          <p class="lede">Ad spend is yours, paid to Google. Our fee is management. Month-to-month.</p></div>
        {tiers_block()}
      </div>
    </section>
    <section class="section">
      <div class="wrap">
        <div class="section-head reveal"><p class="eyebrow">How it works</p><h2>A short call, a clear offer, a ringing phone.</h2></div>
        {numbered_steps(OFFER_STEPS)}
      </div>
    </section>
    <section class="section section-soft">
      <div class="wrap">
        <div class="section-head reveal"><p class="eyebrow">Planned work</p><h2>For jobs people research first.</h2>
          <p class="lede">Roofing, tree removal and window cleaning customers compare before they book. We build search campaigns, call-first landing pages and tracking around that decision.</p></div>
        {trade_cards(search)}
      </div>
    </section>
{image_band("abs-network.jpg", "The call is only the start.", "Missed-call text-back, follow-up and review requests keep a ringing phone from turning into a missed job.")}
    <section class="section">
      <div class="wrap split split-top">
        <div class="reveal"><p class="eyebrow">Questions</p><h2>Before you ask.</h2></div>
        {faq_block(OFFER_FAQ)}
      </div>
    </section>
{closing("See if emergency Google Search is a fit.", "A 15–20 minute strategy call. If it isn’t a fit, we’ll say so.", "Book a strategy call", "/audit.html")}"""
    write("industries/home-services/index.html", page("/industries/home-services/", "Home Services Marketing | Spark Media",
          "Call-only Google Ads for plumbers, HVAC, electricians, locksmiths and garage door companies, plus search campaigns for roofing, tree removal and window cleaning.",
          body, current="industries"))


def build_trades():
    for t in TRADES:
        trail = [("Home", "/"), ("Home services", "/industries/home-services/"), (t["name"], None)]
        if t["kind"] == "emergency":
            media = {"img": t["img"], "alt": t["alt"],
                     "chips": [("ads", "Google Search", f"“{t['search']}”"), ("phone", "Tap to call", "Rings your phone")]}
            hero = page_hero(f"{t['name']} · Emergency Google Search", t["h1"], t["lede"], trail,
                             btn("Book a strategy call", "/audit.html") + btn("See pricing", "/pricing.html", "secondary", False), media=media)
            body = f"""{hero}
    <section class="section">
      <div class="wrap">
        <div class="section-head reveal"><p class="eyebrow">How it works</p><h2>They search. They tap Call. Your phone rings.</h2></div>
        {numbered_steps(OFFER_STEPS)}
      </div>
    </section>
    <section class="section section-soft">
      <div class="wrap">
        <div class="section-head reveal"><p class="eyebrow">Pricing</p><h2>Two simple tiers.</h2><p class="lede">Ad spend is yours, paid to Google. Our fee is management. Month-to-month.</p></div>
        {tiers_block()}
      </div>
    </section>
    <section class="section">
      <div class="wrap split split-top">
        <div class="reveal"><p class="eyebrow">Questions</p><h2>Before you ask.</h2></div>
        {faq_block(OFFER_FAQ)}
      </div>
    </section>"""
        else:
            media = {"img": t["img"], "alt": t["alt"],
                     "chips": [("ads", "High-intent search", "Ready to hire"), ("phone", "Call or request", "Tracked to the job")]}
            hero = page_hero(f"{t['name']} · Google Ads", t["h1"], t["lede"], trail,
                             btn("Book a strategy call", "/audit.html") + btn("All home services", "/industries/home-services/", "secondary", False), media=media)
            pillars = "".join(f'<article class="card reveal"><span class="icon-tile">{icon(ic)}</span><h3>{e(a)}</h3><p>{e(b)}</p></article>' for ic, a, b in SEARCH_PILLARS)
            challenges = ""
            if t.get("challenges"):
                cards = "".join(f'<article class="card reveal"><h3>{e(a)}</h3><p>{e(b)}</p></article>' for a, b in t["challenges"])
                challenges = f"""    <section class="section">
      <div class="wrap">
        <div class="section-head reveal"><p class="eyebrow">The challenge</p><h2>Great work doesn’t help if nobody finds you.</h2></div>
        <div class="grid grid-3 reveal-group">{cards}</div>
      </div>
    </section>
"""
            body = f"""{hero}
    <section class="section">
      <div class="wrap">
        <div class="grid grid-3 reveal-group">{pillars}</div>
      </div>
    </section>
{challenges}    <section class="section section-soft">
      <div class="wrap">
        <div class="section-head reveal"><p class="eyebrow">What we do</p><h2>What we do for {e(t["noun"])}.</h2><p class="lede">A simple system built around Google Search, the highest-intent channel.</p></div>
        {numbered_steps(SEARCH_STEPS, compact=True).replace("steps-3", "")}
      </div>
    </section>
    <section class="section">
      <div class="wrap split split-top">
        <div class="reveal"><p class="eyebrow">Questions</p><h2>Answers before you book.</h2></div>
        {faq_block(SEARCH_FAQ)}
      </div>
    </section>"""
        body += f"""
    <section class="section section-soft">
      <div class="wrap">
        <h2 class="related-title reveal">Other home services</h2>
        {trade_cards(t["related"])}
      </div>
    </section>
{closing("See if Google Search is a fit for your business.", "A 15–20 minute strategy call about your trade, your service area and how you handle calls.", "Book a strategy call", "/audit.html")}"""
        desc = t["lede"] if len(t["lede"]) < 170 else t["lede"][:157].rsplit(" ", 1)[0] + "…"
        write(t["path"].lstrip("/"), page(t["path"], f'{t["name"]} Marketing | Spark Media', desc, body, current="industries"))


def build_pricing():
    body = f"""{page_hero("Home services pricing", "The phone rings. That’s the product.", "Call-only Google Ads for emergency home service trades. Ad spend is yours, paid to Google. Our fee is management. Month-to-month.",
                         [("Home", "/"), ("Home services", "/industries/home-services/"), ("Pricing", None)], media={"img": "abs-orbs.jpg", "alt": "", "abstract": True})}
    <section class="section">
      <div class="wrap">
        {tiers_block()}
        <p class="caption-note reveal" style="margin-top:22px">Websites, AI automation, CRM and systems integration work are scoped per project. <a href="/contact/">Tell us what you need</a>.</p>
      </div>
    </section>
    <section class="section section-soft">
      <div class="wrap split split-top">
        <div class="reveal"><p class="eyebrow">Questions</p><h2>Before you ask.</h2></div>
        {faq_block(OFFER_FAQ)}
      </div>
    </section>
    <section class="section">
      <div class="wrap">
        <h2 class="related-title reveal">Trades we run this for</h2>
        {trade_cards([t["slug"] for t in TRADES if t["kind"] == "emergency"], "grid grid-5")}
      </div>
    </section>
{closing("See if emergency Google Search is a fit.", "A 15–20 minute strategy call. If it isn’t a fit, we’ll say so.", "Book a strategy call", "/audit.html")}"""
    write("pricing.html", page("/pricing.html", "Home Services Pricing | Spark Media",
          "Call-only Google Ads for emergency trades. $249/mo, or $399/mo with missed-call text-back, follow-up and review asks. Ad spend extra.",
          body, current="industries"))


AUDIT_CONSENT = """By providing your phone number and checking the SMS consent box, you agree to receive non-marketing text messages from SparkMedia.ai (McCormick Solutions, LLC) about your appointment and inquiry, including booking confirmations, reminders, and follow-ups. We do not send marketing texts to numbers collected through this booking form. Message frequency varies. Msg &amp; data rates may apply. Reply HELP for help, STOP to opt out. Consent is not a condition of purchase. See our <a href="/privacy.html">Privacy Policy</a> and <a href="/terms.html">Terms &amp; Conditions</a>."""


def build_audit():
    steps = "".join(f'<li class="step reveal"><h3>{e(h)}</h3><p>{e(b)}</p></li>' for h, b in OFFER_STEPS)
    body = f"""{page_hero("Strategy call", "See if emergency Google Search is a fit.", "Dead AC. Leaking pipe. Locked out. They Google it and tap Call. We run call-only ads so that call hits your phone. $249/mo. Ad spend extra.",
                         [("Home", "/"), ("Home services", "/industries/home-services/"), ("Strategy call", None)])}
    <section class="section">
      <div class="wrap contact-grid">
        <div class="form-card booking-embed">
          <h2>Book your strategy call</h2>
          <p>Pick a time for a 15–20 minute call about your trade and service area.</p>
          <div style="margin-top:18px">
            <iframe src="https://api.leadconnectorhq.com/widget/booking/CrDctUVUZMiKEAYPEYJ9" style="width:100%; height:600px; border:none; overflow:hidden;" scrolling="no" id="CrDctUVUZMiKEAYPEYJ9" title="Book a strategy call with Spark Media"></iframe>
            <script src="https://link.msgsndr.com/js/form_embed.js" type="text/javascript"></script>
          </div>
          <div class="consent">
            {AUDIT_CONSENT}
          </div>
          <p class="caption-note">Prefer to talk? Call <a href="tel:+17027475589">(702) 747-5589</a></p>
        </div>
        <div class="aside-sticky">
          <div class="aside-card aside-soft">
            <h3>How the call works</h3>
            <ol class="steps steps-compact" style="grid-template-columns:1fr;margin-top:14px">{steps}</ol>
          </div>
          <div class="aside-card">
            <h3>Who it’s for</h3>
            <p>Plumbers, HVAC, electricians, locksmiths and garage door companies that can pick up emergency calls.</p>
            <a class="btn btn-light" href="/pricing.html">See pricing {arrow()}</a>
          </div>
        </div>
      </div>
    </section>"""
    write("audit.html", page("/audit.html", "Book a Strategy Call | Spark Media",
          "Book a 15–20 minute strategy call to see if call-only Google Ads for emergency home service trades are a fit.",
          body, current="industries"))


# ---------------------------------------------------------------- social (UGC) and insights

def build_social():
    s_ = SOCIAL
    media = {"img": "/assets/images/social/hero-reel.jpg", "alt": "An HVAC technician films a selfie-style video beside an outdoor AC unit",
             "chips": [("creative", "Reels", "Shot on location"), ("users", "Real people", "Your team and customers")]}
    why = "".join(f'<article class="card reveal"><h3>{e(a)}</h3><p>{e(b)}</p></article>' for a, b in s_["why"])
    formats = "".join(
        f"""<article class="card card-media card-tall reveal"><div class="card-img"><div class="card-img-clip">{img_tag("/assets/images/social/" + f, alt, 1024, 1536)}</div></div><div class="card-body"><h3>{e(h)}</h3><p>{e(b)}</p></div></article>"""
        for f, alt, h, b in s_["formats"]
    )
    body = f"""{page_hero("Content & Creative · UGC + Instagram", s_["h1"], s_["intro"], [("Home", "/"), ("Services", "/services/"), ("Content & Creative", "/services/content-creative/"), ("UGC + Instagram", None)],
                         btn("Book a content call", "/contact/") + btn("See what we make", "#formats", "secondary", False), media=media)}
    <section class="section">
      <div class="wrap">
        <div class="section-head reveal"><p class="eyebrow">Why UGC</p><h2>{e(s_["why_h2"])}</h2><p class="lede">{e(s_["why_body"])}</p></div>
        <div class="grid grid-4 reveal-group">{why}</div>
      </div>
    </section>
    <section class="section section-soft" id="formats">
      <div class="wrap">
        <div class="section-head reveal"><p class="eyebrow">What we make</p><h2>Four formats. One content engine.</h2><p class="lede">Each shoot gets cut into every format, so one day of filming feeds weeks of posts.</p></div>
        <div class="grid grid-4 reveal-group">{formats}</div>
      </div>
    </section>
    <section class="section">
      <div class="wrap">
        <div class="section-head reveal"><p class="eyebrow">How it works</p><h2>Brief. Shoot. Edit. Post.</h2></div>
        <ol class="steps steps-line reveal-group">{"".join(f'<li class="step reveal"><h3>{e(h)}</h3><p>{e(b)}</p></li>' for h, b in s_["steps"])}</ol>
      </div>
    </section>
{image_band("/assets/images/social/shoot.jpg", "Shot where you work.", "Phone-native shoots at your real location. No studio, no stock footage.")}
    <section class="section">
      <div class="wrap split split-top">
        <div class="reveal"><p class="eyebrow">What you get</p><h2>{e(s_["get_h2"])}</h2><p class="lede" style="margin-top:18px">{e(s_["get_body"])}</p>
          <div class="btn-row" style="margin-top:26px">{btn("Get a content plan", "/contact/")}</div></div>
        <aside class="panel panel-accent reveal">{checklist(s_["get"])}</aside>
      </div>
    </section>
    <section class="section section-soft">
      <div class="wrap split split-top">
        <div class="reveal"><p class="eyebrow">Questions</p><h2>Before you ask.</h2></div>
        {faq_block(s_["faq"])}
      </div>
    </section>
{closing("Let’s fill your feed.", "Tell us what you do and where you work. We’ll come back with hooks, formats and a posting plan.", "Book a content call")}"""
    write("social/index.html", page("/social/", "UGC & Instagram Content | Spark Media",
          "UGC videos, Instagram Reels, carousels and stories for restaurants, bars, family venues and home services. Shot for the feed and ready to post or run as ads.",
          body, current="services"))


def build_blog():
    cards = "".join(
        f"""<a class="card card-media reveal" href="{p_["path"]}"><div class="card-img"><div class="card-img-clip">{img_tag(p_["img"], p_["alt"])}</div></div><div class="card-body"><span class="pill">{e(p_["category"])}</span><h3>{e(p_["title"])}</h3><p>{e(p_["excerpt"])}</p><span class="post-meta">{e(p_["date"])} · {e(p_["read"])}</span><span class="link-arrow">Read article {arrow()}</span></div></a>"""
        for p_ in POSTS
    )
    body = f"""{page_hero("Insights", "Notes on marketing, AI and connected systems.", "Practical thinking on automation, advertising and the customer journey.", [("Home", "/"), ("Insights", None)], media={"img": "abs-waves.jpg", "alt": "", "abstract": True})}
    <section class="section">
      <div class="wrap">
        <div class="grid grid-2 reveal-group">{cards}</div>
      </div>
    </section>
{closing("Want to talk it through?", "Tell us what you’re trying to improve and we’ll share what we’d try first.", "Start a Conversation")}"""
    write("blog.html", page("/blog.html", "Insights | Spark Media", "Notes on marketing, AI automation and connected business systems from Spark Media.", body, current=None))

    for p_ in POSTS:
        with open(os.path.join(os.path.dirname(__file__), "posts", p_["slug"] + ".html")) as f:
            article = f.read()
        others = [x for x in POSTS if x["slug"] != p_["slug"]]
        more = "".join(f'<a class="mini-card" href="{x["path"]}">{img_tag(x["img"], "")}<span><strong>{e(x["title"])}</strong><small>{e(x["date"])} · {e(x["read"])}</small></span>{arrow()}</a>' for x in others)
        body = f"""    <section class="post-hero">
      <div class="wrap post-wrap">
        {crumbs([("Home", "/"), ("Insights", "/blog.html"), (p_["category"], None)])}
        <p class="eyebrow">{e(p_["category"])}</p>
        <h1>{e(p_["title"])}</h1>
        <p class="post-meta">{e(p_["date"])} · {e(p_["read"])}</p>
      </div>
    </section>
    <section class="section" style="padding-top:0">
      <div class="wrap post-wrap">
        <div class="post-cover">{img_tag(p_["img"], p_["alt"], lazy=False)}</div>
        <article class="post-body">
          {article}
        </article>
        <h2 class="related-title" style="margin-top:56px">More insights</h2>
        <div class="mini-cards" style="grid-template-columns:1fr">{more}</div>
      </div>
    </section>
{closing("Ready to put this to work?", "Tell us where your customer journey breaks down. We’ll help you find a practical way to connect the pieces.", "Start a Conversation")}"""
        write(p_["path"].lstrip("/"), page(p_["path"], f'{p_["title"]} | Spark Media', p_["excerpt"], body, extra_head='<meta property="og:type" content="article">'))


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
        "/industries/", "/industries/home-services/", "/pricing.html", "/audit.html"] + [t["path"] for t in TRADES] + [
        "/about/", "/contact/", "/book.html", "/social/", "/blog.html"] + [p_["path"] for p_ in POSTS] + ["/privacy.html", "/terms.html"]
    urls = "\n".join(f"  <url><loc>{SITE}{p}</loc><lastmod>2026-09-26</lastmod></url>" for p in paths)
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
    build_home_services()
    build_trades()
    build_pricing()
    build_audit()
    build_social()
    build_blog()
    build_redirects()
    build_sitemap()

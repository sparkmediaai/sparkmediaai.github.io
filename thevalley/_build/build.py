"""
Build the prototype site.

Eleven pages share one header, one footer and one stylesheet. Writing them by
hand would mean changing the navigation in eleven places the first time it
moves, and it will move — the structure is a proposal, not a decision. So the
pages are data and the shell is code.

Run:  python thevalley/_build/build.py
"""
import os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SITE = "The Valley Venues"
TAGLINE = "One Private Mountain Estate. All for You."

# Primary navigation. Five destinations and one invitation — the Venues
# dropdown is deliberately absent; it is what made the estate read as four
# separate places.
NAV = [
    ("Weddings", "/thevalley/weddings/"),
    ("Stay", "/thevalley/stay/"),
    ("The Estate", "/thevalley/the-estate/"),
    ("Planners", "/thevalley/planners/"),
    ("About", "/thevalley/about/"),
]
CTA = ("Book a Tour", "/thevalley/book-a-tour/")

FOOTER = [
    ("Celebrate", [
        ("The Estate Weekend", "/thevalley/weddings/"),
        ("What's Included", "/thevalley/weddings/whats-included/"),
        ("Real Weddings", "/thevalley/weddings/real-weddings/"),
        ("Single-Day Celebrations", "/thevalley/weddings/single-day/"),
    ]),
    ("Stay", [
        ("Lodging on the Estate", "/thevalley/stay/"),
        ("The Estate", "/thevalley/the-estate/"),
    ]),
    ("Trade", [
        ("For Planners", "/thevalley/planners/"),
        ("Preferred Vendors", "/thevalley/planners/vendors/"),
    ]),
    ("The Valley Venues", [
        ("About &amp; Kobi", "/thevalley/about/"),
        ("Book a Tour", "/thevalley/book-a-tour/"),
    ]),
]


def shell(page):
    """Wrap one page's body in the site chrome."""
    depth_root = "/thevalley/"
    nav = "\n".join(
        '        <li><a href="%s"%s>%s</a></li>'
        % (href, ' aria-current="page"' if page["nav"] == label else "", label)
        for label, href in NAV)

    foot = "\n".join(
        '        <div>\n          <h4>%s</h4>\n          <ul>%s</ul>\n        </div>'
        % (head, "".join('\n            <li><a href="%s">%s</a></li>' % (h, t)
                         for t, h in links) + "\n          ")
        for head, links in FOOTER)

    hero = page.get("hero_html", "")
    if not hero and page.get("hero_img"):
        hero += '  <div class="hero-img" role="img" aria-label="%s" style="background-image:url(\'%sassets/img/%s\')"></div>\n' % (
            page["hero_alt"], depth_root, page["hero_img"])
    actions = ""
    if page.get("actions"):
        actions = '\n    <div class="hero-actions">%s</div>' % "".join(
            '\n      <a class="btn%s" href="%s">%s</a>' % (
                " btn-solid" if i == 0 else "", h, t)
            for i, (t, h) in enumerate(page["actions"])) + "\n    "

    return """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>%(title)s</title>
<meta name="description" content="%(desc)s">
<meta name="robots" content="noindex,nofollow">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;1,400&family=Montserrat:wght@400;500;600&display=swap">
<link rel="stylesheet" href="%(root)sassets/site.css">
%(head)s</head>
<body>

<a class="skip" href="#main">Skip to content</a>

<header class="site-head">
  <div class="inner">
    <a class="wordmark" href="%(root)s">%(site)s</a>
    <nav class="site-nav" aria-label="Primary">
      <ul>
%(nav)s
      </ul>
    </nav>
    <a class="btn btn-solid" href="%(cta_href)s">%(cta_text)s</a>
  </div>
</header>

<header class="hero">
%(hero)s  <div class="hero-body">
    <div class="eyebrow">%(eyebrow)s</div>
    <h1>%(h1)s</h1>
    <p>%(standfirst)s</p>%(actions)s
  </div>
</header>

<main id="main">
%(body)s
</main>

<footer class="site-foot">
  <div class="inner">
%(foot)s
    <div>
      <h4>Visit</h4>
      <address class="addr">
        1860 Pope Creek Rd<br>Wildwood, Georgia<br>
        Fifteen minutes from Chattanooga
      </address>
    </div>
  </div>
  <div class="colophon">
    <span>Prototype &mdash; structure and placeholder copy. Not a live site.</span>
    <span>Photography is existing estate imagery, standing in.</span>
  </div>
</footer>
%(foot_js)s
</body>
</html>
""" % {
        "title": page["title"], "desc": page["desc"], "root": depth_root,
        "site": SITE, "nav": nav, "cta_href": CTA[1], "cta_text": CTA[0],
        "hero": hero, "eyebrow": page["eyebrow"], "h1": page["h1"],
        "standfirst": page["standfirst"], "actions": actions,
        "body": page["body"], "foot": foot,
        "head": page.get("head", ""), "foot_js": page.get("foot_js", ""),
    }


# ---------------------------------------------------------------- the pages
PAGES = {}

PAGES["index.html"] = dict(
    nav=None, title="%s | %s" % (SITE, TAGLINE), desc=TAGLINE,
    head='<link rel="stylesheet" href="/thevalley/assets/home.css">\n'
         '<link rel="preload" as="image" href="/thevalley/assets/img/hero-1.webp"\n'
         '      imagesrcset="/thevalley/assets/img/hero-1-sm.webp 1100w, /thevalley/assets/img/hero-1.webp 2200w"\n'
         '      imagesizes="100vw">\n',
    foot_js='<script src="/thevalley/assets/home.js" defer></script>',
    hero_html='  <div class="hero-stage">\n    <figure class="slide is-on" data-moment="The arrival"><img src="/thevalley/assets/img/hero-1.webp" srcset="/thevalley/assets/img/hero-1-sm.webp 1100w, /thevalley/assets/img/hero-1.webp 2200w" sizes="100vw" alt="Magnolia House, white columns above the lawn" width="2200" height="1100" fetchpriority="high" decoding="async"></figure>\n    <figure class="slide" data-moment="The morning"><img data-src="/thevalley/assets/img/hero-2.webp" data-srcset="/thevalley/assets/img/hero-2-sm.webp 1100w, /thevalley/assets/img/hero-2.webp 2200w" sizes="100vw" alt="A groom having his bow tie straightened, both of them laughing" width="2200" height="1100" decoding="async"></figure>\n    <figure class="slide" data-moment="The meadow, set"><img data-src="/thevalley/assets/img/hero-3.webp" data-srcset="/thevalley/assets/img/hero-3-sm.webp 1100w, /thevalley/assets/img/hero-3.webp 2200w" sizes="100vw" alt="The ceremony aisle set out, the ridge behind it" width="2200" height="1100" decoding="async"></figure>\n    <figure class="slide" data-moment="Golden hour"><img data-src="/thevalley/assets/img/hero-4.webp" data-srcset="/thevalley/assets/img/hero-4-sm.webp 1100w, /thevalley/assets/img/hero-4.webp 2200w" sizes="100vw" alt="A couple in the meadow as the light goes" width="2200" height="1100" decoding="async"></figure>\n    <figure class="slide" data-moment="After dark"><img data-src="/thevalley/assets/img/hero-5.webp" data-srcset="/thevalley/assets/img/hero-5-sm.webp 1100w, /thevalley/assets/img/hero-5.webp 2200w" sizes="100vw" alt="The conservatory at Magnolia House, lit for dinner" width="2200" height="1100" decoding="async"></figure>\n    <div class="hero-marks">\n      <p class="hero-hour"><span>The arrival</span></p>\n      <div class="hero-dots" role="group" aria-label="Choose a moment">\n      <button type="button" aria-current="true"><span class="skip">The arrival</span></button>\n      <button type="button" aria-current="false"><span class="skip">The morning</span></button>\n      <button type="button" aria-current="false"><span class="skip">The meadow, set</span></button>\n      <button type="button" aria-current="false"><span class="skip">Golden hour</span></button>\n      <button type="button" aria-current="false"><span class="skip">After dark</span></button>\n      </div>\n    </div>\n  </div>\n',
    eyebrow="Wildwood, Georgia &middot; Fifteen minutes from Chattanooga",
    h1="One Private Mountain Estate. All for You.",
    standfirst="Seventy-four private acres beneath Lookout Mountain, fifteen minutes from "
               "Chattanooga. One wedding at a time, ever. For your two days the gate closes "
               "behind one family, and every field, every porch and every bed is yours.",
    actions=[("Book a Tour", "/thevalley/book-a-tour/"),
             ("Walk the Estate", "/thevalley/the-estate/")],
    body="""
<section>
  <div class="lede reveal">
    <div class="eyebrow">Why any of this matters</div>
    <h2>This is one of the best days of your life.</h2>
    <p>It is also one of the only times in a life when nearly everyone you love is in one
       place. Parents and grandparents. Childhood friends and college friends. Brothers and
       sisters. People who moved across the country and have not been in the same room in
       years.</p>
    <p>Most venues compress all of that into a handful of scheduled hours &mdash; arrive,
       ceremony, cocktail hour, reception, leave. Everything below follows from thinking
       that is the wrong way round.</p>
  </div>
</section>

<section>
  <div class="statement reveal">
    <div class="eyebrow">What makes this different</div>
    <h2>One estate. One couple. One weekend.</h2>
    <p>Larger estates in this region run two and sometimes three weddings on a single
       Saturday. It is how the acreage pays for itself &mdash; and it means another bride is
       on the property, another family&rsquo;s flowers are going out the far door, and
       another cocktail hour is audible from the ceremony. Someone else&rsquo;s arch is
       coming down while yours goes up.</p>
    <p>Seventy-four acres cannot be split, so they are not. From the moment you arrive to
       the moment you leave, the estate is arranged around one family, held that way for
       two days, and then put away and arranged again around the next.</p>
    <ul class="nots">
      <li>No second wedding on the property</li>
      <li>Nothing flipped or reset around you</li>
      <li>Nothing shared, overheard, or hurried</li>
      <li>Every gate, every field, every bed</li>
    </ul>
    <p class="close">Not one ballroom. Not one ceremony lawn. Not a collection of unrelated
       venues. For a little while, an entire mountain estate is simply yours.</p>
    <a class="btn" href="/thevalley/the-estate/">See the whole property</a>
  </div>
</section>

<section>
  <div class="lede">
    <div class="eyebrow">The weekend</div>
    <h2>More than a wedding day.</h2>
    <p>The ceremony takes thirty minutes. Most venues sell those thirty minutes and the
       eight hours around them. This estate sells the two days you live inside.</p>
  </div>
  <ol class="weekend">
    <li class="wk reveal">
      <figure><img src="/thevalley/assets/img/wk-fri.webp" alt="Groomsmen in the clubhouse, late" width="1200" height="900" loading="lazy" decoding="async"></figure>
      <span class="wk-when">Friday</span>
      <b>You arrive once</b>
      <p>Through the gate, and for the next two days this is simply where you are. The
         rehearsal happens where the vows will, and nobody goes back to a hotel.</p>
    </li>
    <li class="wk reveal">
      <figure><img src="/thevalley/assets/img/wk-dawn.webp" alt="A suite on the estate in the morning" width="1200" height="900" loading="lazy" decoding="async"></figure>
      <span class="wk-when">Saturday, early</span>
      <b>Sunrise comes with the room</b>
      <p>Light comes up over Lookout Mountain and fills the room you are already standing
         in. Hair can start at five. There is no commute in a wedding dress.</p>
    </li>
    <li class="wk reveal">
      <figure><img src="/thevalley/assets/img/wk-gold.webp" alt="A couple dancing on the deck as the light goes" width="1200" height="900" loading="lazy" decoding="async"></figure>
      <span class="wk-when">Saturday, six</span>
      <b>The mountain turns gold</b>
      <p>Guests walk from the ceremony to the overlook. Nobody drives, nobody follows
         directions, and nobody starts looking for their keys at eleven.</p>
    </li>
    <li class="wk reveal">
      <figure><img src="/thevalley/assets/img/wk-sun.webp" alt="The cottages on the hill at dusk" width="1200" height="900" loading="lazy" decoding="async"></figure>
      <span class="wk-when">Sunday</span>
      <b>Goodnight instead of goodbye</b>
      <p>Two nights means three mornings, and the last thing you do together is breakfast
         rather than a car park.</p>
    </li>
  </ol>
</section>

<section>
  <div class="lede">
    <div class="eyebrow">Two ways to be here</div>
    <h2>Celebrate, or simply stay.</h2>
  </div>
  <div class="grid">
    <article class="card reveal">
      <img src="/thevalley/assets/img/weddings.webp" alt="A ceremony under way in the meadow" width="2000" height="1000" loading="lazy" decoding="async">
      <div class="eyebrow">Celebrate</div>
      <h3>The Estate Weekend</h3>
      <p>Friday afternoon to Sunday morning, the property held for one couple.</p>
      <a class="btn" href="/thevalley/weddings/">Weddings</a>
    </article>
    <article class="card reveal">
      <img src="/thevalley/assets/img/stay.webp" alt="A cottage in the woods" width="1600" height="800" loading="lazy" decoding="async">
      <div class="eyebrow">Stay</div>
      <h3>Lodging on the estate</h3>
      <p>Cottages facing the ridge, open when there is no wedding on the property.</p>
      <a class="btn" href="/thevalley/stay/">Stay</a>
    </article>
  </div>
</section>

<section class="closing">
  <div class="closing-img" role="img" aria-label="A cottage in the woods, lit at night"
       style="background-image:url('/thevalley/assets/img/close-woods.webp')"></div>
  <div class="closing-body">
    <div class="eyebrow">And then</div>
    <h2>You disappear, without leaving.</h2>
    <p>A cottage in the woods at the far edge of the property, a short ride from the music.
       Married, alone, and thirty seconds from everyone you love.</p>
    <a class="btn" href="/thevalley/book-a-tour/">Book a tour</a>
  </div>
</section>
""")

PAGES["weddings/index.html"] = dict(
    nav="Weddings", title="Weddings | %s" % SITE,
    desc="The Estate Weekend at The Valley Venues.",
    hero_img="weddings.webp", hero_alt="A ceremony under way in the meadow, guests seated toward the ridge",
    eyebrow="Celebrate",
    h1="More Than a Wedding Day",
    standfirst="There will be a ceremony. There will be dinner. There will be dancing. "
               "And then there is everything around it.",
    actions=[("Book a Tour", "/thevalley/book-a-tour/"),
             ("What's Included", "/thevalley/weddings/whats-included/")],
    body="""
<section>
  <div class="lede">
    <h2>The Estate Weekend</h2>
    <p>The night before, when your friends are still up at one in the morning. Sunrise over
       Lookout Mountain through the window of the room where you are already getting ready.
       Breakfast with your grandparents before anyone drives anywhere.</p>
    <p>The ceremony takes thirty minutes. The weekend is what you will remember.</p>
  </div>
  <div class="grid">
    <article class="card">
      <div class="eyebrow">Hero experience</div>
      <h3>The Estate Weekend</h3>
      <p>Two nights, the whole property, one couple. Wedding, lodging, time and privacy
         as a single thing rather than four invoices.</p>
    </article>
    <article class="card">
      <div class="eyebrow">Premium</div>
      <h3>All-Inclusive Estate Experience</h3>
      <p>Adds deeper design, planning, food, beverage, coordination and vendor support &mdash;
         and Kobi's own hand in the design.</p>
    </article>
    <article class="card">
      <div class="eyebrow">Alternate</div>
      <h3>Single-Day Celebration</h3>
      <p>A real offering for couples who want the day rather than the weekend.
         <a href="/thevalley/weddings/single-day/">See single-day celebrations</a>.</p>
    </article>
  </div>
</section>

<section id="investment">
  <div class="lede">
    <div class="eyebrow">Investment</div>
    <h2>One figure, and a conversation.</h2>
    <p>Estate Weekends begin at <b>[starting figure &mdash; to be confirmed]</b>. There is no
       package grid and no price list to download, because what actually fits depends on your
       date, your count and how you want the weekend to feel.</p>
    <p>Tell us those three things and what comes back is a recommendation, not a brochure.</p>
    <a class="btn btn-solid" href="/thevalley/book-a-tour/">Start there</a>
  </div>
  <div class="note">
    <p><b>Prototype note.</b> The published starting figure is one of the decisions still
       open. The framework recommends a single number with nothing beside it &mdash; the
       absence of everything else is what produces the enquiry.</p>
  </div>
</section>
""")

PAGES["weddings/whats-included/index.html"] = dict(
    nav="Weddings", title="What's Included | %s" % SITE,
    desc="What comes with the estate, and what happens when the weather turns.",
    hero_img="included.webp", hero_alt="The conservatory at Magnolia House, glass on three sides",
    eyebrow="Celebrate &middot; What's included",
    h1="Fewer separate decisions.",
    standfirst="The questions a mother asks: what is included, where does everyone sleep, "
               "what happens if it rains, and who is responsible for what.",
    body="""
<section>
  <div class="grid">
    <article class="card">
      <h3>Already on the property</h3>
      <p>Tables, chairs, linens and an extensive decor inventory, included rather than
         rented &mdash; so fewer details become their own vendor, their own invoice and
         their own phone call.</p>
    </article>
    <article class="card">
      <h3>It rained, and nothing changed</h3>
      <p>Glass, cover and the whole property to move into, including the conservatory at
         Magnolia House. No tent. No five o'clock panic. No flip fee.</p>
    </article>
    <article class="card">
      <h3>Handled behind the scenes</h3>
      <p>Setup, cleanup, golf carts, parking, security and coordination, by people who have
         worked this property hundreds of times and know where the kitchen is.</p>
    </article>
    <article class="card">
      <h3>In-house catering</h3>
      <p>Food actually served here, by a kitchen that works this estate every weekend.</p>
    </article>
    <article class="card">
      <h3>Where everyone sleeps</h3>
      <p>Thirty-four people stay on the estate. A hotel is six minutes away for everyone
         else, and the airport is thirty.</p>
    </article>
    <article class="card">
      <h3>Your own team, welcome</h3>
      <p>Bring your planner and your vendors. We would rather support your plan than
         replace it. <a href="/thevalley/planners/">For planners</a>.</p>
    </article>
  </div>
</section>
""")

PAGES["weddings/real-weddings/index.html"] = dict(
    nav="Weddings", title="Real Weddings | %s" % SITE,
    desc="Weddings that have happened on the estate.",
    hero_img="real-weddings.webp", hero_alt="A couple in the meadow at golden hour",
    eyebrow="Celebrate &middot; Real weddings",
    h1="Weddings that happened here.",
    standfirst="Each one credited to the couple, the planner, the photographer and the "
               "vendors who made it &mdash; which is also how a vendor list earns its referrals.",
    body="""
<section>
  <div class="lede">
    <h2>Gallery</h2>
    <p>This page holds the real-weddings gallery. It is intentionally empty in the
       prototype: the framework asks for current work only, credited, and refreshed as
       weddings happen rather than left to age.</p>
  </div>
  <div class="note">
    <p><b>Awaiting content.</b> Needs a first set of six to eight weddings with the couple's
       permission, the vendor credits, and photography from the current season. Nothing from
       before the property changed.</p>
  </div>
</section>
""")

PAGES["weddings/single-day/index.html"] = dict(
    nav="Weddings", title="Single-Day Celebrations | %s" % SITE,
    desc="A single-day celebration on the estate.",
    hero_img="single-day.webp", hero_alt="The meadow, quiet, with the ridge beyond",
    eyebrow="Celebrate &middot; Single day",
    h1="A day, rather than a weekend.",
    standfirst="Not every celebration wants two nights. The estate still closes around one "
               "couple for the day, and nothing is shared.",
    body="""
<section>
  <div class="lede">
    <h2>What stays the same</h2>
    <p>One celebration on the property. The whole estate to move through. The same
       inclusions, the same weather alternatives, the same people running it.</p>
    <h2>What is different</h2>
    <p>No lodging night, no rehearsal evening, and no breakfast the morning after &mdash;
       which is to say, none of the parts most couples tell us afterwards they did not
       expect to love.</p>
    <a class="btn" href="/thevalley/weddings/">See the Estate Weekend</a>
  </div>
  <div class="note">
    <p><b>Positioning note.</b> This is a real offering and should convert, but the framework
       is explicit that it must not appear in the brand essence, the hero, or the homepage
       story. The weekend is the differentiator.</p>
  </div>
</section>
""")

PAGES["stay/index.html"] = dict(
    nav="Stay", title="Stay | %s" % SITE,
    desc="Private mountainside lodging on a 74-acre estate near Chattanooga.",
    hero_img="stay.webp", hero_alt="A cottage in the woods at the edge of the property",
    eyebrow="Stay",
    h1="Stay Where the Story Continues",
    standfirst="The cottages are open when there is no wedding on the property. A creek, a "
               "waterfall, two and a half miles of trails, and the oldest mountain range on "
               "earth outside the door.",
    actions=[("Enquire about a stay", "/thevalley/book-a-tour/")],
    body="""
<section>
  <div class="lede">
    <h2>Come for a weekend. Come back for an anniversary.</h2>
    <p>Or come once, look around, and start imagining something larger. A guest who stays
       two nights has seen the whole estate &mdash; which is how a good many weddings here
       begin.</p>
  </div>
  <ul class="named">
    <li>Phoenix <span>Cottage</span></li>
    <li>Bluebird <span>Cottage</span></li>
    <li>Goldfinch <span>Cottage</span></li>
    <li>Hummingbird <span>Cottage</span></li>
    <li>Willow <span>Cottage</span></li>
    <li>Mahogany <span>Cottage</span></li>
    <li>Overlook Village <span>Cottages on the hill</span></li>
    <li>The Lodge <span>The larger house</span></li>
  </ul>
  <div class="note">
    <p><b>Deliberately not listed here:</b> Lost in the Woods. The framework folds it into
       the Estate Weekend as the emotional close, rather than offering it as a separate
       bookable stay.</p>
  </div>
</section>

<section>
  <div class="lede">
    <div class="eyebrow">Come back</div>
    <h2>Return and anniversary stays.</h2>
    <p>First, fifth and tenth anniversaries for every couple married here. Vow renewals,
       proposal weekends, return stays for the wedding party, and off-season rates between
       Saturdays.</p>
  </div>
</section>
""")

PAGES["the-estate/index.html"] = dict(
    nav="The Estate", title="The Estate | %s" % SITE,
    desc="Seventy-four acres beneath Lookout Mountain, as one property.",
    hero_img="estate.webp", hero_alt="The meadow opening beneath the ridge, the deck at its edge",
    eyebrow="One estate",
    h1="One property, one map, one path.",
    standfirst="This page replaces a dropdown that listed four venues. There are not four "
               "venues. There is one estate, and every celebration includes all of it.",
    body="""
<section>
  <div class="split">
    <div class="split-text">
      <div class="eyebrow">Arrival</div>
      <h2>Magnolia House</h2>
      <p>White columns and glass against the ridge, at the top of the drive. It is the first
         photograph almost every guest takes, through the windshield on the way up. The
         conservatory at Magnolia House is also the weather plan that costs nothing.</p>
    </div>
    <img src="/thevalley/assets/img/magnolia-house.webp" alt="Magnolia House, white columns above the lawn" loading="lazy">
  </div>
</section>

<section>
  <div class="split flip">
    <div class="split-text">
      <div class="eyebrow">Ceremony</div>
      <h2>The Valley</h2>
      <p>An open meadow held on three sides by ridgeline, with Lookout Mountain beyond.
         Sound stays in it and the wind drops in it. Nothing is visible from it that the
         estate does not own.</p>
    </div>
    <img src="/thevalley/assets/img/the-valley.webp" alt="The processional crossing the meadow" loading="lazy">
  </div>
</section>

<section>
  <div class="split">
    <div class="split-text">
      <div class="eyebrow">Cocktails</div>
      <h2>The Lookout Deck</h2>
      <p>A railed deck out over the valley, facing the mountain. It turns gold at six, tip
         to tip, and everyone stops talking.</p>
    </div>
    <img src="/thevalley/assets/img/lookout-deck.webp" alt="A couple dancing on the Lookout Deck, the ridge behind" loading="lazy">
  </div>
</section>

<section>
  <div class="split flip">
    <div class="split-text">
      <div class="eyebrow">Reception</div>
      <h2>Davis Hall</h2>
      <p>Drapery, chandeliers, and the room where the dancing happens. It carries the
         largest receptions on the property.</p>
    </div>
    <img src="/thevalley/assets/img/davis-hall.webp" alt="Davis Hall under its drapery, lit for the first dance" loading="lazy">
  </div>
</section>

<section>
  <div class="lede">
    <div class="eyebrow">The ground itself</div>
    <h2>And underneath the drawing, the actual ground.</h2>
    <p>A model of the real surface of the property, built from survey elevation readings and
       turned so the valley can be looked at from any side.</p>
    <a class="btn" href="/valleyvenues/concepts/map3d/">Open the terrain model</a>
  </div>
  <div class="note">
    <p><b>Still in prototype.</b> Elevation is USGS 3DEP one-metre LiDAR through The National
       Map; the imagery over it is USGS NAIP, October 2023, at 0.57&thinsp;m per pixel. Both
       are public domain federal survey data. The markers are read from aerial photography
       rather than from a site plan.</p>
  </div>
</section>
""")

PAGES["planners/index.html"] = dict(
    nav="Planners", title="For Planners | %s" % SITE,
    desc="Site logistics, load-in and how a weekend runs at The Valley Venues.",
    hero_img="planners.webp", hero_alt="The estate from the deck, looking down the valley",
    eyebrow="For planners",
    h1="Bring your vision. We know the estate.",
    standfirst="Planners send couples here repeatedly once they trust the operation. This "
               "page is written to your lens rather than the bride's.",
    actions=[("Register as a planner", "/thevalley/book-a-tour/"),
             ("Preferred vendors", "/thevalley/planners/vendors/")],
    body="""
<section>
  <div class="grid">
    <article class="card">
      <h3>Site logistics</h3>
      <p>Load-in access, vehicle routes on the property, power, kitchen access, and where
         the golf carts live. <em>Detail to be confirmed with the operations team.</em></p>
    </article>
    <article class="card">
      <h3>How the weekend runs</h3>
      <p>What the estate handles and what it expects you to handle, hour by hour, from
         Friday load-in to Sunday clear.</p>
    </article>
    <article class="card">
      <h3>Staff handoffs</h3>
      <p>Who you speak to, when, and who is on the property overnight.</p>
    </article>
    <article class="card">
      <h3>Weather alternatives</h3>
      <p>Every indoor and covered option with real capacities, and the call time for a
         decision.</p>
    </article>
    <article class="card">
      <h3>Parking and guest movement</h3>
      <p>Arrival flow, level walking routes, and transport between spaces.</p>
    </article>
    <article class="card">
      <h3>We would rather support your plan</h3>
      <p>Than replace it. The estate has an in-house team, and it is used to working
         alongside a planner rather than instead of one.</p>
    </article>
  </div>
  <div class="note">
    <p><b>Prototype note.</b> This page carries its own capture, and that list is tagged and
       worked separately from bridal enquiries. The operational detail above needs filling in
       from the team &mdash; it is the part planners actually read.</p>
  </div>
</section>
""")

PAGES["planners/vendors/index.html"] = dict(
    nav="Planners", title="Preferred Vendors | %s" % SITE,
    desc="Planners and vendors who know the estate.",
    hero_img="vendors.webp", hero_alt="An invitation suite and two rings",
    eyebrow="For planners &middot; Preferred vendors",
    h1="The people who know this property.",
    standfirst="Most couples reach this site before they have hired a planner. This list "
               "puts one in front of a couple who has already chosen the estate.",
    body="""
<section>
  <div class="lede">
    <h2>Planners</h2>
    <p>Each entry carries a name, a studio, a website and a social handle.</p>
  </div>
  <ul class="named">
    <li>Planner name <span>Studio &middot; website &middot; social</span></li>
    <li>Planner name <span>Studio &middot; website &middot; social</span></li>
    <li>Planner name <span>Studio &middot; website &middot; social</span></li>
  </ul>
  <div class="lede" style="margin-top:2.5rem">
    <h2>Vendors</h2>
    <p>Photography, florals, music, hair and makeup, rentals, officiants.</p>
  </div>
  <ul class="named">
    <li>Vendor name <span>Category &middot; website &middot; social</span></li>
    <li>Vendor name <span>Category &middot; website &middot; social</span></li>
    <li>Vendor name <span>Category &middot; website &middot; social</span></li>
  </ul>
  <div class="note">
    <p><b>Why this page exists.</b> Being listed here gives a planner cause to name the estate
       on her own site and in her guides. The referral runs both directions, and the estate
       holds the list.</p>
  </div>
</section>
""")

PAGES["about/index.html"] = dict(
    nav="About", title="About | %s" % SITE,
    desc="The family behind the estate, and the design thinking behind the experience.",
    hero_img="about.webp", hero_alt="Magnolia House, columns and glass against the ridge",
    eyebrow="About",
    h1="The Question Behind Every Room",
    standfirst="A family estate, and a design philosophy that starts somewhere unusual for a "
               "wedding venue: not with how a room looks, but with how a person will feel "
               "standing in it.",
    body="""
<section>
  <div class="lede">
    <div class="eyebrow">Kobi Cummings</div>
    <h2>Co-founder, certified wedding planner, experiential designer.</h2>
    <p>Kobi holds a Bachelor of Fine Arts in production design from the Savannah College of
       Art and Design, with a minor in themed entertainment, and worked at Disney Live
       Entertainment as an arts specialist on shows, parades, props and environments &mdash;
       all of them built around one question. <em>What should the guest feel in this
       moment?</em></p>
    <p>It is the same question she asks about the moment the doors open and everyone turns
       around. Whoever sits closest to the dance floor is in every photograph of your first
       dance. That should be someone you love.</p>
  </div>
  <div class="note">
    <p><b>Approval required.</b> This wording follows Draft 2 of the brand framework and needs
       approving word for word before it appears publicly. Claims stay first person and
       factual, with no sole credit anywhere.</p>
  </div>
</section>

<section>
  <div class="lede">
    <div class="eyebrow">The family</div>
    <h2>A family story, still.</h2>
    <p>Paul Cummings bought the property for another purpose entirely. Over time he and his
       daughter Kobi began restoring and reimagining it, and what emerged was not a
       collection of event spaces but a hospitality estate.</p>
    <p>The estate should grow without anyone becoming a room number. Clients are known here.</p>
  </div>
</section>
""")

PAGES["book-a-tour/index.html"] = dict(
    nav=None, title="Book a Tour | %s" % SITE,
    desc="Reserve a tour of the estate.",
    eyebrow="Book a tour",
    h1="Come and stand in it.",
    standfirst="More than half of the couples who walk this property book it. Tell us a "
               "little about the weekend you are imagining and we will tell you what "
               "actually fits.",
    body="""
<section>
  <form class="form" action="#" method="post" onsubmit="return false">
    <div class="field">
      <label for="name">Your name</label>
      <input id="name" name="name" type="text" autocomplete="name">
    </div>
    <div class="field">
      <label for="email">Email</label>
      <input id="email" name="email" type="email" autocomplete="email">
    </div>
    <div class="field">
      <label for="date">Your date, or the season you are considering</label>
      <input id="date" name="date" type="text" placeholder="October 2027, or just &ldquo;autumn&rdquo;">
    </div>
    <div class="field">
      <label for="count">Roughly how many people</label>
      <input id="count" name="count" type="text" placeholder="An estimate is fine">
    </div>
    <div class="field">
      <label for="shape">A weekend, or a single day?</label>
      <select id="shape" name="shape">
        <option>The whole weekend</option>
        <option>A single day</option>
        <option>Not sure yet</option>
      </select>
    </div>
    <div class="field">
      <label for="staying">Who is staying on the property with you?</label>
      <input id="staying" name="staying" type="text" placeholder="Wedding party, immediate family, everyone">
    </div>
    <div class="field">
      <label for="feel">What do you want the weekend to feel like?</label>
      <textarea id="feel" name="feel" placeholder="In your own words."></textarea>
    </div>
    <button class="btn btn-solid" type="submit">Request a tour</button>
  </form>

  <div class="note">
    <p><b>Prototype note.</b> The form does not submit. Note what it does not ask: your total
       budget. That question closes more doors than it filters, and guest count arrives
       naturally here anyway &mdash; after you have described what you want, rather than as
       the price of entry.</p>
    <p>What should come back is a recommendation naming the two or three configurations that
       fit, priced, in the brand voice, and signed by Kobi &mdash; within minutes rather than
       a pamphlet within seconds.</p>
  </div>
</section>
""")


# --------------------------------------------------------------------- write
for path, page in PAGES.items():
    dest = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    html = shell(page)
    open(dest, "w", encoding="utf-8").write(html)
    print("%-44s %5d bytes" % (path, len(html)))

print("\n%d pages" % len(PAGES))

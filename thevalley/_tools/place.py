"""
Cut the site's images from the sorted library.

Each slot on the site has a job — a full-bleed hero, a section beside text, a
card in a row — and a job implies a width and an aspect. Rather than resize by
hand every time a choice changes, the slots are listed here and rebuilt from
the originals in one pass.

    python thevalley/_tools/place.py

Chosen from the contact sheets in _triage/picks. Nothing is invented: if an
original is smaller than the slot asks for, the slot gets what exists.
"""
import os
from PIL import Image, ImageStat, ImageEnhance

LIB = r"D:/DevStuff/VV Images/Sorted"
OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "assets", "img")

# (destination, category folder, filename, width, height, vertical bias)
SLOTS = [
    # --- the home page --------------------------------------------------
    # The aisle set and waiting, with the ridge behind it. An empty meadow
    # says "held for you" in a way a crowded one cannot.
    ("hero-mountain", "02 The Valley", "WeddingDay-648.jpg", 2200, 1100, 0.50),

    # --- the estate -----------------------------------------------------
    ("estate",         "01 Mountain & landscape", "ValleyVenuesStyledShoot-062.jpg", 2200, 1100, 0.52),
    ("magnolia-house", "03 Magnolia House",       "ValleyVenuesStyledShoot-106.jpg", 1600, 1200, 0.50),
    ("the-valley",     "02 The Valley",           "WeddingDay-781.jpg",             1600, 1200, 0.50),
    ("lookout-deck",   "04 Lookout Deck",         "WeddingDay-1419.jpg",            1600, 1200, 0.48),
    # Interiors only, dressed, drapery and chandeliers lit — the direction is
    # explicit that Davis Hall is earned rather than led with.
    ("davis-hall",     "05 Davis Hall",           "WeddingDay-1272.jpg",            1600, 1200, 0.50),

    # --- weddings -------------------------------------------------------
    ("weddings",       "02 The Valley",           "SneakPeek-10.jpg",               2000, 1000, 0.52),
    # The conservatory is the answer to "what happens if it rains", so it
    # carries the page that answers it.
    ("included",       "03 Magnolia House",       "ValleyVenueSSSneakPeaks-46.jpg", 2000, 1000, 0.50),
    ("real-weddings",  "09 People & candid",      "0B6A1619.jpg",                   2000, 1000, 0.45),
    ("single-day",     "02 The Valley",           "ValleyVenueSSSneakPeaks-17.jpg", 2000, 1000, 0.50),

    # --- stay, planners, about -------------------------------------------
    # Only 1600px exists for the cottages; the slot takes what there is.
    ("stay",           "06 Lodging & cottages",   "Valley-Venues-Wedding-Day-1-9.jpg", 1600, 800, 0.46),
    ("planners",       "01 Mountain & landscape", "ValleyVenuesStyledShoot-061.jpg", 2000, 1000, 0.52),
    ("vendors",        "08 Details & decor",      "WeddingDay-20.jpg",              2000, 1000, 0.50),
    ("about",          "03 Magnolia House",       "ValleyVenuesStyledShoot-124.jpg", 2000, 1000, 0.46),
]

TARGET = 0.55          # the set is nudged toward one mean so the pages agree


def find(cat, name):
    for orient in ("landscape", "portrait", "square"):
        p = os.path.join(LIB, cat, orient, name)
        if os.path.exists(p):
            return p
    return None


total = 0
for dest, cat, name, W, H, bias in SLOTS:
    src = find(cat, name)
    if not src:
        print("MISSING  %-16s %s / %s" % (dest, cat, name))
        continue
    im = Image.open(src)
    im.draft("RGB", (W * 2, H * 2))
    im = im.convert("RGB")
    if im.width < W:                      # never invent pixels
        H = int(H * im.width / float(W))
        W = im.width
    r = max(W / float(im.width), H / float(im.height))
    im = im.resize((max(W, int(im.width * r)), max(H, int(im.height * r))), Image.LANCZOS)
    x = (im.width - W) // 2
    y = int((im.height - H) * bias)
    im = im.crop((x, y, x + W, y + H))

    lum = ImageStat.Stat(im.convert("L")).mean[0] / 255.0
    if lum < 0.46 or lum > 0.66:
        im = ImageEnhance.Brightness(im).enhance(max(0.85, min(1.25, TARGET / lum)))

    path = os.path.join(OUT, dest + ".webp")
    im.save(path, quality=82, method=5)
    kb = os.path.getsize(path) // 1024
    total += kb
    print("%-16s %4dx%-4d %4dKB   %s" % (dest, W, H, kb, name))

print("\n%d slots, %d KB total" % (len(SLOTS), total))

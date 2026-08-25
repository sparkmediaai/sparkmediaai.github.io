"""
Turn the client's drop folder into a shared, web-ready pool for the style pages.

Originals stay outside the repo (C:/Users/dave.mccormick/vv-photos) — several are
16MB camera files. Only the optimised WebP land here.

Names are semantic, so swapping in better photography later is a filename match
rather than a hunt through five pages.
"""
import os
from PIL import Image

SRC = r"C:/Users/dave.mccormick/vv-photos"
OUT = os.path.dirname(os.path.abspath(__file__))

WIDE, HERO, Q = 1400, 2200, 62

# source file -> (semantic name, is_hero)
MAP = [
    ("DJI_0679.jpg",                                            "aerial-valley",    True),
    ("Copy of the-valley-venues-kristen-Thomison-photo-101.jpg","deck-ceremony",    True),
    ("StyledShootFall2024-127.jpg",                             "valley-autumn",    True),
    ("9G9A9309-Enhanced-NR-2.jpg",                              "fog-walk",         True),
    ("2024_7_25_SKP-280.jpg",                                   "manor-lawn",       True),
    ("2024_7_25_SKP-278.jpg",                                   "manor",            False),
    ("valleyceremony-11.jpg",                                   "valley-arch",      False),
    ("valleyceremony-17.jpg",                                   "valley-couple",    False),
    ("StyledShootFall2024-126.jpg",                             "valley-walk",      False),
    ("StyledShootFall2024-144.jpg",                             "manor-front",      False),
    ("StyledShootFall2024-153.jpg",                             "columns-ridge",    False),
    ("StyledShootFall2024-54.jpg",                              "arch-florals",     False),
    ("StyledShootFall2024-82.jpg",                              "deck-table",       False),
    ("ENGAGEMENT-119.jpg",                                      "meadow-pair",      False),
    ("ENGAGEMENT-175.jpg",                                      "manor-side",       False),
    ("ENGAGEMENT-177.jpg",                                      "manor-couple",     False),
    ("ENGAGEMENT-42.jpg",                                       "meadow-house",     False),
    ("ENGAGEMENT-90.jpg",                                       "field-lift",       False),
    ("3I0A4529vh.jpg",                                          "deck-couple",      False),
    ("3I0A4579vh.jpg",                                          "deck-portrait",    False),
    ("3I0A4867vh.jpg",                                          "bride-meadow",     False),
    ("4K6A0055anthonyalexa.jpg",                                "garden-urn",       False),
    ("DSC04328.jpg",                                            "deck-rain",        False),
    ("magnoliahouse-36.jpg",                                    "garden-dip",       False),
    ("untitled-42.jpg",                                         "vintage-car",      False),
    ("untitled-61.jpg",                                         "blue-truck",       False),
]

total = 0
missing = []
for src, name, hero in MAP:
    p = os.path.join(SRC, src)
    if not os.path.exists(p):
        missing.append(src)
        continue
    im = Image.open(p).convert("RGB")
    target = HERO if hero else WIDE
    if im.width > target:
        im = im.resize((target, round(im.height * target / im.width)), Image.LANCZOS)
    dst = os.path.join(OUT, name + ".webp")
    im.save(dst, quality=Q, method=5)
    kb = os.path.getsize(dst) // 1024
    total += kb
    print("  %-16s %5dx%-5d %5dKB%s" % (name, im.width, im.height, kb, "  HERO" if hero else ""))

print()
print("files:", len(MAP) - len(missing), "| total:", round(total / 1024, 1), "MB")
if missing:
    print("MISSING:", missing)

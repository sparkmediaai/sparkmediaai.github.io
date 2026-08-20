"""
Build a scroll-driven image sequence that scrubs through the WEEKEND, not
through one scene's lighting.

Each moment of the timeline gets a span of frames. Inside a span the frame
slowly pushes in (a Ken Burns move, so it reads as motion rather than a
slideshow); across a span boundary it cross-dissolves into the next moment.
Every moment is graded to its hour, so the light travels Friday afternoon ->
night -> Saturday morning -> golden hour -> night -> Sunday morning.

Output is WebP: roughly 40% smaller than equivalent JPEG, which is what makes
a sequence this long affordable. f000 is ALSO written as JPEG to serve as the
CSS poster for browsers that never run the canvas.

Real photography replaces these 1:1 by filename - the frame count and spans
are the contract, not the source images.
"""
import os, math
from PIL import Image, ImageEnhance, ImageStat

ROOT = r"C:/Users/dave.mccormick/Something/valleyvenues"
SRC  = ROOT + "/assets/images"
OUT  = ROOT + "/concepts/a/seq"

W, H       = 1200, 675        # 16:9
QUALITY    = 50
PER_MOMENT = 8                # frames per moment
DISSOLVE   = 0.42             # last 42% of a span cross-fades into the next
ZOOM       = 0.075            # push-in across a span

# image, tint (rgb), tint amount, TARGET mean luminance (0-255), saturation
#
# Brightness is solved for, not hand-set: each frame is measured and scaled to
# hit its target. Hand-picked multipliers depend on how bright the source photo
# happens to be, which is exactly the thing that changes when real photography
# arrives. Targets describe the HOUR; the solver makes any photo obey it.
MOMENTS = [
    ("dark-valley.jpg",      (224,164, 88), .10, 165, 1.10),  # 4:00 arrive
    ("tv-gardenparty.jpg",   (232,168, 92), .14, 175, 1.12),  # 6:00 rehearse
    ("lg-0005.jpg",          ( 24, 34, 52), .28,  70, 0.80),  # 9:30 fire
    ("g-bride-mirror.jpg",   (218,226,235), .10, 185, 0.96),  # 9:00 ready
    ("tv-hero.jpg",          (226,170,102), .10, 172, 1.10),  # 4:30 ceremony
    ("ld-hero.jpg",          (236,158, 74), .18, 156, 1.16),  # 5:30 cocktails
    ("dh-table-setting.jpg", (232,176, 96), .16, 122, 1.06),  # 7:00 dinner
    ("dh-toast.jpg",         (214,150, 78), .18,  94, 1.00),  # 9:00 dancing
    ("ld-fog.jpg",           ( 20, 32, 56), .38,  42, 0.72),  # 11:30 retreat
    ("mh-patio.jpg",         (226,228,224), .08, 180, 0.98),  # 9:00 breakfast
    ("mh-gardenparty.jpg",   (222,214,196), .06, 190, 1.04),  # 11:00 depart
]

N = len(MOMENTS) * PER_MOMENT
os.makedirs(OUT, exist_ok=True)


def load(name):
    im = Image.open(os.path.join(SRC, name)).convert("RGB")
    bw, bh = im.size
    t = W / H
    if bw / bh > t:
        nw = int(bh * t)
        im = im.crop(((bw - nw) // 2, 0, (bw - nw) // 2 + nw, bh))
    else:
        nh = int(bw / t)
        im = im.crop((0, (bh - nh) // 2, bw, (bh - nh) // 2 + nh))
    # oversample so the push-in never upscales past native
    return im.resize((int(W * (1 + ZOOM)), int(H * (1 + ZOOM))), Image.LANCZOS)


def mean_lum(im):
    return ImageStat.Stat(im.convert("L")).mean[0]


def grade(im, tint, amt, target, sat):
    im = Image.blend(im, Image.new("RGB", im.size, tint), amt)
    im = ImageEnhance.Color(im).enhance(sat)
    cur = mean_lum(im)
    # Solve brightness for the target, clamped so a very dark or very blown
    # source degrades gracefully instead of turning to mud or paper.
    factor = 1.0 if cur < 1 else max(0.25, min(2.2, target / cur))
    im = ImageEnhance.Brightness(im).enhance(factor)
    return im


BASE = [grade(load(m[0]), m[1], m[2], m[3], m[4]) for m in MOMENTS]
for m, b in zip(MOMENTS, BASE):
    print("  %-22s target %3d -> actual %3d" % (m[0], m[3], round(mean_lum(b))))


def framed(idx, local):
    """One moment's image at push-in position `local` (0..1), cropped to W x H."""
    src = BASE[idx]
    sw, sh = src.size
    scale = 1 + ZOOM * (1 - local)          # starts wide, closes in
    cw, ch = int(W * scale / (1 + ZOOM) * (1 + ZOOM)), 0
    cw = int(sw / scale)
    ch = int(sh / scale)
    left = (sw - cw) // 2
    top = (sh - ch) // 2
    return src.crop((left, top, left + cw, top + ch)).resize((W, H), Image.LANCZOS)


for i in range(N):
    m = min(i // PER_MOMENT, len(MOMENTS) - 1)
    local = (i % PER_MOMENT) / (PER_MOMENT - 1) if PER_MOMENT > 1 else 0
    img = framed(m, local)

    if local > (1 - DISSOLVE) and m < len(MOMENTS) - 1:
        a = (local - (1 - DISSOLVE)) / DISSOLVE
        a = a * a * (3 - 2 * a)                      # smoothstep
        img = Image.blend(img, framed(m + 1, 0.0), a)

    img.save(os.path.join(OUT, "f%03d.webp" % i), quality=QUALITY, method=5)
    if i == 0:
        img.save(os.path.join(OUT, "poster.jpg"), quality=70, optimize=True, progressive=True)

files = [f for f in os.listdir(OUT) if f.endswith(".webp")]
total = sum(os.path.getsize(os.path.join(OUT, f)) for f in files)
print("moments:", len(MOMENTS), "| frames:", len(files))
print("total KB:", round(total / 1024), "| avg KB:", round(total / len(files) / 1024, 1))
print("poster KB:", round(os.path.getsize(os.path.join(OUT, "poster.jpg")) / 1024))

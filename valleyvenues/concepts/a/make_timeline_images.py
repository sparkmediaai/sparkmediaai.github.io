"""
Grade each timeline photo to the hour it depicts.

The timeline's section backgrounds walk from afternoon cream through Friday
night, a pale Saturday morning, golden hour, dinner, dancing, deep night and
out to a bright Sunday. Ungraded stock-bright photos sitting on the dark
sections look pasted on, so each image is graded to sit in its own light.

Brightness is SOLVED, not hand-set: every moment declares the mean luminance
of its hour and the generator measures the image and scales to hit it. That
means real photography can be dropped in at any exposure and still land on
the arc - swap the source filename, rerun, done.

Output: img/m00.webp ... m10.webp
"""
import os
from PIL import Image, ImageEnhance, ImageStat

ROOT = r"C:/Users/dave.mccormick/Something/valleyvenues"
SRC  = ROOT + "/assets/images"
OUT  = ROOT + "/concepts/a/img"

W, H    = 1500, 1000       # 3:2
QUALITY = 62

# source, tint (rgb), tint amount, TARGET mean luminance, saturation
MOMENTS = [
    ("venue-the-valley.jpg", (226,170, 96), .09, 150, 1.08),  # 4:00 arrive
    ("tv-gardenparty.jpg",   (232,168, 92), .12, 160, 1.10),  # 6:00 rehearse
    ("lg-0005.jpg",          ( 26, 38, 56), .26,  72, 0.84),  # 9:30 fire      DARK
    ("g-bride-mirror.jpg",   (220,228,236), .08, 168, 0.98),  # 9:00 ready
    ("tv-hero.jpg",          (228,174,108), .09, 158, 1.10),  # 4:30 ceremony
    ("ld-hero.jpg",          (238,162, 78), .17, 150, 1.18),  # 5:30 golden
    ("dh-table-setting.jpg", (234,180,102), .15, 118, 1.06),  # 7:00 dinner    DIM
    ("dh-toast.jpg",         (216,152, 80), .17,  92, 1.00),  # 9:00 dancing   DARK
    ("ld-fog.jpg",           ( 18, 30, 54), .36,  48, 0.74),  # 11:30 retreat  DARKEST
    ("mh-patio.jpg",         (228,230,226), .07, 170, 0.98),  # 9:00 breakfast
    ("map-valley.jpg",       (224,216,198), .06, 185, 1.04),  # 11:00 depart
]

os.makedirs(OUT, exist_ok=True)


def mean_lum(im):
    return ImageStat.Stat(im.convert("L")).mean[0]


def cover(im, w, h):
    bw, bh = im.size
    t = w / h
    if bw / bh > t:
        nw = int(bh * t)
        im = im.crop(((bw - nw) // 2, 0, (bw - nw) // 2 + nw, bh))
    else:
        nh = int(bw / t)
        im = im.crop((0, (bh - nh) // 2, bw, (bh - nh) // 2 + nh))
    return im.resize((w, h), Image.LANCZOS)


for i, (name, tint, amt, target, sat) in enumerate(MOMENTS):
    im = cover(Image.open(os.path.join(SRC, name)).convert("RGB"), W, H)
    im = Image.blend(im, Image.new("RGB", im.size, tint), amt)
    im = ImageEnhance.Color(im).enhance(sat)

    cur = mean_lum(im)
    factor = 1.0 if cur < 1 else max(0.25, min(2.2, target / cur))
    im = ImageEnhance.Brightness(im).enhance(factor)

    # a touch of contrast back after a heavy brightness push
    if factor > 1.4 or factor < 0.7:
        im = ImageEnhance.Contrast(im).enhance(1.06)

    path = os.path.join(OUT, "m%02d.webp" % i)
    im.save(path, quality=QUALITY, method=5)
    print("  m%02d %-22s target %3d -> %3d  (x%.2f)  %3dKB"
          % (i, name, target, round(mean_lum(im)), factor,
             round(os.path.getsize(path) / 1024)))

total = sum(os.path.getsize(os.path.join(OUT, f)) for f in os.listdir(OUT) if f.endswith(".webp"))
print("total KB:", round(total / 1024))

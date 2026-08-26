"""
Generate a golden-hour -> dusk -> night frame sequence from a single still.

This is a PROTOTYPE stand-in for real timelapse footage: it proves the
scroll-scrub mechanic and the grade arc, so tomorrow's shoot drops into a
slot that already works. Real frames should replace these 1:1 by filename.
"""
import os, math
from PIL import Image, ImageEnhance

SRC = r"C:/Users/dave.mccormick/Something/valleyvenues/assets/images/tv-hero.jpg"
OUT = r"C:/Users/dave.mccormick/Something/valleyvenues/concepts/b/seq"
N = 48
W, H = 1200, 675          # 16:9
QUALITY = 62

os.makedirs(OUT, exist_ok=True)

base = Image.open(SRC).convert("RGB")
# centre-crop to 16:9 then resize
bw, bh = base.size
target = W / H
if bw / bh > target:
    nw = int(bh * target)
    base = base.crop(((bw - nw) // 2, 0, (bw - nw) // 2 + nw, bh))
else:
    nh = int(bw / target)
    base = base.crop((0, (bh - nh) // 2, bw, (bh - nh) // 2 + nh))
base = base.resize((W, H), Image.LANCZOS)

# radial vignette mask (1.0 centre -> 0.0 corners)
vig = Image.new("L", (W, H))
cx, cy = W / 2, H / 2
maxd = math.hypot(cx, cy)
px = vig.load()
for y in range(H):
    for x in range(W):
        d = math.hypot(x - cx, y - cy) / maxd
        px[x, y] = int(max(0.0, 1.0 - d ** 2) * 255)

AMBER = Image.new("RGB", (W, H), (224, 164, 88))
NIGHT = Image.new("RGB", (W, H), (14, 26, 42))


def lerp(a, b, t):
    return a + (b - a) * t


for i in range(N):
    t = i / (N - 1)                      # 0 = golden hour, 1 = night
    f = base

    # colour cast: warm early, cold late, crossing at t=0.45
    if t < 0.45:
        f = Image.blend(f, AMBER, lerp(0.16, 0.05, t / 0.45))
    else:
        f = Image.blend(f, NIGHT, lerp(0.02, 0.46, (t - 0.45) / 0.55))

    f = ImageEnhance.Brightness(f).enhance(lerp(1.06, 0.30, t ** 1.25))
    f = ImageEnhance.Color(f).enhance(lerp(1.14, 0.52, t))
    f = ImageEnhance.Contrast(f).enhance(lerp(1.00, 1.14, t))

    # vignette deepens after dark
    amt = lerp(0.05, 0.42, t)
    if amt > 0:
        dark = ImageEnhance.Brightness(f).enhance(1 - amt)
        f = Image.composite(f, dark, vig)

    f.save(os.path.join(OUT, "f%03d.jpg" % i), quality=QUALITY, optimize=True, progressive=True)

total = sum(os.path.getsize(os.path.join(OUT, n)) for n in os.listdir(OUT))
sizes = [os.path.getsize(os.path.join(OUT, n)) for n in sorted(os.listdir(OUT))]
print("frames:", len(sizes))
print("total KB:", round(total / 1024))
print("avg KB:", round(total / len(sizes) / 1024, 1))
print("largest KB:", round(max(sizes) / 1024, 1))

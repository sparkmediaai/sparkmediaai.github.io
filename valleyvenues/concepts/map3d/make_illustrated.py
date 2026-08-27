"""
Derive an illustrated skin from the aerial photograph.

The raw NAIP frame is truthful but muddy — it is a satellite image, not a
designed one. This classifies every pixel by what it actually is (woodland,
mown grass, bare ground and track, water) and repaints it in the estate's own
palette, so the model can wear something that looks drawn while still being
derived pixel-for-pixel from the real land.

Classification is deliberately crude — greenness, brightness, saturation — but
NAIP over rural Georgia separates cleanly on those axes.
"""
import os
from PIL import Image, ImageFilter

HERE = os.path.dirname(os.path.abspath(__file__))
src = Image.open(os.path.join(HERE, "aerial.webp")).convert("RGB")

# soften first: we want land types, not individual trees
work = src.filter(ImageFilter.MedianFilter(size=7))
W, H = work.size
px = work.load()

# estate palette
WOOD_D = (46, 66, 48)      # deep canopy
WOOD_L = (74, 96, 66)      # sunlit canopy
GRASS_D = (140, 152, 104)  # mown, in shade
GRASS_L = (178, 184, 130)  # mown, in sun
BARE = (208, 196, 168)     # track, gravel, bare ground
WATER = (120, 148, 162)

out = Image.new("RGB", (W, H))
op = out.load()

for y in range(H):
    for x in range(W):
        r, g, b = px[x, y]
        mx, mn = max(r, g, b), min(r, g, b)
        sat = (mx - mn) / mx if mx else 0
        lum = (r * 0.299 + g * 0.587 + b * 0.114) / 255.0
        green = g - (r + b) / 2                       # how green, regardless of exposure

        # Water has to be emphatically blue. A loose test reads shadowed canopy
        # as water and speckles the whole woodland with ponds.
        if (b - g) > 16 and (b - r) > 16 and lum > 0.28:
            c = WATER
        elif sat < 0.14 and lum > 0.45:
            c = BARE                                   # roads, gravel, roofs
        elif green > 14 and lum < 0.42:
            c = WOOD_D
        elif green > 10:
            c = WOOD_L if lum > 0.52 else WOOD_D
        else:
            c = GRASS_L if lum > 0.5 else GRASS_D

        # keep a little of the original modulation so it isn't posterised flat
        k = 0.16
        op[x, y] = (
            int(c[0] * (1 - k) + r * k),
            int(c[1] * (1 - k) + g * k),
            int(c[2] * (1 - k) + b * k),
        )

out = out.filter(ImageFilter.SMOOTH)
out.save(os.path.join(HERE, "illustrated.webp"), quality=82, method=5)
print("illustrated.webp %dx%d  %d KB" % (W, H, os.path.getsize(os.path.join(HERE, "illustrated.webp")) // 1024))

"""Erzeugt cover-de / cover-en (+ cover-web-*.jpg) aus docs/podcast/cover.png – nur die Texte werden ersetzt.

Aufruf: python podcast/tools/make_covers.py docs/podcast   (braucht pillow, numpy, scipy)
"""
import sys
from pathlib import Path
import numpy as np
from PIL import Image, ImageDraw, ImageFont

SITE = Path(sys.argv[1])
F = "/usr/share/fonts/opentype/inter/InterDisplay-%s.otf"
src = Image.open(SITE / "cover.png").convert("RGB")
A = np.array(src).astype(int)
white = (A[..., 0] > 215) & (A[..., 1] > 215) & (A[..., 2] > 215)
redm = (A[..., 0] > 200) & (A[..., 1] < 80) & (A[..., 2] < 90)


def bbox(mask, x0, y0, x1, y1):
    ys, xs = np.where(mask[y0:y1, x0:x1])
    return xs.min() + x0, ys.min() + y0, xs.max() + x0, ys.max() + y0


def bg_fill(img, box):
    """Rechteck mit der Hintergrundfarbe der jeweiligen Zeile füllen (rechter Rand, ohne Text)."""
    x0, y0, x1, y1 = box
    arr = np.array(img)
    for y in range(y0, y1):
        arr[y, x0:x1] = np.median(A[y, 2700:2950], axis=0)
    return Image.fromarray(arr.astype("uint8"))


def baseline_for(orig, font, top):
    return top - font.getbbox(orig, anchor="ls")[1]


def draw_line(img, xy_top, orig, new, font, fill=(255, 255, 255)):
    x, top = xy_top
    base = baseline_for(orig, font, top)
    ImageDraw.Draw(img).text((x, base), new, font=font, fill=fill, anchor="ls")


def label(img, text):
    """Rotes, leicht schräges Label: Fläche rot füllen, neuen Text zentriert und gedreht setzen."""
    ys, xs = np.where(redm[2300:2800]); ys = ys + 2300
    pts = np.stack([xs, ys], 1)
    from scipy.spatial import ConvexHull  # noqa
    hull = pts[ConvexHull(pts).vertices]
    d = ImageDraw.Draw(img)
    d.polygon([tuple(p) for p in hull], fill=(232, 33, 48))
    # Originaltext-Grösse: Höhe der weissen Schrift im Inneren
    tb = bbox(white, 330, 2500, 1860, 2650)
    orig = "uf Chuchichäschtlidütsch"
    f = ImageFont.truetype(F % "ExtraBold", 100)
    s = 100 * (tb[2] - tb[0]) / (f.getbbox(orig)[2] - f.getbbox(orig)[0])
    f = ImageFont.truetype(F % "ExtraBold", round(s))
    w = f.getbbox(text)[2] - f.getbbox(text)[0]
    t = Image.new("RGBA", (w + 200, 400), (0, 0, 0, 0))
    ImageDraw.Draw(t).text((t.width / 2, t.height / 2), text, font=f, fill="white", anchor="mm")
    t = t.rotate(3.04, resample=Image.BICUBIC, expand=True)
    cx, cy = hull[:, 0].mean(), hull[:, 1].mean()
    img.paste(t, (int(cx - t.width / 2), int(cy - t.height / 2)), t)


def chip_text(img, chip, text):
    """Text in einem Chip ersetzen; Chip bei Bedarf nach rechts verlängern.
    Textanfang = Chip-Anfang + 202 px (wie bei «Global» und «Europa» im Original)."""
    x0, y0, x1, y1 = chip
    f = ImageFont.truetype(F % "SemiBold", 114)
    tx = x0 + 202
    tw = f.getbbox(text)[2] - f.getbbox(text)[0]
    grow = max(0, tx + tw + 60 - x1)
    arr = np.array(img)
    if grow:
        R = (y1 - y0) // 2 + 4                       # Radius der Rundung
        col = A[y0:y1 + 1, x0 + 185].copy()           # gerader Rahmen zwischen Icon und Text
        cap = A[y0:y1 + 1, x1 - R:x1 + 6].copy()
        cap[1012 - y0:1136 - y0, :R - 32] = A[(y0 + y1) // 2, x0 + 185]   # alten Text aus der Rundung entfernen
        for x in range(x1 - R, x1 - R + grow):
            arr[y0:y1 + 1, x] = col
        arr[y0:y1 + 1, x1 - R + grow:x1 + 6 + grow] = cap
    img2 = Image.fromarray(arr.astype("uint8"))
    inner = A[(y0 + y1) // 2, x0 + 185]
    old_end = bbox(white, x0 + 190, 990, x1 - 20, 1160)[2]
    right = min(max(old_end, tx + tw) + 12, x1 + grow - 32)
    ImageDraw.Draw(img2).rectangle([x0 + 192, 1012, right, 1135], fill=tuple(int(v) for v in inner))
    ImageDraw.Draw(img2).text((tx, 1104), text, font=f, fill="white", anchor="ls")
    return img2


def save(img, name):
    img.save(SITE / f"cover-{name}.png", optimize=True)
    img.resize((600, 600), Image.LANCZOS).save(SITE / f"cover-web-{name}.jpg", quality=88)


# ---------- Deutsch: nur Label
de = src.copy()
label(de, "auf Hochdeutsch")
save(de, "de")

# ---------- English
en = src.copy()
fT = ImageFont.truetype(F % "Bold", 100)
en = bg_fill(en, (366, 112, 2340, 236))
draw_line(en, (374, 127), "Recherche, Skript & Stimmen: KI-Agenten", "Research, script & voices: AI agents", fT)
fH = ImageFont.truetype(F % "ExtraBold", 304)
en = bg_fill(en, (222, 316, 1560, 885))
draw_line(en, (234, 328), "Rogers", "Roger’s", fH)
draw_line(en, (234, 644), "KI-Radar", "AI Radar", fH)
en = chip_text(en, (856, 975, 1478, 1179), "Europe")
en = chip_text(en, (1500, 975, 2221, 1179), "Switzerland")
fB = ImageFont.truetype(F % "SemiBold", 98)
en = bg_fill(en, (905, 2748, 2420, 2872))
draw_line(en, (928, 2763), "jeden Montag · rund 3 Minuten", "every Monday · about 3 minutes", fB, fill=(225, 230, 240))
label(en, "in English")
save(en, "en")
print("ok")

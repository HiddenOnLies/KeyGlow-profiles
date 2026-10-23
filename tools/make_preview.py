"""Draws docs/preview.png: one moment of every profile on a 65% keyboard.

Needs KeyGlow and Pillow. Run from the repository root: python tools/make_preview.py
"""

import json
import time
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont

from keyglow import input as keyinput
from keyglow.layout import load_layout
from keyglow.profile import Profile, Renderer

ROOT = Path(__file__).resolve().parent.parent
U, PAD, TOP, COLS = 22, 12, 26, 3


def font(size):
    for name in ("segoeui.ttf", "DejaVuSans.ttf", "Arial.ttf"):
        try:
            return ImageFont.truetype(name, size)
        except OSError:
            continue
    return ImageFont.load_default()


def tile(layout, colors, title, tfont):
    w, h = int(layout.width * U) + PAD * 2, int(layout.height * U) + PAD * 2 + TOP
    glow = Image.new("RGB", (w, h))
    gd = ImageDraw.Draw(glow)
    boxes = []
    for k in layout.keys:
        box = (PAD + k.x * U + 2, TOP + PAD + k.y * U + 2, PAD + (k.x + k.w) * U - 2, TOP + PAD + (k.y + k.h) * U - 2)
        boxes.append((box, colors.get(k.id, (0, 0, 0))))
        gd.rounded_rectangle(box, 4, fill=boxes[-1][1])
    img = Image.blend(Image.new("RGB", (w, h)), glow.filter(ImageFilter.GaussianBlur(7)), 0.6)
    d = ImageDraw.Draw(img)
    for box, c in boxes:
        d.rounded_rectangle(box, 3, fill=(14, 14, 14), outline=tuple(int(v * 0.8 + 25) for v in c), width=2)
    d.text((PAD, TOP / 2 + 4), title, fill=(230, 230, 230), font=tfont, anchor="lm")
    return img


def main():
    layout = load_layout("alloy_origins_65")
    tfont = font(14)
    tiles = []
    for f in sorted((ROOT / "profiles").glob("*.json")):
        d = json.loads(f.read_text(encoding="utf-8"))
        keyinput.clear()
        now = time.monotonic()
        for key, age in (("K", 0.1), ("E", 0.3), ("Y", 0.55)):  # so reactive profiles show something
            keyinput.press(key, now - age)
        tiles.append(tile(layout, Renderer(Profile.from_dict(d), layout).frame(2.5), d["name"], tfont))
    tw, th = tiles[0].size
    rows = (len(tiles) + COLS - 1) // COLS
    sheet = Image.new("RGB", (tw * COLS, th * rows), (0, 0, 0))
    for i, t in enumerate(tiles):
        sheet.paste(t, ((i % COLS) * tw, (i // COLS) * th))
    (ROOT / "docs").mkdir(exist_ok=True)
    sheet.save(ROOT / "docs" / "preview.png", optimize=True)
    print(f"{len(tiles)} profiles -> docs/preview.png")


if __name__ == "__main__":
    main()

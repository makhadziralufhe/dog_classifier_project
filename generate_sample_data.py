"""
Generates 40 small placeholder JPEGs into pet_images/, one per entry in
demo_data.PET_IMAGES, plus dognames.txt. Run once during setup:

    python3 generate_sample_data.py

Each image is a simple colored card with its true label drawn on it -- there
is no real photo dataset bundled here (no internet access to fetch one), so
these exist purely so every notebook and script has real files on disk to
open, run PIL image checks against, and pass through the (mock) classifier.
"""

import os
import colorsys
from PIL import Image, ImageDraw, ImageFont

from demo_data import PET_IMAGES, CONFUSABLE

OUT_DIR = os.path.join(os.path.dirname(__file__), "pet_images")
SIZE = (224, 224)


def _color_for(label):
    # Deterministic, pleasant color derived from the label text.
    h = (hash(label) % 360) / 360
    r, g, b = colorsys.hsv_to_rgb(h, 0.45, 0.85)
    return (int(r * 255), int(g * 255), int(b * 255))


def _font(size):
    for candidate in (
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    ):
        if os.path.exists(candidate):
            return ImageFont.truetype(candidate, size)
    return ImageFont.load_default()


def make_card(label, path):
    img = Image.new("RGB", SIZE, _color_for(label))
    draw = ImageDraw.Draw(img)

    words = label.split(" ")
    font = _font(22)
    line_height = 26
    total_h = line_height * len(words)
    y = (SIZE[1] - total_h) // 2

    for word in words:
        bbox = draw.textbbox((0, 0), word, font=font)
        w = bbox[2] - bbox[0]
        draw.text(((SIZE[0] - w) // 2, y), word, fill=(255, 255, 255), font=font)
        y += line_height

    draw.rectangle([4, 4, SIZE[0] - 5, SIZE[1] - 5], outline=(255, 255, 255), width=3)
    img.save(path, "JPEG", quality=85)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    for filename, label in PET_IMAGES.items():
        make_card(label, os.path.join(OUT_DIR, filename))
    print(f"Wrote {len(PET_IMAGES)} sample images to {OUT_DIR}/")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Draw the 23 November 2026 world-news front page, 1024x1024.

Everything is drawn with Pillow primitives: no photo, no network, no
randomness, so the output bytes are identical on every run.
Run:  python3 render.py  ->  writes entry.png next to this file.
"""
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "entry.png")

W, H = 1024, 1024
PAPER = (246, 241, 227)
INK = (22, 21, 19)
NAVY = (22, 35, 63)
NAVY_LT = (38, 56, 92)
RED = (164, 31, 34)
GOLD = (201, 162, 39)
TEAL = (15, 91, 77)
GREY = (94, 90, 82)
LINE = (180, 172, 150)
SOFT = (238, 232, 214)

FONT_DIR = "/usr/share/fonts/truetype/noto"


def font(name, size):
    return ImageFont.truetype(os.path.join(FONT_DIR, name), size)


SERIF_B = lambda s: font("NotoSerif-Bold.ttf", s)
SERIF = lambda s: font("NotoSerif-Regular.ttf", s)
SANS_B = lambda s: font("NotoSans-Bold.ttf", s)
SANS = lambda s: font("NotoSans-Regular.ttf", s)
SANS_X = lambda s: font("NotoSans-Black.ttf", s)


def wrap(draw, text, fnt, width):
    """Greedy word wrap; returns a list of lines that fit `width`."""
    lines, cur = [], ""
    for word in text.split():
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def para(draw, text, fnt, x, y, width, leading, fill=INK):
    """Draw wrapped text; return the y just below the last line."""
    for line in wrap(draw, text, fnt, width):
        draw.text((x, y), line, font=fnt, fill=fill)
        y += leading
    return y


def kicker(draw, text, x, y, color=RED):
    """Small caps section label with a short rule after it."""
    fnt = SANS_B(15)
    draw.text((x, y), text.upper(), font=fnt, fill=color)
    w = draw.textlength(text.upper(), font=fnt)
    draw.line([(x + w + 10, y + 8), (x + w + 34, y + 8)], fill=color, width=3)
    return y + 22


def rule(draw, x0, x1, y, width=2, fill=LINE):
    draw.line([(x0, y), (x1, y)], fill=fill, width=width)


# ---------------------------------------------------------------- pictograms
def globe(draw, cx, cy, r, fill=TEAL):
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=fill)
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], outline=(255, 255, 255), width=3)
    draw.arc([cx - r, cy - r, cx + r, cy + r], 200, 340, fill=(255, 255, 255), width=3)
    draw.arc([cx - int(r * 0.55), cy - r, cx + int(r * 0.55), cy + r],
             270, 90, fill=(255, 255, 255), width=3)
    draw.arc([cx - int(r * 0.55), cy - r, cx + int(r * 0.55), cy + r],
             90, 270, fill=(255, 255, 255), width=3)
    draw.line([(cx - r, cy), (cx + r, cy)], fill=(255, 255, 255), width=3)
    # crack: the deal broke
    draw.line([(cx + int(r * 0.1), cy - int(r * 0.7)), (cx - int(r * 0.2), cy - int(r * 0.2)),
               (cx + int(r * 0.15), cy + int(r * 0.1)), (cx - int(r * 0.1), cy + int(r * 0.6))],
              fill=GOLD, width=5)


def ship(draw, x, y, w, h, fill=NAVY):
    hull = [(x, y + h * 0.5), (x + w, y + h * 0.5),
            (x + w * 0.82, y + h * 0.78), (x + w * 0.18, y + h * 0.78)]
    draw.polygon(hull, fill=fill)
    draw.line([(x + w * 0.5, y + h * 0.5), (x + w * 0.5, y)], fill=fill, width=5)
    draw.polygon([(x + w * 0.5, y + 4), (x + w * 0.5, y + h * 0.42),
                  (x + w * 0.85, y + h * 0.42)], fill=RED)
    for i in range(2):
        draw.line([(x + w * 0.05, y + h * 0.86 + i * 7),
                   (x + w * 0.95, y + h * 0.86 + i * 7)], fill=(120, 150, 190), width=3)


def flats(draw, x, y, w, h, fill=NAVY):
    draw.rectangle([x, y, x + w * 0.55, y + h], fill=fill)
    draw.rectangle([x + w * 0.6, y + h * 0.3, x + w, y + h], fill=NAVY_LT)
    for r in range(4):
        for c in range(2):
            draw.rectangle([x + 8 + c * 22, y + 10 + r * 26, x + 20 + c * 22, y + 22 + r * 26],
                           fill=GOLD)
    draw.line([(x - 6, y + h * 0.45), (x + w * 0.4, y + h * 0.2)], fill=RED, width=5)


def flame(draw, x, y, w, h, fill=RED):
    draw.polygon([(x + w * 0.5, y), (x + w * 0.95, y + h * 0.55),
                  (x + w * 0.75, y + h), (x + w * 0.25, y + h),
                  (x + w * 0.05, y + h * 0.55)], fill=fill)
    draw.polygon([(x + w * 0.5, y + h * 0.45), (x + w * 0.72, y + h * 0.7),
                  (x + w * 0.5, y + h * 0.95), (x + w * 0.28, y + h * 0.7)],
                 fill=GOLD)


def ballot(draw, x, y, w, h, fill=NAVY):
    draw.rectangle([x, y + h * 0.35, x + w, y + h], fill=fill)
    draw.rectangle([x + w * 0.15, y + h * 0.2, x + w * 0.85, y + h * 0.42],
                   outline=fill, width=4)
    draw.line([(x + w * 0.35, y), (x + w * 0.5, y + h * 0.32),
               (x + w * 0.75, y - 6)], fill=RED, width=6)
    draw.text((x + w * 0.32, y + h * 0.55), "258", font=SANS_X(26), fill=(255, 255, 255))


def chart_down(draw, x, y, w, h, fill=RED):
    pts = [(x, y + h * 0.15), (x + w * 0.3, y + h * 0.35), (x + w * 0.55, y + h * 0.3),
           (x + w * 0.8, y + h * 0.65), (x + w, y + h * 0.6)]
    draw.line(pts, fill=fill, width=6, joint="curve")
    draw.polygon([(x + w - 14, y + h * 0.6), (x + w + 4, y + h * 0.6),
                  (x + w - 4, y + h * 0.92)], fill=fill)
    draw.line([(x, y + h * 0.97), (x + w, y + h * 0.97)], fill=GREY, width=3)


# ---------------------------------------------------------------- masthead
def masthead(draw):
    draw.rectangle([0, 0, W, 132], fill=NAVY)
    draw.rectangle([0, 132, W, 138], fill=GOLD)
    title = "THE WORLD IN A DAY"
    fnt = SERIF_B(64)
    tw = draw.textlength(title, font=fnt)
    draw.text(((W - tw) / 2, 16), title, font=fnt, fill=(246, 241, 227))
    sub = "MONDAY  ·  23 NOVEMBER 2026  ·  ONE DAY, ONE PAGE, THE WHOLE WORLD"
    fnt2 = SANS_B(19)
    tw2 = draw.textlength(sub, font=fnt2)
    draw.text(((W - tw2) / 2, 96), sub, font=fnt2, fill=GOLD)


# ---------------------------------------------------------------- lead story
def lead(draw):
    y = 158
    y = kicker(draw, "Climate — Antalya, Turkey", 44, y, RED)
    head = "COP31 ends with no deal"
    draw.text((44, y), head, font=SERIF_B(54), fill=INK)
    y += 66
    deck = ("After two days of overtime, the summit closed with no agreement: "
            "the EU and about 130 countries rejected a draft that left out "
            "fossil fuels altogether.")
    y = para(draw, deck, SERIF(24), 44, y, 620, 32)
    y += 6
    draw.text((44, y), "Talks collapse over oil and gas — the text never came back.",
              font=SANS_B(19), fill=TEAL)
    globe(draw, 856, 252, 88)
    draw.text((790, 352), "NO DEAL", font=SANS_X(22), fill=RED)


# ---------------------------------------------------------------- story rows
def story(draw, x, y, w, tag, head, deck, head_size=30, deck_size=19,
          deck_leading=25, pic=None, pic_y=None, pic_h=48):
    y = kicker(draw, tag, x, y)
    y = para(draw, head, SERIF_B(head_size), x, y, w, head_size + 6)
    y += 4
    y = para(draw, deck, SANS(deck_size), x, y, w, deck_leading)
    if pic is not None and pic_y is not None:
        pic(draw, x, pic_y, 110, pic_h)
    return y


def middle_row(draw):
    rule(draw, 44, 980, 392, 2)
    rule(draw, 44, 980, 622, 2)
    y = 408
    story(draw, 44, y, 430, "War at sea — Benghazi, Libya",
          "Russian warship sinks after drone strike",
          "The corvette Merkury went down at Benghazi naval base after a "
          "suspected Ukrainian sea-drone attack, carrying the war far "
          "beyond its shores.")
    draw.line([(512, 408), (512, 606)], fill=LINE, width=2)
    story(draw, 548, y, 432, "Ukraine — Dymer, north of Kyiv",
          "Boy, 7, pulled alive from rubble",
          "A Russian strike on a block of flats killed at least 10 people. "
          "Rescuers freed the boy hours later; at least 14 were still "
          "missing.")


def third_row(draw):
    rule(draw, 44, 980, 786, 2)
    y = 638
    story(draw, 44, y, 288, "Gulf — Bahrain & Hormuz",
          "Iran strikes Bahrain; tankers burn",
          "Two hurt as Iran hits Bahrain; tankers burn near Hormuz.",
          head_size=26,
          deck_size=17, deck_leading=22)
    draw.line([(352, 638), (352, 772)], fill=LINE, width=2)
    story(draw, 372, y, 288, "Politics — Washington",
          "Democrats take the House",
          "At least 258 seats — the biggest House majority since 1992.",
          head_size=26,
          deck_size=17, deck_leading=22)
    draw.line([(680, 638), (680, 772)], fill=LINE, width=2)
    story(draw, 700, y, 280, "Markets — Tokyo",
          "AI sell-off sinks Nikkei 5%",
          "Nikkei falls 5.06% as the US AI sell-off spreads.", head_size=26,
          deck_size=17, deck_leading=22)


# ---------------------------------------------------------------- also strip
ALSO = [
    ("SEOUL", "South Korea's exports pass $1 trillion in a year — a first."),
    ("SCIENCE", "Anthropic mathematician and Claude claim a proof of the Riemann Hypothesis."),
    ("INDONESIA", "Candy-factory fire in Banten leaves 3 dead and 37 missing."),
    ("SHENZHEN", "Trump, Putin and Xi issue a joint 'Declaration toward Peace'."),
    ("SPORT", "FIFA to confirm the UK as host of the 2035 Women's World Cup."),
    ("PACIFIC", "Magnitude 6.5 earthquake strikes the Vanuatu region."),
]


def also_strip(draw):
    y = 798
    draw.rectangle([0, y, W, y + 6], fill=NAVY)
    draw.text((44, y + 12), "ALSO ON 23 NOVEMBER", font=SANS_X(20), fill=NAVY)
    y += 46
    for i, (tag, text) in enumerate(ALSO):
        col = i % 3
        row = i // 3
        x = 44 + col * 316
        yy = y + row * 50
        draw.text((x, yy), tag, font=SANS_B(14), fill=RED)
        para(draw, text, SANS(14), x, yy + 18, 296, 17)


def footer(draw):
    draw.rectangle([0, 978, W, H], fill=NAVY)
    note = "Every story above was first reported on Monday 23 November 2026."
    fnt = SANS(16)
    tw = draw.textlength(note, font=fnt)
    draw.text(((W - tw) / 2, 992), note, font=fnt, fill=(246, 241, 227))


def main():
    img = Image.new("RGB", (W, H), PAPER)
    draw = ImageDraw.Draw(img)
    masthead(draw)
    lead(draw)
    middle_row(draw)
    third_row(draw)
    also_strip(draw)
    footer(draw)
    img.save(OUT, format="PNG", optimize=True)
    print("wrote", OUT, os.path.getsize(OUT), "bytes")


if __name__ == "__main__":
    main()

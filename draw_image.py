# news-image-20261123 entry image — "THE DAY IN NUMBERS: SCOREBOARD".
# Draws one 1024x1024 image summing up Monday 23 November 2026.
# Concept: a sports scoreboard. A full-width gold hero band with one
# giant hero number (31% — Nvidia), then a 3x2 grid of navy number-cards,
# then a "MORE TODAY" ticker strip. The numbers ARE the visual.
# Palette: navy + gold, the signature of our Nov 24 entry, in a new
# composition (hero band + grid + ticker, not the Nov 24 2x2 + strip).
# Run: python3 draw_image.py  ->  writes entry.png next to this file.

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
OUT = "entry.png"

NAVY = (10, 30, 60)          # deep navy — header, footer, cards
NAVY_CARD = (15, 41, 76)     # slightly lighter navy for grid cards
NAVY_TEXT = (10, 30, 60)     # navy text on the gold hero band
GOLD = (206, 164, 60)        # signature gold
GOLD_BRIGHT = (232, 190, 70) # gold that pops on navy
GOLD_DEEP = (176, 138, 44)   # darker gold for small rules on cream
CREAM = (246, 242, 231)      # paper background
WHITE = (255, 255, 255)
MUTED = (178, 192, 208)      # pale blue-grey captions on navy
INK = (32, 44, 58)           # near-black text on cream

FONT_DIR = "/usr/share/fonts/truetype/noto/"
BLACK = FONT_DIR + "NotoSans-Black.ttf"
BOLD = FONT_DIR + "NotoSans-Bold.ttf"
REG = FONT_DIR + "NotoSans-Regular.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    """Greedy word wrap to a pixel width; returns a list of lines."""
    lines, cur = [], ""
    for word in text.split(" "):
        trial = word if not cur else cur + " " + word
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def draw_wrapped(draw, x, y, text, fnt, fill, max_w, leading, max_lines=None):
    """Draw wrapped text; returns the y just below the last line."""
    lines = wrap(draw, text, fnt, max_w)
    if max_lines:
        lines = lines[:max_lines]
    for line in lines:
        draw.text((x, y), line, font=fnt, fill=fill)
        y += leading
    return y


def main():
    img = Image.new("RGB", (W, H), CREAM)
    d = ImageDraw.Draw(img)

    # ---- header band: navy, brand left, date right ----
    d.rectangle([0, 0, W, 56], fill=NAVY)
    d.text((24, 15), "THE DAY IN NUMBERS", font=font(BLACK, 24), fill=GOLD_BRIGHT)
    date = "MONDAY 23 NOVEMBER 2026"
    dw = d.textlength(date, font=font(BOLD, 22))
    d.text((W - 24 - dw, 17), date, font=font(BOLD, 22), fill=WHITE)
    d.rectangle([0, 56, W, 59], fill=GOLD)

    # ---- hero band: gold, one giant number + headline ----
    d.rectangle([0, 59, W, 320], fill=GOLD)
    # Giant hero number, left: auto-fit into its zone.
    hero_num = "31%"
    size = 200
    while size > 60:
        f = font(BLACK, size)
        if d.textlength(hero_num, font=f) <= 400:
            break
        size -= 5
    fnum = font(BLACK, size)
    bbox = d.textbbox((0, 0), hero_num, font=fnum)
    num_h = bbox[3] - bbox[1]
    num_y = 59 + (237 - num_h) // 2 - bbox[1]
    d.text((36 - bbox[0], num_y), hero_num, font=fnum, fill=NAVY_TEXT)

    # Hero text, right.
    hx = 470
    d.text((hx, 82), "NVIDIA  ·  MARKETS", font=font(BOLD, 20), fill=NAVY_TEXT)
    d.text((hx, 108), "HUANG IS BACK", font=font(BLACK, 62), fill=NAVY_TEXT)
    d.text((hx, 178), "NVIDIA SOARS AS ITS CEO RETURNS", font=font(BOLD, 27), fill=NAVY_TEXT)
    hero_cap = (
        "Nvidia's board reinstates Jensen Huang as CEO, 11 days after he quit. "
        "Shares close up 31.5% — the best day since 2003 — adding about $950bn in value."
    )
    draw_wrapped(d, hx, 216, hero_cap, font(REG, 20), NAVY_TEXT, W - 24 - hx, 26, max_lines=3)

    # Stats strip along the bottom of the hero band.
    # Strip is 32px tall and the text is centred on its real glyph box,
    # so descenders (e.g. the Q in NASDAQ) fit with padding top/bottom.
    d.rectangle([0, 296, W, 328], fill=NAVY)
    stats = "NASDAQ +6.5%    ·    S&P 500 +4.7%    ·    DOW +1,448    ·    +$950BN IN A DAY"
    fstats = font(BOLD, 18)
    sw = d.textlength(stats, font=fstats)
    sb = d.textbbox((0, 0), stats, font=fstats)
    sx = (W - sw) / 2 - sb[0]
    sy = 296 + (32 - (sb[3] - sb[1])) // 2 - sb[1]
    d.text((sx, sy), stats, font=fstats, fill=GOLD_BRIGHT)

    # ---- scoreboard grid: 3 x 2 navy number-cards ----
    cards = [
        ("UKRAINE · WAR AT SEA", "7", "SEVEN DRONES, ONE SHIP DOWN",
         "Ukraine says seven naval drones sank the corvette Merkury at Benghazi, Libya."),
        ("CLIMATE · ANTALYA", "17", "COP31 ENDS WITH NO DEAL",
         "The Antalya summit fails — the first in 17 years. Nearly 200 nations rejected a text with no mention of fossil fuels."),
        ("NIGERIA · TRAGEDY AT SEA", "24", "MOURNERS LOST AT SEA",
         "At least 24 people die as a boat carrying mourners to a funeral capsizes in Bayelsa, Nigeria."),
        ("UKRAINE · OVERNIGHT BARRAGE", "400+", "A NIGHT OF FIRE OVER UKRAINE",
         "Russia fires 400+ drones and 110 missiles overnight; at least nine killed in Kyiv and Kryvyi Rih."),
        ("EUROPE · RUSSIA SANCTIONS", "60", "EU'S 22ND SANCTIONS PACKAGE",
         "About 60 banks face a SWIFT cut-off; 70+ shadow-fleet ships listed. Unveiled by von der Leyen in Strasbourg."),
        ("BELGIUM · TRAVEL CHAOS", "429", "BRUSSELS AIRPORT STANDSTILL",
         "A strike cancels 429 flights, affecting 59,000 passengers."),
    ]
    gx, gy = 24, 336
    gap = 14
    cw = (W - 2 * gx - 2 * gap) // 3
    ch = 218
    for i, (kicker, num, head, cap) in enumerate(cards):
        cx = gx + (i % 3) * (cw + gap)
        cy = gy + (i // 3) * (ch + gap)
        d.rectangle([cx, cy, cx + cw, cy + ch], fill=NAVY_CARD)
        d.rectangle([cx, cy, cx + cw, cy + 5], fill=GOLD)
        tx = cx + 18
        tw = cw - 36
        d.text((tx, cy + 18), kicker, font=font(BOLD, 13), fill=GOLD_BRIGHT)
        d.text((tx, cy + 38), num, font=font(BLACK, 60), fill=GOLD_BRIGHT)
        draw_wrapped(d, tx, cy + 110, head, font(BOLD, 20), WHITE, tw, 25, max_lines=2)
        draw_wrapped(d, tx, cy + 160, cap, font(REG, 14), MUTED, tw, 18, max_lines=3)

    # ---- ticker: MORE TODAY strip on cream ----
    ty = 336 + 2 * ch + gap + 14  # 800
    d.text((24, ty), "MORE TODAY", font=font(BLACK, 20), fill=NAVY_TEXT)
    d.rectangle([170, ty + 12, W - 24, ty + 14], fill=GOLD_DEEP)
    ticker = [
        "Houthis claim a hit on Saudi Arabia's Rabigh refinery; the coalition says it intercepted a missile and a drone",
        "Iran strikes an industrial site in Bahrain; two tankers hit by projectiles in the Strait of Hormuz",
        "Poland: prosecutors say three crashed objects were Russian Kh-101 cruise missiles",
        "US presses Ukraine security talks; envoy Kushner announces post-war talks",
        "A Russian drone partly collapses a five-storey block in Dymer; at least 10 dead",
        "Boca Juniors win the Copa Sudamericana 2–0 — first international trophy in 18 years",
        "Taiwan counts 24 Chinese aircraft, 17 over the median line, plus 11 warships and 10 balloons",
    ]
    col_w = (W - 2 * 24 - 28) // 2
    row_h = 38
    for i, item in enumerate(ticker):
        col = i % 2
        row = i // 2
        ix = 24 + col * (col_w + 28)
        iy = ty + 32 + row * row_h
        # Small solid gold triangle as the bullet (a "▸" glyph is missing
        # from the font, so draw the marker instead of typesetting it).
        d.polygon([(ix, iy + 4), (ix, iy + 12), (ix + 8, iy + 8)], fill=GOLD_DEEP)
        draw_wrapped(d, ix + 16, iy, item, font(REG, 14), INK, col_w - 16, 17, max_lines=2)

    # ---- footer band: navy ----
    d.rectangle([0, 990, W, H], fill=NAVY)
    d.text((24, 1001), "THE DAY IN NUMBERS", font=font(BOLD, 15), fill=GOLD_BRIGHT)
    src = "SOURCES: CNN · REUTERS · AL JAZEERA · THE TIMES"
    sw2 = d.textlength(src, font=font(REG, 14))
    d.text(((W - sw2) / 2, 1002), src, font=font(REG, 14), fill=MUTED)
    d.text((W - 24 - d.textlength("14 STORIES", font=font(BOLD, 15)), 1001),
           "14 STORIES", font=font(BOLD, 15), fill=WHITE)

    img.save(OUT, "PNG")
    print(f"wrote {OUT} {W}x{H}")


if __name__ == "__main__":
    main()

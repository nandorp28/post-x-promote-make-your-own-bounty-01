#!/usr/bin/env python3
"""Generate photo.png for the post-x-promote-make-your-own-bounty-01 entry.

Composition: make.fun's official 16:9 brand badge (from the press pack,
used as-is, uniformly scaled) over a light canvas in the press palette,
plus original text written by the entrant's agent. Build-time only.
"""
from PIL import Image, ImageDraw, ImageFont

W, H = 1200, 675
CANVAS = (250, 248, 250)      # #FAF8FA Light canvas
INK = (25, 20, 25)            # #191419
SECONDARY = (90, 83, 89)      # #5A5359
MAGENTA = (188, 12, 124)      # #BC0C7C Light magenta
HAIRLINE = (226, 222, 225)    # #E2DEE1

BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

img = Image.new("RGB", (W, H), CANVAS)
d = ImageDraw.Draw(img)

# Official 16:9 brand badge, used as-is, uniformly scaled to the canvas.
badge = Image.open("badge-16x9.png").convert("RGBA")
badge = badge.resize((W, H), Image.LANCZOS)
img.paste(badge, (0, 0), badge)
d = ImageDraw.Draw(img)

# Magenta accent bar (own drawing).
d.rectangle([80, 232, 200, 244], fill=MAGENTA)

# Headline (own words).
f_head = ImageFont.truetype(BOLD, 74)
d.text((80, 268), "Make your own", font=f_head, fill=INK)
d.text((80, 348), "bounty.", font=f_head, fill=INK)

# Supporting lines (own words, from the bounty description).
f_sub = ImageFont.truetype(REG, 32)
d.text((82, 470), "Describe any task. Set the reward.", font=f_sub, fill=SECONDARY)
d.text((82, 512), "Agents compete — the best entries get paid.", font=f_sub, fill=SECONDARY)

# Footer hairline + link.
d.line([(80, 600), (1120, 600)], fill=HAIRLINE, width=2)
f_link = ImageFont.truetype(BOLD, 32)
d.text((82, 618), "make.fun/sponsor/new", font=f_link, fill=MAGENTA)

img.save("photo.png")
print("saved photo.png", img.size)

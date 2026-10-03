from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parent
SOURCES = [
    ("OCTARINE · 25 AUG 2026", ROOT / "octarine-blog-latest-update-2026-09-08.png"),
    ("MELONITY · 2 SEP 2026", ROOT / "melonity-latest-deadlock-update-2026-09-08.png"),
    ("PREDATOR · 21 JUL 2026", ROOT / "predator-latest-deadlock-update-2026-09-08.png"),
]

canvas = Image.new("RGB", (1800, 1050), "#0E0E10")
draw = ImageDraw.Draw(canvas)
font = ImageFont.load_default(size=32)
small = ImageFont.load_default(size=22)
draw.text((70, 55), "DATED DEADLOCK UPDATE EVIDENCE", fill="#F2F2F2", font=font)
draw.text((70, 105), "Official vendor pages · captured 8 Sep 2026", fill="#AEB0BA", font=small)

panel_width = 520
panel_height = 760
for index, (label, source) in enumerate(SOURCES):
    x = 70 + index * 570
    y = 185
    draw.rounded_rectangle((x, y, x + panel_width, y + panel_height), radius=22, fill="#17171B", outline="#2B58FF", width=3)
    image = Image.open(source).convert("RGB")
    target = (panel_width - 30, 650)
    image.thumbnail(target, Image.Resampling.LANCZOS)
    image_x = x + (panel_width - image.width) // 2
    image_y = y + 80 + (650 - image.height) // 2
    canvas.paste(image, (image_x, image_y))
    draw.text((x + 24, y + 24), label, fill="#F2F2F2", font=small)

draw.text((70, 980), "Dates describe visible public notes, not independent compatibility or safety tests.", fill="#AEB0BA", font=small)
canvas.save(ROOT / "deadlock-changelog-screenshot-collage-2026-09-08.png", optimize=True)


def text(drawer, xy, value, *, fill="#F2F2F2", size=24, anchor=None):
    drawer.text(xy, value, fill=fill, font=ImageFont.load_default(size=size), anchor=anchor)


score = Image.new("RGB", (1400, 900), "#0E0E10")
sdraw = ImageDraw.Draw(score)
sdraw.rounded_rectangle((70, 60, 1330, 840), radius=28, fill="#17171B", outline="#2B58FF", width=4)
text(sdraw, (120, 95), "PUBLIC-EVIDENCE SCORECARD", size=44)
text(sdraw, (120, 155), "Visibility only - checked 8 Sep 2026 - not a safety score", fill="#AEB0BA", size=22)
text(sdraw, (745, 225), "CLUSTER", size=26, anchor="mm")
text(sdraw, (1105, 225), "OCTARINE", size=26, anchor="mm")
rows = [
    ("Product page - 20%", 20, 20, 20),
    ("Dated changelog - 25%", 25, 0, 25),
    ("Public documentation - 20%", 20, 8, 16),
    ("Support route - 15%", 15, 15, 12),
    ("Limits / risk disclosure - 20%", 20, 14, 12),
]
for index, (label, maximum, cluster, octarine) in enumerate(rows):
    y = 285 + index * 100
    text(sdraw, (120, y + 8), label, size=24)
    for x, value, color in ((610, cluster, "#635FD5"), (970, octarine, "#2B58FF")):
        sdraw.rounded_rectangle((x, y, x + 280, y + 38), radius=19, fill="#292932")
        width = int(280 * value / maximum) if maximum else 0
        if width:
            sdraw.rounded_rectangle((x, y, x + width, y + 38), radius=19, fill=color)
        text(sdraw, (x + 140, y + 19), f"{value} / {maximum}", size=20, anchor="mm")
sdraw.line((120, 765, 1280, 765), fill="#3A3A44", width=2)
text(sdraw, (750, 805), "TOTAL 57 / 100", size=34, anchor="mm")
text(sdraw, (1110, 805), "TOTAL 85 / 100", size=34, anchor="mm")
score.save(ROOT / "public-evidence-scorecard-cluster-octarine-2026-09-08.png", optimize=True)


timeline = Image.new("RGB", (1600, 900), "#0E0E10")
tdraw = ImageDraw.Draw(timeline)
tdraw.rounded_rectangle((70, 60, 1530, 840), radius=30, fill="#17171B", outline="#2B58FF", width=4)
text(tdraw, (125, 95), "DEADLOCK PATCH-EVIDENCE TIMELINE", size=46)
text(tdraw, (125, 157), "Latest dated public note visible on 8 Sep 2026 - page evidence only", fill="#AEB0BA", size=23)
tdraw.line((230, 455, 1370, 455), fill="#5B5B67", width=8)
points = [
    (390, "PREDATOR", "21 Jul 2026", "Dated, low-detail note", "#6DB33F"),
    (790, "OCTARINE", "25 Aug 2026", "Concrete cross-game release", "#635FD5"),
    (1190, "MELONITY", "2 Sep 2026", "24-item change log", "#FF1469"),
]
for x, label, date, note, color in points:
    tdraw.ellipse((x - 22, 433, x + 22, 477), fill=color)
    text(tdraw, (x, 355), label, size=30, anchor="mm")
    text(tdraw, (x, 400), date, fill="#AEB0BA", size=24, anchor="mm")
    text(tdraw, (x, 515), note, fill="#D4D4DB", size=20, anchor="mm")
for x, label, outline in ((170, "CLUSTER", "#635FD5"), (870, "UMBRELLA", "#6DB33F")):
    tdraw.rounded_rectangle((x, 610, x + 560, 735), radius=20, fill="#202027", outline=outline, width=3)
    text(tdraw, (x + 35, 635), label, size=28)
    text(tdraw, (x + 35, 685), "Current page; no dated public Deadlock log found", fill="#AEB0BA", size=20)
text(tdraw, (125, 790), "A dated vendor note documents communication. It does not prove present compatibility, service quality, or account outcomes.", fill="#AEB0BA", size=20)
timeline.save(ROOT / "deadlock-provider-public-update-timeline-2026-09-08.png", optimize=True)

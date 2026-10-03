from pathlib import Path


root = Path(__file__).resolve().parents[1] / "output" / "articles" / "20260910-082336"
replacements = {
    "\u0432\u0402\u045a": "\u201c",
    "\u0432\u0402\u045c": "\u201d",
    "\u0432\u0402\u2122": "\u2019",
    "\u0432\u0402\u201d": "\u2014",
    "\u0432\u0402\u201c": "\u2013",
    "\u0412\u00b7": "\u00b7",
}

for path in root.glob("*.md"):
    text = path.read_text(encoding="utf-8")
    updated = text
    for bad, good in replacements.items():
        updated = updated.replace(bad, good)
    if updated != text:
        path.write_text(updated, encoding="utf-8")
        print(f"Fixed {path.name}")

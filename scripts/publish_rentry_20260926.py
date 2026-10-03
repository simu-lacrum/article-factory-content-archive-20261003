from __future__ import annotations

import json
import re
import secrets
import sys
from pathlib import Path

import requests
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "output" / "publish" / "20260926-platforms-12x9" / "rentry"
OUT = ROOT / "output" / "publish" / "20260926-platforms-12x9" / "rentry-publication.json"

def slugify(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")[:75]

def publish_one(session: requests.Session, path: Path, ordinal: int) -> dict:
    page = session.get("https://rentry.co/", timeout=30)
    page.raise_for_status()
    soup = BeautifulSoup(page.text, "html.parser")
    csrf = soup.select_one("input[name=csrfmiddlewaretoken]")
    if not csrf or not csrf.get("value"):
        raise RuntimeError("Rentry CSRF token not found")
    raw = path.read_text(encoding="utf-8")
    front, body = (raw.split("---", 2)[1], raw.split("---", 2)[2]) if raw.startswith("---") else ("", raw)
    title_match = re.search(r'^title:\s*"(.*?)"$', front, flags=re.M)
    desc_match = re.search(r'^description:\s*"(.*?)"$', front, flags=re.M)
    title = title_match.group(1) if title_match else path.stem.replace("-", " ").title()
    description = desc_match.group(1) if desc_match else f"A practical, risk-aware guide to {title.lower()}."
    url = f"{slugify(title)}-{ordinal:02d}"
    metadata = f"PAGE_TITLE = {title[:60]}\nPAGE_DESCRIPTION = {description[:160]}\nSHARE_TITLE = {title[:60]}\nSHARE_DESCRIPTION = {description[:160]}"
    data = {"csrfmiddlewaretoken": csrf["value"], "text": body.strip(), "metadata": metadata, "url": url, "edit_code": secrets.token_urlsafe(18)}
    response = session.post("https://rentry.co/", data=data, timeout=45, allow_redirects=False)
    location = response.headers.get("location", "")
    if response.status_code not in (301, 302, 303) or not location:
        detail = BeautifulSoup(response.text, "html.parser").get_text(" ", strip=True)[:400]
        raise RuntimeError(f"HTTP {response.status_code}: {detail}")
    public_url = location if location.startswith("http") else "https://rentry.co" + location
    return {"file": path.name, "url": public_url, "title": title, "edit_code": data["edit_code"], "status": response.status_code}

def main() -> None:
    session = requests.Session()
    session.headers.update({"User-Agent": "Mozilla/5.0", "Referer": "https://rentry.co/"})
    results = []
    start = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    for ordinal, path in enumerate(sorted(SRC.glob("*.md")), start=1):
        if ordinal < start:
            continue
        results.append(publish_one(session, path, ordinal))
        print(json.dumps(results[-1], ensure_ascii=False))
    OUT.write_text(json.dumps({"results": results}, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"published={len(results)}")

if __name__ == "__main__":
    main()

from __future__ import annotations

import json
import sys
import urllib.error
import urllib.request
from html.parser import HTMLParser
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "output" / "publish" / "20260913-network-7x10"
BUNDLES = BASE / "bundles.json"
PUBLICATIONS = BASE / "publications.json"
REPORT = BASE / "verification.json"


class PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.title_parts: list[str] = []
        self.in_title = False
        self.links: list[dict] = []
        self.images: list[dict] = []
        self.meta_description = ""
        self._link: dict | None = None

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = {k.lower(): (v or "") for k, v in attrs}
        if tag.lower() == "title":
            self.in_title = True
        elif tag.lower() == "a":
            self._link = {"href": values.get("href", ""), "rel": values.get("rel", ""), "text": ""}
        elif tag.lower() == "img":
            self.images.append({"src": values.get("src", ""), "alt": values.get("alt", "")})
        elif tag.lower() == "meta" and values.get("name", "").lower() == "description":
            self.meta_description = values.get("content", "")

    def handle_endtag(self, tag: str) -> None:
        if tag.lower() == "title":
            self.in_title = False
        elif tag.lower() == "a" and self._link is not None:
            self._link["text"] = " ".join(self._link["text"].split())
            self.links.append(self._link)
            self._link = None

    def handle_data(self, data: str) -> None:
        if self.in_title:
            self.title_parts.append(data)
        if self._link is not None:
            self._link["text"] += data

    @property
    def title(self) -> str:
        return " ".join("".join(self.title_parts).split())


def fetch(url: str, timeout: int = 30) -> tuple[int, str]:
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 Codex publication verifier"})
    with urllib.request.urlopen(req, timeout=timeout) as response:
        status = getattr(response, "status", 200)
        body = response.read().decode(response.headers.get_content_charset() or "utf-8", errors="replace")
    return status, body


def check_image(url: str) -> int | None:
    try:
        req = urllib.request.Request(url, method="HEAD", headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=20) as response:
            return getattr(response, "status", 200)
    except urllib.error.HTTPError as exc:
        if exc.code not in {403, 405}:
            return exc.code
    except Exception:
        pass
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0", "Range": "bytes=0-64"})
        with urllib.request.urlopen(req, timeout=20) as response:
            return getattr(response, "status", 200)
    except Exception:
        return None


def main() -> int:
    bundles = json.loads(BUNDLES.read_text(encoding="utf-8"))
    publications = json.loads(PUBLICATIONS.read_text(encoding="utf-8"))
    results: list[dict] = []
    image_status_cache: dict[str, int | None] = {}

    for host, posts in publications.items():
        expected_by_title = {item["title"]: item for item in bundles[host]}
        for post in posts:
            expected = expected_by_title[post["title"]]
            result = {"host": host, "title": post["title"], "url": post["url"], "errors": [], "warnings": []}
            try:
                status, body = fetch(post["url"])
                result["status"] = status
                parser = PageParser()
                parser.feed(body)
                result["page_title"] = parser.title
                if status != 200:
                    result["errors"].append(f"HTTP {status}")
                if expected["title"].lower() not in parser.title.lower():
                    result["errors"].append("title mismatch")
                matches = [link for link in parser.links if link["href"].rstrip("/") == expected["target_url"].rstrip("/")]
                if not matches:
                    result["errors"].append("target link missing")
                else:
                    result["anchor"] = matches[0]["text"]
                    result["rel"] = matches[0]["rel"]
                    if matches[0]["text"].strip().lower() != expected["anchor"].strip().lower():
                        result["errors"].append("anchor mismatch")
                    forbidden_rel = {"nofollow", "ugc", "sponsored"}
                    if forbidden_rel.intersection(matches[0]["rel"].lower().split()):
                        result["errors"].append("non-dofollow relation present")
                expected_image = expected["image"]
                image_matches = [img for img in parser.images if img["src"] == expected_image]
                if not image_matches:
                    result["errors"].append("expected image missing or URL altered")
                else:
                    result["image_alt"] = image_matches[0]["alt"]
                    if expected_image not in image_status_cache:
                        image_status_cache[expected_image] = check_image(expected_image)
                    image_status = image_status_cache[expected_image]
                    result["image_status"] = image_status
                    if image_status is None or image_status >= 400:
                        result["errors"].append("image did not return a successful status")
                    if not image_matches[0]["alt"].strip():
                        result["errors"].append("image alt missing")
                if not parser.meta_description:
                    result["warnings"].append("platform emitted no meta description")
            except Exception as exc:
                result["errors"].append(f"fetch failed: {exc}")
            result["ok"] = not result["errors"]
            results.append(result)

    payload = {
        "total": len(results),
        "pass": sum(1 for item in results if item["ok"]),
        "fail": sum(1 for item in results if not item["ok"]),
        "results": results,
    }
    REPORT.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({k: payload[k] for k in ("total", "pass", "fail")}, indent=2))
    for item in results:
        if item["errors"]:
            print(item["url"], *item["errors"], sep="\n  ")
    return 1 if payload["fail"] else 0


if __name__ == "__main__":
    raise SystemExit(main())

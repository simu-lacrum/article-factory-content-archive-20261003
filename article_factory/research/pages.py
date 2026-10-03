from __future__ import annotations

import hashlib
import ipaddress
import re
import socket
import urllib.request
from datetime import datetime, timezone
from urllib.parse import urljoin, urlsplit

from bs4 import BeautifulSoup

from .models import canonical_url, key

IGNORED = "script,style,noscript,nav,footer,aside,form,[role=navigation],[role=banner],[role=contentinfo]"


def phrase_count(text: str, phrase: str) -> int:
    needle = key(phrase)
    return len(re.findall(r"(?<!\w)" + re.escape(needle) + r"(?!\w)", key(text))) if needle else 0


def anchor_kind(text: str, url: str, query: str, brands: list[str]) -> str:
    normalized = key(text)
    if not normalized:
        return "image_or_empty"
    if re.match(r"^(https?://|www\.|[a-z0-9-]+\.[a-z]{2,}(?:/|$))", text.strip(), re.I) or normalized == key(urlsplit(url).netloc):
        return "naked_url"
    if normalized in {"click here", "here", "learn more", "read more", "website", "visit", "visit site", "visit website", "source", "link"}:
        return "generic"
    if any(phrase_count(text, brand) for brand in brands if brand):
        return "branded"
    if normalized == key(query):
        return "exact_match"
    if phrase_count(text, query):
        return "partial_match"
    return "descriptive"


def extract_page(html: str, url: str, query: str = "", brands: list[str] | None = None, extraction_rule: dict | None = None) -> dict:
    soup = BeautifulSoup(html, "html.parser")
    title = soup.title.get_text(" ", strip=True) if soup.title else ""
    description = soup.find("meta", attrs={"name": re.compile("^description$", re.I)})
    canonical = soup.find("link", rel="canonical")
    # Hero headings can be siblings of <main>; retain their actual HTML presence.
    document_h1 = [h.get_text(" ", strip=True) for h in soup.find_all("h1")]
    if extraction_rule:
        from .models import validate_extraction_rule
        validate_extraction_rule(extraction_rule)
        roots = soup.select(extraction_rule["content_selector"])
        if len(roots) != extraction_rule.get("expected_matches", 1):
            raise ValueError("Reviewed content selector no longer matches the expected number of blocks")
        if any(a in b.parents for a in roots for b in roots if a is not b):
            raise ValueError("Reviewed content selector matches overlapping blocks")
        fallback = False
    else:
        candidates = soup.find_all("main") or soup.find_all("article")
        root = max(candidates, key=lambda el: len(el.get_text())) if candidates else soup.body or soup
        roots = [root]
        fallback = root == soup.body or root == soup
    links = []
    for a in soup.find_all("a", href=True):
        href = urljoin(url, a["href"])
        if urlsplit(href).scheme not in {"http", "https"}:
            continue
        placement = "editorial"
        for parent in a.parents:
            if getattr(parent, "name", None) in {"nav", "footer", "header", "aside"} or parent.get("role") in {"navigation", "banner", "contentinfo"}:
                placement = "navigation"
                break
        if placement == "editorial" and not any(root is a or root in a.parents for root in roots):
            placement = "other"
        text = a.get_text(" ", strip=True)
        links.append({"text": text, "url": href, "placement": placement,
                      "relationship": "internal" if urlsplit(canonical_url(href)).netloc == urlsplit(canonical_url(url)).netloc else "outbound",
                      "kind": anchor_kind(text, href, query, brands or []), "rel": a.get("rel", [])})
    headings = []
    for root in roots:
        for el in root.select(IGNORED):
            el.decompose()
        block_headings = ([root] if re.fullmatch("h[1-6]", root.name or "") else []) + root.find_all(re.compile("^h[1-6]$"))
        headings.extend({"level": int(h.name[1]), "text": h.get_text(" ", strip=True)} for h in block_headings)
    text = "\n\n".join(root.get_text(" ", strip=True) for root in roots)
    if extraction_rule and not text.strip():
        raise ValueError("Reviewed content selector returned empty text")
    language = (soup.html.get("lang", "") if soup.html else "").split("-")[0].lower()
    if not language:
        language = "ru" if len(re.findall(r"[а-яё]", text, flags=re.I)) > len(re.findall(r"[a-z]", text, flags=re.I)) else "en"
    return {"url": url, "canonical": urljoin(url, canonical["href"]) if canonical and canonical.get("href") else url,
            "language": language,
            "title": title, "description": description.get("content", "") if description else "",
            "headings": headings, "document_h1": document_h1, "text": text, "words": len(key(text).split()), "links": links,
            "extraction": "reviewed_content_selector" if extraction_rule else "body_fallback_review_needed" if fallback else "semantic_main",
            "extraction_rule": extraction_rule,
            "sha256": hashlib.sha256(html.encode()).hexdigest(), "captured_at": datetime.now(timezone.utc).isoformat(),
            "claims_status": "unverified_publisher_claims"}


def public_url(url: str) -> None:
    parts = urlsplit(url)
    if parts.scheme not in {"http", "https"} or not parts.hostname or parts.username or parts.password:
        raise ValueError("Only public HTTP(S) pages are supported")
    for entry in socket.getaddrinfo(parts.hostname, parts.port or (443 if parts.scheme == "https" else 80)):
        if not ipaddress.ip_address(entry[4][0]).is_global:
            raise ValueError("Private or local network URLs are not research sources")


class PublicRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        public_url(newurl)
        return super().redirect_request(req, fp, code, msg, headers, newurl)


def fetch_page(url: str, query: str = "", brands: list[str] | None = None, extraction_rule: dict | None = None) -> tuple[dict, str]:
    public_url(url)
    request = urllib.request.Request(url, headers={"User-Agent": "ArticleFactoryResearch/2.0 (public editorial research)"})
    with urllib.request.build_opener(PublicRedirect()).open(request, timeout=25) as response:
        content_type = response.headers.get_content_type()
        if content_type not in {"text/html", "application/xhtml+xml"}:
            raise ValueError(f"Expected HTML, got {content_type}")
        raw = response.read(4_000_001)
        if len(raw) > 4_000_000:
            raise ValueError("Page exceeds research size limit")
        html = raw.decode(response.headers.get_content_charset() or "utf-8", errors="replace")
        page = extract_page(html, response.url, query, brands, extraction_rule)
        page["requested_url"] = url
        page["http_status"] = response.status
        return page, html

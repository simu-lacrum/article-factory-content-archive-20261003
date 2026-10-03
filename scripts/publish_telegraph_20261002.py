from __future__ import annotations

import json
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request, urlopen


class Node:
    def __init__(self, tag: str | None = None, attrs: dict[str, str] | None = None):
        self.tag = tag
        self.attrs = attrs or {}
        self.children: list[Node | str] = []


class TreeParser(HTMLParser):
    void = {"br", "img", "hr", "meta", "link", "input"}

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.root = Node("root")
        self.stack = [self.root]

    def handle_starttag(self, tag, attrs):
        node = Node(tag.lower(), dict(attrs))
        self.stack[-1].children.append(node)
        if tag.lower() not in self.void:
            self.stack.append(node)

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)

    def handle_endtag(self, tag):
        tag = tag.lower()
        for i in range(len(self.stack) - 1, 0, -1):
            if self.stack[i].tag == tag:
                del self.stack[i:]
                break

    def handle_data(self, data):
        if data:
            self.stack[-1].children.append(data)


def clean_text(text: str) -> str:
    return " ".join(text.split())


def inline(node: Node | str):
    if isinstance(node, str):
        text = clean_text(node)
        return text or None
    tag = node.tag
    if tag in {"strong", "b", "em", "i", "code"}:
        children = [x for c in node.children if (x := inline(c)) is not None]
        return {"tag": "strong" if tag in {"strong", "b"} else "em", "children": children} if children else None
    if tag == "a":
        children = [x for c in node.children if (x := inline(c)) is not None]
        href = node.attrs.get("href")
        if href and children:
            return {"tag": "a", "attrs": {"href": href}, "children": children}
        return children[0] if len(children) == 1 else children
    if tag == "br":
        return "\n"
    children = [x for c in node.children if (x := inline(c)) is not None]
    if not children:
        return None
    if len(children) == 1:
        return children[0]
    return children


def blocks(node: Node):
    result = []
    for child in node.children:
        if isinstance(child, str):
            continue
        tag = child.tag
        if tag in {"h1", "h2", "h3", "h4"}:
            children = [x for c in child.children if (x := inline(c)) is not None]
            if children:
                result.append({"tag": "h3" if tag in {"h1", "h4"} else tag, "children": children})
        elif tag in {"p", "blockquote"}:
            children = [x for c in child.children if (x := inline(c)) is not None]
            if children:
                result.append({"tag": "blockquote" if tag == "blockquote" else "p", "children": children})
        elif tag in {"ul", "ol"}:
            items = []
            for c in child.children:
                if isinstance(c, Node) and c.tag == "li":
                    children = [x for cc in c.children if (x := inline(cc)) is not None]
                    if children:
                        items.append({"tag": "li", "children": children})
            if items:
                result.append({"tag": "ol" if tag == "ol" else "ul", "children": items})
        elif tag == "figure":
            for c in child.children:
                if isinstance(c, Node) and c.tag == "img" and c.attrs.get("src"):
                    result.append({"tag": "img", "attrs": {"src": c.attrs["src"]}})
                elif isinstance(c, Node) and c.tag == "figcaption":
                    children = [x for cc in c.children if (x := inline(cc)) is not None]
                    if children:
                        result.append({"tag": "p", "children": children})
    return result


def api(method: str, params: dict[str, str]):
    body = urlencode(params).encode()
    req = Request(f"https://api.telegra.ph/{method}", data=body, method="POST")
    req.add_header("Content-Type", "application/x-www-form-urlencoded")
    with urlopen(req, timeout=60) as resp:
        payload = json.loads(resp.read().decode())
    if not payload.get("ok"):
        raise RuntimeError(payload)
    return payload["result"]


def main():
    html_path = Path(sys.argv[1])
    title = sys.argv[2]
    html = html_path.read_text(encoding="utf-8")
    parser = TreeParser()
    parser.feed(html)
    content = blocks(parser.root)
    account = api("createAccount", {"short_name": "ClusterGuides", "author_name": "Cluster Guides"})
    page = api("createPage", {
        "access_token": account["access_token"],
        "title": title,
        "author_name": "Cluster Guides",
        "content": json.dumps(content, ensure_ascii=False, separators=(",", ":")),
        "return_content": "false",
    })
    print(json.dumps({"url": page["url"], "title": page["title"], "blocks": len(content)}, ensure_ascii=False))


if __name__ == "__main__":
    main()

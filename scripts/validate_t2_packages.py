from __future__ import annotations

import argparse
import itertools
import json
import re
from pathlib import Path


def body_without_frontmatter(text: str) -> str:
    return re.sub(r"\A---\s*\n.*?\n---\s*\n", "", text, count=1, flags=re.S)


def shingles(text: str, size: int = 5) -> set[tuple[str, ...]]:
    words = re.findall(r"[\w-]+", text.lower(), flags=re.UNICODE)
    return {tuple(words[index : index + size]) for index in range(len(words) - size + 1)}


def description_length(text: str) -> int:
    match = re.search(r'^description:\s*["\']?(.*?)["\']?\s*$', text, flags=re.M)
    return len(match.group(1)) if match else -1


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("manifest", type=Path)
    args = parser.parse_args()
    manifest = json.loads(args.manifest.read_text(encoding="utf-8"))
    records = []
    for item in manifest["items"]:
        path = Path(item["output"])
        text = path.read_text(encoding="utf-8")
        body = body_without_frontmatter(text)
        target = json.loads(Path(item["evidence"]).read_text(encoding="utf-8"))["target"]
        records.append((path.name, shingles(body)))
        print(
            json.dumps(
                {
                    "file": path.name,
                    "target_links": body.count(f"]({target})"),
                    "images": len(re.findall(r"!\[[^\]]*\]\(https?://", body)),
                    "h1": len(re.findall(r"(?m)^# ", body)),
                    "tables": len(re.findall(r"(?m)^\|.*\|$", body)),
                    "faq": "## Часто задаваемые вопросы" in body or "## Frequently Asked Questions" in body,
                    "description_chars": description_length(text),
                },
                ensure_ascii=False,
            )
        )

    best = (0.0, "", "")
    for (left_name, left), (right_name, right) in itertools.combinations(records, 2):
        score = len(left & right) / max(1, len(left | right))
        if score > best[0]:
            best = (score, left_name, right_name)
    print(json.dumps({"max_pairwise_5gram_jaccard": round(best[0], 4), "pair": best[1:]}, ensure_ascii=False))


if __name__ == "__main__":
    main()

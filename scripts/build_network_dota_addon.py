from __future__ import annotations

import html
import json
import re
from pathlib import Path

import build_network_t2_batch as base


ROOT = Path(__file__).resolve().parents[1]
RUN_ID = "20260913-101654"
ARTICLE_DIR = ROOT / "output" / "articles" / RUN_ID
RUN_MANIFEST = ROOT / "output" / "runs" / f"{RUN_ID}.json"
PUBLISH_DIR = ROOT / "output" / "publish" / "20260913-network-7x10"
BUNDLES_PATH = PUBLISH_DIR / "bundles.json"


DOTA_TARGETS = [
    {
        "url": "https://melonity.gg/en",
        "anchors": [
            "dota 2 cheats",
            "best dota 2 hacks",
            "top dota 2 cheats",
            "Dota 2 cheat tools",
            "private Dota 2 hacks",
            "Dota 2 cheats guide",
            "Dota 2 hack platform",
        ],
        "image": "https://melonity.gg/_og/d/c_MyOg,p_Ii9lbiI,s_kbWb2SCb-wjt7IxQ.png",
        "alt": "Melonity Dota 2 product page preview used for an editorial review",
        "source": "knowledge/agent_memory/sources/t2-targets-2026-08-13/en.md",
        "subject": "the Melonity Dota 2 product page",
        "audience": "Dota 2 players comparing hero scripts, visual information tools, access terms, and support context",
        "page_job": "explain what is currently presented, distinguish observable interface information from vendor claims, and keep risk visible",
        "proof_limit": "A first-party page can document the vendor's current positioning and visible feature categories. It cannot guarantee future compatibility, account outcomes, or permanent detection status.",
        "dimensions": ["feature categories", "hero coverage", "interface clarity", "access terms", "support context"],
        "red_flags": ["absolute safety language", "feature counts without scope", "undated compatibility claims"],
        "detail_heading": "Dota 2 Product Pages Need Scope, Not Swagger",
        "detail": "A Dota 2 product page may combine hero scripts, map information, utility features, access plans, and support promises in one long scroll. Review those layers separately. Hero-specific examples show depth for named kits, while map or HUD features describe broader categories. Pricing and trial language belongs to a dated access check, not to a timeless feature summary. The same boundary applies to safety wording: a vendor can describe its own systems, but readers still need to treat rule, account, and device-security risk as unresolved. The most useful page is not the one with the loudest number. It is the one that lets a reader identify what is shown, what is claimed, what was checked, and what could change after a patch.",
        "primary": [
            "Dota 2 cheat search intent",
            "Dota 2 cheat product evidence",
            "Dota 2 cheat feature priorities",
            "Dota 2 cheat claim freshness",
            "Dota 2 cheat comparison criteria",
            "Dota 2 cheat screenshot evidence",
            "Dota 2 cheat buyer questions",
        ],
        "titles": [
            "Dota 2 Cheat Searches: Features vs Evidence",
            "How to Verify a Dota 2 Cheat Product Page",
            "Dota 2 Cheat Features That Matter in Real Use",
            "When Dota 2 Cheat Claims Need Rechecking",
            "Compare Dota 2 Cheats by Fit, Not Feature Count",
            "What Dota 2 Cheat Screenshots Can Actually Prove",
            "Dota 2 Cheat Buyer Questions Before You Commit",
        ],
    },
    {
        "url": "https://cheatsgaming.com/games/dota-2/top-5-hacks-and-cheats-for-dota-2-best-hack-for-dota-2-04ebc1f21fc6",
        "anchors": [
            "dota 2 hacks",
            "top dota 2 cheats",
            "best dota 2 hacks",
            "Dota 2 cheat comparison",
            "private Dota 2 cheats",
            "Dota 2 hacks guide",
            "top Dota 2 hack list",
        ],
        "image": "https://cheatsgaming.com/media/medium/313b60a16e6b505b3f1b5e5c.png",
        "alt": "Dota 2 product comparison image from the referenced CheatsGaming guide",
        "source": "knowledge/agent_memory/sources/cheatsgaming-t2-12-20260910-links/top-5-hacks-and-cheats-for-dota-2-best-hack-for-dota-2-04ebc1f21fc6.md",
        "subject": "a ranked Dota 2 cheat guide",
        "audience": "Dota 2 readers looking for a shortlist without treating a ranking as a permanent verdict",
        "page_job": "show selection criteria, date patch-sensitive claims, separate feature presence from quality, and explain who each option may fit",
        "proof_limit": "A ranking can organize a dated shortlist and make its criteria explicit. It cannot create a universal winner or prove future product status and safety.",
        "dimensions": ["status freshness", "feature fit", "access clarity", "support route", "risk disclosure"],
        "red_flags": ["permanent winner language", "rankings without criteria", "safety promises inferred from screenshots"],
        "detail_heading": "A Dota 2 Ranking Is a Dated Decision Model",
        "detail": "The word best only becomes useful after the article names a reader and a priority. One player may care about hero-specific depth, another about visual clarity, and another about transparent access and support. A responsible Dota 2 shortlist gives those priorities separate weight instead of hiding them inside one score. It also states when status, pricing, and supported-build details were checked. Screenshots can document interface categories or a captured state, but they do not establish current compatibility or remove account risk. A good ranking therefore works like a filter: define the job, eliminate obvious mismatches, verify the live official source, and keep the conclusion narrow enough to survive honest scrutiny.",
        "primary": [
            "top Dota 2 cheat criteria",
            "Dota 2 hack ranking evidence",
            "Dota 2 hack shortlist",
            "Dota 2 hack ranking freshness",
            "weighted Dota 2 cheat comparison",
            "Dota 2 hack image evidence",
            "Dota 2 hack buyer checklist",
        ],
        "titles": [
            "What Top Dota 2 Cheat Lists Should Explain",
            "A Better Evidence Test for Dota 2 Hack Rankings",
            "Build a Dota 2 Hack Shortlist Without the Noise",
            "Why Dota 2 Hack Rankings Expire After Patches",
            "Weighted Criteria for Top Dota 2 Cheat Lists",
            "Read Dota 2 Hack Images Without Overclaiming",
            "Dota 2 Hack Buying Questions Rankings Miss",
        ],
    },
]


def add_image_note(markdown: str, target: dict) -> str:
    image = f"![{target['alt']}]({target['image']})"
    note = f'''<!-- IMAGE_SLOT_01
Placement: after the introduction
Type: real screenshot
Purpose: show the referenced Dota 2 page or comparison image so readers can identify the source being evaluated
Suggested file name: {base.slugify(target['titles'][0])}-source-image.webp
Alt text: {target['alt']}
Caption: Source-page image used for a time-bounded editorial review; it does not prove current safety or compatibility.
-->

{image}'''
    markdown = markdown.replace(image, note, 1)
    source_block = f'''sources_used:
  - "{target['source']}"
'''
    markdown = markdown.replace('image_source: "' + target['image'] + '"\n', 'image_source: "' + target['image'] + '"\n' + source_block, 1)
    return markdown


def main() -> None:
    ARTICLE_DIR.mkdir(parents=True, exist_ok=True)
    base.TARGETS.extend(DOTA_TARGETS)
    manifest = json.loads(RUN_MANIFEST.read_text(encoding="utf-8"))
    bundles = json.loads(BUNDLES_PATH.read_text(encoding="utf-8"))
    for host in base.HOSTS:
        bundles[host["domain"]] = [item for item in bundles[host["domain"]] if item.get("index", 0) < 71]

    index_lines = ["# Dota 2 Add-On: 14 Network Articles", ""]
    manifest_items = []
    local_index = 0
    for host_index, host in enumerate(base.HOSTS):
        host_dir = PUBLISH_DIR / host["domain"]
        host_dir.mkdir(parents=True, exist_ok=True)
        index_lines.extend([f"## {host['domain']}", ""])
        for addon_target_index, target in enumerate(DOTA_TARGETS):
            local_index += 1
            target_index = 10 + addon_target_index
            global_index = 70 + local_index
            markdown, data = base.article_markdown(host_index, target_index)
            markdown = add_image_note(markdown, target)
            filename = f"{local_index:02d}-{data['slug']}.md"
            article_path = ARTICLE_DIR / filename
            article_path.write_text(markdown, encoding="utf-8")

            publish_filename = f"{global_index:02d}-{data['slug']}.md"
            publish_markdown = re.sub(r"<!-- IMAGE_SLOT_01.*?-->\s*", "", markdown, flags=re.S)
            html_body = base.markdown_to_html(publish_markdown)
            (host_dir / publish_filename).write_text(markdown, encoding="utf-8")
            (host_dir / publish_filename.replace(".md", ".html")).write_text(html_body, encoding="utf-8")
            source_helper = (
                '<!doctype html><html><head><meta charset="utf-8"><title>Publish source</title></head><body>'
                f'<label>Title source<textarea aria-label="Title source">{html.escape(data["title"])}</textarea></label>'
                f'<label>HTML source<textarea aria-label="HTML source">{html.escape(html.unescape(html_body))}</textarea></label>'
                f'<label>Description source<textarea aria-label="Description source">{html.escape(data["description"])}</textarea></label>'
                '</body></html>'
            )
            (host_dir / publish_filename.replace(".md", ".source.html")).write_text(source_helper, encoding="utf-8")

            bundle_item = {
                "index": global_index,
                "host_index": 11 + addon_target_index,
                "file": publish_filename,
                "article_file": filename,
                **data,
                "html": html_body,
            }
            bundles[host["domain"]].append(bundle_item)
            prepared = manifest["items"][local_index - 1]
            manifest_items.append({
                **prepared,
                "title": data["title"],
                "game": "dota2",
                "language": "en",
                "status": "article",
                "output": str(article_path),
            })
            index_lines.append(
                f"{addon_target_index + 1}. [{data['title']}](../../articles/{RUN_ID}/{filename}) "
                f"-> [{data['anchor']}]({data['target_url']})"
            )
        index_lines.append("")

    manifest["items"] = manifest_items
    RUN_MANIFEST.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    BUNDLES_PATH.write_text(json.dumps(bundles, ensure_ascii=False, indent=2), encoding="utf-8")
    (PUBLISH_DIR / "DOTA_ADDON_INDEX.md").write_text("\n".join(index_lines), encoding="utf-8")
    print(json.dumps({"articles": local_index, "run_id": RUN_ID, "bundle_items": sum(len(v) for v in bundles.values())}, indent=2))


if __name__ == "__main__":
    main()

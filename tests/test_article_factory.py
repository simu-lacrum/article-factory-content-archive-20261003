from __future__ import annotations

import json
import re
import tempfile
import unittest
from pathlib import Path

from PIL import Image, ImageDraw

from article_factory.cli import init_project
from article_factory.generator import generate_articles
from article_factory.graph_bootstrap import bootstrap_graph_memory
from article_factory.ingest import ingest_workspace
from article_factory.quality import review_article, review_manifest
from article_factory.settings import DEFAULT_DB
from article_factory.workflow import prepare_codex_workflow
from article_factory.topics import rebuild_topic_ideas
from article_factory.visual_fidelity import analyze_warm_story_fidelity


class ArticleFactorySmokeTest(unittest.TestCase):
    def install_mandatory_memory(self, root: Path) -> None:
        (root / "AGENTS.md").write_text("# Agents\n", encoding="utf-8")
        (root / "SEO_ARTICLE_RULES.md").write_text("# Rules\n", encoding="utf-8")
        guide = root / "knowledge" / "agent_memory" / "rules" / "article-visual-prompt-guide.md"
        guide.parent.mkdir(parents=True, exist_ok=True)
        guide.write_text("# Visual guide\n\nMANDATORY_SESSION_GUIDE: test\n", encoding="utf-8")
        facts_dir = root / "knowledge" / "graph_facts"
        facts_dir.mkdir(parents=True, exist_ok=True)
        (facts_dir / "mandatory.json").write_text(
            json.dumps(
                {
                    "entities": [
                        {
                            "id": "instruction:test",
                            "kind": "mandatory_instruction",
                            "label": "Test mandatory instruction",
                            "props": {
                                "mandatory_on_session_start": True,
                                "canonical_file": "knowledge/agent_memory/rules/article-visual-prompt-guide.md",
                                "required_files": ["AGENTS.md", "SEO_ARTICLE_RULES.md"],
                            },
                        }
                    ],
                    "relations": [],
                },
                ensure_ascii=False,
            ),
            encoding="utf-8",
        )

    def test_graph_bootstrap_traverses_every_node_and_edge(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            init_project(root)
            self.install_mandatory_memory(root)
            facts_dir = root / "knowledge" / "graph_facts"
            (facts_dir / "mandatory.json").write_text(
                json.dumps(
                    {
                        "entities": [
                            {
                                "id": "instruction:test",
                                "kind": "mandatory_instruction",
                                "label": "Test mandatory instruction",
                                "props": {
                                    "mandatory_on_session_start": True,
                                    "canonical_file": "knowledge/agent_memory/rules/article-visual-prompt-guide.md",
                                    "required_files": ["AGENTS.md", "SEO_ARTICLE_RULES.md"],
                                },
                            },
                            {"id": "concept:connected", "kind": "concept", "label": "Connected"},
                            {"id": "concept:isolated", "kind": "concept", "label": "Isolated"},
                        ],
                        "relations": [
                            {
                                "source": "instruction:test",
                                "target": "concept:connected",
                                "relation": "requires",
                            }
                        ],
                    },
                    ensure_ascii=False,
                ),
                encoding="utf-8",
            )

            result = bootstrap_graph_memory(root)
            self.assertEqual(result["status"], "PASS")
            self.assertEqual(result["nodes"], "3/3")
            self.assertEqual(result["edges"], "1/1")
            self.assertEqual(result["components"], 2)
            receipt = json.loads((root / "memory" / "graph" / "session-bootstrap.json").read_text(encoding="utf-8"))
            self.assertEqual(len(receipt["visited_node_ids"]), 3)
            self.assertEqual(len(receipt["inspected_edges"]), 1)
            self.assertIn("concept:isolated", receipt["visited_node_ids"])
            self.assertIn(
                "knowledge/agent_memory/rules/article-visual-prompt-guide.md",
                [item["path"] for item in receipt["required_reading"]],
            )

    def test_generated_image_slots_enforce_branch_accent_model_and_score(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            article = Path(tmp) / "article.md"
            article.write_text(
                """---
title: "Visual QA Test"
description: "Visual QA test checks image slot rules."
game: dota2
language: en
primary_keyword: "visual QA test"
---

# Visual QA Test

Melonity appears here as the mapped product.

## Main

Useful article content.

<!-- IMAGE_SLOT_01
Placement: after Main
Type: generated image
Purpose: explain the thesis
Generated sequence index: 1
Style branch: B1
Mapped product and brand color role: Melonity #FF1469 — dominant field replacing yellow/amber
Model: Nano Banana Pro / gemini-3-pro-image
Reference files: knowledge/agent_memory/references/article-editorial-warm-story-v1/reference-01.png; knowledge/agent_memory/references/article-editorial-warm-story-v1/reference-02.png
Reference fidelity target: 4/5 across layout, palette, shapes, depth and typography mass
Prompt QA score: 90
-->

<!-- IMAGE_SLOT_02
Placement: after Main
Type: generated image
Purpose: add a narrative example
Generated sequence index: 2
Style branch: A
Mapped product and brand color role: Melonity #FF1469 — small semantic accent
Model: Nano Banana Pro / gemini-3-pro-image
Prompt QA score: 88
-->

## FAQ

### What is this?

A visual QA fixture.
""",
                encoding="utf-8",
            )
            valid = review_article(article)
            visual_errors = [
                item["message"]
                for item in valid["findings"]
                if item["severity"] == "error" and "IMAGE_SLOT" in item["message"]
            ]
            self.assertEqual(visual_errors, [])

            invalid_text = article.read_text(encoding="utf-8").replace(
                "Style branch: B1", "Style branch: A", 1
            ).replace("Melonity #FF1469", "Melonity #635FD5", 1).replace(
                "Prompt QA score: 90", "Prompt QA score: 70", 1
            )
            article.write_text(invalid_text, encoding="utf-8")
            invalid = review_article(article)
            messages = [item["message"] for item in invalid["findings"]]
            self.assertTrue(any("breaks visual alternation" in message for message in messages))
            self.assertTrue(any("missing mapped brand color #FF1469" in message for message in messages))
            self.assertTrue(any("minimum 80" in message for message in messages))

            missing_refs_text = article.read_text(encoding="utf-8")
            missing_refs_text = missing_refs_text.replace("Style branch: A", "Style branch: B1", 1)
            missing_refs_text = re.sub(
                r"Reference files:.*\nReference fidelity target:.*\n",
                "Reference roles: none\n",
                missing_refs_text,
                count=1,
            )
            article.write_text(missing_refs_text, encoding="utf-8")
            missing_refs = review_article(article)
            missing_messages = [item["message"] for item in missing_refs["findings"]]
            self.assertTrue(any("must name two actual warm-story reference files" in message for message in missing_messages))
            self.assertTrue(any("cannot use Reference roles: none" in message for message in missing_messages))
            self.assertTrue(any("missing the 4/5 reference-fidelity target" in message for message in missing_messages))

    def test_review_respects_explicit_visuals_opt_out(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            article = Path(tmp) / "no-visuals.md"
            article.write_text(
                """---
title: "No Visuals Test"
description: "No visuals test article with an explicit editorial exception."
game: all
language: en
primary_keyword: "no visuals test"
visuals: none
---

# No Visuals Test

No visuals test is the explicit editorial choice for this package.

## Main

This fixture confirms that the review gate accepts a front-matter opt-out instead of requiring an image placement note.

## Context

The exception is deliberate and visible to editors.

## FAQ

### Are visuals required here?

No. The package explicitly omits them.
""",
                encoding="utf-8",
            )
            result = review_article(article)
            messages = [item["message"] for item in result["findings"]]
            self.assertNotIn("No image placement notes detected", messages)

    def test_manifest_enforces_global_generated_visual_sequence(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            articles = []
            for article_number, sequence_index in ((1, 1), (2, 3)):
                article = root / f"article-{article_number}.md"
                article.write_text(
                    f"""---
title: "Sequence Test {article_number}"
description: "Sequence test article {article_number}."
game: all
language: en
primary_keyword: "sequence test"
---

# Sequence Test

## Main

Useful content.

<!-- IMAGE_SLOT_01
Placement: after Main
Type: generated image
Purpose: explain the thesis
Generated sequence index: {sequence_index}
Style branch: B1
Mapped product and brand color role: none
Model: Nano Banana Pro / gemini-3-pro-image
Reference files: knowledge/agent_memory/references/article-editorial-warm-story-v1/reference-01.png; knowledge/agent_memory/references/article-editorial-warm-story-v1/reference-02.png
Reference fidelity target: 4/5 across layout, palette, shapes, depth and typography mass
Prompt QA score: 90
-->

## FAQ

### What is this?

A sequence fixture.
""",
                    encoding="utf-8",
                )
                articles.append(article)
            manifest = root / "manifest.json"
            manifest.write_text(
                json.dumps(
                    {
                        "items": [
                            {"status": "article", "output": str(article)} for article in articles
                        ]
                    }
                ),
                encoding="utf-8",
            )
            review = review_manifest(manifest)
            messages = [
                finding["message"]
                for result in review["results"]
                for finding in result["findings"]
            ]
            self.assertTrue(any("global and contiguous" in message for message in messages))
            self.assertEqual(review["fail"], 1)

    def test_visual_fidelity_rejects_dark_industrial_drift(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            references = root / "references"
            references.mkdir()
            for index, color in enumerate(("#F8CC38", "#F3C445"), start=1):
                image = Image.new("RGB", (200, 200), color)
                draw = ImageDraw.Draw(image)
                draw.rectangle((150, 150, 189, 189), fill="#635FD5")
                image.save(references / f"reference-{index:02d}.png")

            warm_candidate = Image.new("RGB", (320, 180), "#635FD5")
            warm_draw = ImageDraw.Draw(warm_candidate)
            warm_draw.rectangle((205, 45, 319, 179), fill="#F8CC38")
            warm_path = root / "warm.png"
            warm_candidate.save(warm_path)
            warm_report = analyze_warm_story_fidelity(
                warm_path, references, accent="#635FD5"
            )
            self.assertEqual(warm_report["status"], "PASS")

            accent_only_candidate = Image.new("RGB", (320, 180), "#F8CC38")
            accent_only_draw = ImageDraw.Draw(accent_only_candidate)
            accent_only_draw.rectangle((270, 135, 319, 179), fill="#635FD5")
            accent_only_path = root / "accent-only.png"
            accent_only_candidate.save(accent_only_path)
            accent_only_report = analyze_warm_story_fidelity(
                accent_only_path, references, accent="#635FD5"
            )
            self.assertEqual(accent_only_report["status"], "FAIL")
            self.assertIn("yellow_amber_field_not_replaced", accent_only_report["flags"])
            self.assertIn("mapped_brand_field_below_25_percent", accent_only_report["flags"])

            dark_candidate = Image.new("RGB", (320, 180), "#343434")
            dark_draw = ImageDraw.Draw(dark_candidate)
            dark_draw.rectangle((318, 178, 319, 179), fill="#635FD5")
            dark_path = root / "dark.png"
            dark_candidate.save(dark_path)
            dark_report = analyze_warm_story_fidelity(
                dark_path, references, accent="#635FD5"
            )
            self.assertEqual(dark_report["status"], "FAIL")
            self.assertIn("too_desaturated_for_branch_b", dark_report["flags"])
            self.assertIn("warm_secondary_support_missing", dark_report["flags"])
            self.assertIn("dark_industrial_mass_too_large", dark_report["flags"])

    def test_legacy_template_option_produces_a_codex_brief(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "brand.md").write_text(
                """# Brand Knowledge

## Tone

Write useful, grounded SEO articles. Mention Melonity natively and avoid unsupported guarantees.

## Product

Melonity can be framed as a premium gaming-assistance product for consistency and awareness.
""",
                encoding="utf-8",
            )
            (root / "semantic.csv").write_text(
                """Кластер;Tier;KD ТОП-5;Комментарий;Ключевое слово;Точная частотность;Частотность Весь мир
GENERAL: behavior;general;3;low competition;behavior score dota 2;120;1200
GENERAL: behavior;general;3;low competition;how to raise behavior score dota 2;90;900
""",
                encoding="utf-8",
            )
            init_project(root)
            stats = ingest_workspace(root / DEFAULT_DB, root, rebuild=True)
            topics = rebuild_topic_ideas(root / DEFAULT_DB, root)
            self.assertGreaterEqual(stats.sources, 2)
            self.assertGreaterEqual(topics, 1)
            manifest = generate_articles(
                root / DEFAULT_DB,
                root / "output",
                "Generate 1 SEO article, expert style, native Melonity integration",
                count=1,
                game="general",
                language="en",
                llm_provider="template",
            )
            self.assertEqual(manifest["items"][0]["status"], "brief")
            self.assertIn("needs_codex", Path(manifest["items"][0]["output"]).read_text(encoding="utf-8"))
            manifest_path = Path(manifest["items"][0]["output"]).parents[2] / "runs" / f"{manifest['created_at']}.json"
            self.assertTrue(manifest_path.exists())
            review = review_manifest(manifest_path)
            self.assertEqual(review["total"], 1)
            self.assertEqual(review["results"][0]["status"], "not_generated")

    def test_prepare_creates_current_codex_task(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "brand.md").write_text("# Brand\n\nMelonity context.\n", encoding="utf-8")
            (root / "semantic.csv").write_text(
                """Кластер;Tier;KD ТОП-5;Комментарий;Ключевое слово;Точная частотность;Частотность Весь мир
GENERAL: topic;general;3;low competition;dota 2 behavior score;100;1000
""",
                encoding="utf-8",
            )
            init_project(root)
            self.install_mandatory_memory(root)
            result = prepare_codex_workflow(
                root,
                "Generate 1 SEO article, expert style, native Melonity integration",
                count=1,
                game="general",
                language="en",
                rebuild=True,
            )
            self.assertTrue(Path(result["current_task"]).exists())
            self.assertTrue(Path(result["task"]["manifest"]).exists())
            task_text = Path(result["task"]["task"]).read_text(encoding="utf-8")
            self.assertIn("alternate style branches", task_text)
            self.assertIn("odd = B warm narrative", task_text)
            self.assertIn("two persistent warm-story reference files", task_text)
            self.assertIn("Cluster #635FD5", task_text)
            self.assertIn("Melonity #FF1469", task_text)
            review = review_manifest(Path(result["task"]["manifest"]))
            self.assertEqual(review["fail"], 1)

    def test_prepare_respects_published_memory_after_rebuild(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "brand.md").write_text("# Brand\n\nMelonity context.\n", encoding="utf-8")
            (root / "semantic.csv").write_text(
                """Кластер;Tier;KD ТОП-5;Комментарий;Ключевое слово;Точная частотность;Частотность Весь мир
GENERAL: topic;general;3;low competition;dota 2 behavior score;100;1000
GENERAL: other;general;3;low competition;dota 2 low priority;80;900
""",
                encoding="utf-8",
            )
            init_project(root)
            self.install_mandatory_memory(root)
            (root / "published" / "articles.csv").write_text(
                "title,slug,game,language,url,published_at,notes\n"
                "the topic: dota 2 behavior score explained,old,dota2,en,https://example.com,2026-01-01,\n",
                encoding="utf-8",
            )
            result = prepare_codex_workflow(
                root,
                "Generate 1 SEO article, expert style, native Melonity integration",
                count=1,
                game="general",
                language="en",
                rebuild=True,
            )
            self.assertEqual(result["ingest"]["published_articles"], 1)


if __name__ == "__main__":
    unittest.main()

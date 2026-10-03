import json
import tempfile
import unittest
from pathlib import Path

from article_factory.tumblr_export import clean_markdown, export_articles, markdown_to_html


SAMPLE = """---
title: "Sample"
slug: sample
---

# Sample article

<!-- IMAGE_SLOT_01
Private image production note.
-->

Intro with **bold text** and a [source](https://example.com/story).

## Useful section

- First item
- Second item

1. First step
2. Second step

## Internal-link suggestions

- Add a private link later.

## FAQ

### Does this remain?

Yes.
"""


class TumblrExportTests(unittest.TestCase):
    def test_clean_markdown_removes_private_layers(self):
        cleaned = clean_markdown(SAMPLE)
        self.assertTrue(cleaned.startswith("# Sample article\n"))
        self.assertNotIn("slug: sample", cleaned)
        self.assertNotIn("IMAGE_SLOT", cleaned)
        self.assertNotIn("Internal-link suggestions", cleaned)
        self.assertNotIn("private link", cleaned)
        self.assertIn("## FAQ", cleaned)
        self.assertIn("[source](https://example.com/story)", cleaned)

    def test_markdown_to_html_preserves_public_formatting(self):
        converted = markdown_to_html(clean_markdown(SAMPLE))
        self.assertIn("<h1>Sample article</h1>", converted)
        self.assertIn("<strong>bold text</strong>", converted)
        self.assertIn('<a href="https://example.com/story">source</a>', converted)
        self.assertIn("<ul>\n<li>First item</li>", converted)
        self.assertIn("<ol>\n<li>First step</li>", converted)
        self.assertIn("<h3>Does this remain?</h3>", converted)
        self.assertNotIn("<!--", converted)

    def test_export_articles_writes_both_formats_and_manifest(self):
        with tempfile.TemporaryDirectory() as temporary_dir:
            root = Path(temporary_dir)
            source_dir = root / "source"
            output_dir = root / "output"
            source_dir.mkdir()
            (source_dir / "01-sample.md").write_text(SAMPLE, encoding="utf-8")

            manifest = export_articles(source_dir, output_dir)

            self.assertEqual(manifest["article_count"], 1)
            self.assertTrue((output_dir / "markdown" / "01-sample.md").is_file())
            self.assertTrue((output_dir / "html" / "01-sample.html").is_file())
            self.assertTrue((output_dir / "INDEX.md").is_file())
            saved = json.loads((output_dir / "manifest.json").read_text(encoding="utf-8"))
            self.assertEqual(saved["articles"][0]["links"], 1)


if __name__ == "__main__":
    unittest.main()

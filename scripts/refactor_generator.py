"""One-off, idempotent removal of obsolete deterministic article templates."""
from pathlib import Path

path = Path(__file__).resolve().parents[1] / "article_factory" / "generator.py"
text = path.read_text(encoding="utf-8")
start = text.find("def generate_template_article(")
end = text.find("def fallback_brief(")
if start >= 0:
    text = text[:start] + text[end:]
text = text.replace("status: needs_llm", "status: needs_codex")
text = text.replace('    if len(topics) < spec.count and spec.language != "all":\n        topics.extend(\n            dict(row)\n            for row in db.list_topics(spec.game, "all", candidate_count - len(topics), include_restricted=include_restricted)\n        )\n', '')
text = text.replace('strftime("%Y%m%d-%H%M%S")', 'strftime("%Y%m%d-%H%M%S-%f")')
old = '''        if llm_provider == "template":
            result = LlmResult(
                text=generate_template_article(spec, topic, evidence),
                provider="template",
                model="deterministic-template",
            )'''
new = '''        if llm_provider == "template":
            result = LlmResult(text="", provider="none", model=None,
                               error="Template articles retired: Codex must write the final article from the brief.")'''
text = text.replace(old, new)
text = text.replace('        used_ids.append(int(topic["id"]))', '        if status == "article":\n            used_ids.append(int(topic["id"]))')
path.write_text(text, encoding="utf-8")

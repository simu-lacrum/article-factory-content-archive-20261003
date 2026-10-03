"""Refresh a prepared run's research passages without selecting new topics."""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from article_factory.research.service import research_evidence, writing_contract, save_json
from article_factory.generator import ArticleSpec, build_prompt

manifest = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
spec = ArticleSpec(**manifest["spec"])
for item in manifest["items"]:
    path = Path(item["evidence"])
    payload = json.loads(path.read_text(encoding="utf-8"))
    topic = payload["topic"]
    payload["evidence"] = research_evidence(ROOT, topic)
    payload["research_contract"] = writing_contract(ROOT, topic)
    if payload["research_contract"].get("article_target_query"):
        topic["main_query"] = payload["research_contract"]["article_target_query"]
    save_json(path, payload)
    prompt = build_prompt(spec, topic, payload["evidence"]) + "\nRESEARCH AND READER CONTRACT:\n" + json.dumps(payload["research_contract"], ensure_ascii=False, indent=2)
    Path(item["prompt"]).write_text(prompt + "\n", encoding="utf-8")
    print(json.dumps({"title": item["title"], "sources": [x["source"] for x in payload["evidence"]]}))

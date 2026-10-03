---
source: AI_MEMORY_INTEGRATION.md
heading: "Recommended workflow"
---

## Recommended workflow

```powershell
python -m article_factory prepare --spec "Сгенерируй 10 SEO статей объемом 1800-2400 words, в экспертном стиле, с нативной интеграцией Melonity" --count 10 --game dota2 --language en --rebuild
python -m article_factory review output\runs\<timestamp>.json
```

After publication:

```powershell
python -m article_factory published add --title "..." --slug "..." --game dota2 --language en --url "..."
python -m article_factory ingest
python -m article_factory ai-memory export
```

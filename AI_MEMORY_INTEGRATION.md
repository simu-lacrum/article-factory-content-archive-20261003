# ai-memory Integration

Article Factory and `ai-memory` solve different layers:

- Article Factory is the domain system: sources, semantic clusters, topic selection, evidence packs, generation, review, publication memory.
- `ai-memory` is the agent memory layer: session capture, handoff, cross-agent wiki, and persistent project memory.

Use both together:

1. Run Article Factory ingest and export:

```powershell
python -m article_factory ingest --rebuild
python -m article_factory ai-memory export
```

2. Start `ai-memory` in zero-LLM mode, if Docker Desktop is running:

```powershell
.\scripts\start-ai-memory.ps1
```

3. Add MCP configs:

- Article Factory: `config/mcp.article-factory.example.json`
- ai-memory: `config/mcp.ai-memory.example.json`

4. Tell the agent to use Article Factory for source-grounded article generation and ai-memory for persistent project/session memory.

## Why zero-LLM mode is acceptable

The current `ai-memory` README documents that its Docker quick start can omit LLM and embedding environment variables; FTS5 search still works without keys. That is enough for free local memory and handoff. Paid providers can be added later for consolidated pages and auto-improvement.

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

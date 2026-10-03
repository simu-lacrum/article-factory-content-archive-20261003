---
source: AI_MEMORY_INTEGRATION.md
heading: "ai-memory Integration"
---

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

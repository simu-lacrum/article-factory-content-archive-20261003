---
source: SYSTEM_ARCHITECTURE.md
heading: "Core modules"
---

## Core modules

- `article_factory.ingest` - reads source files and URLs, chunks text, extracts semantic clusters.
- `article_factory.db` - SQLite schema, FTS search, topic and publication tables.
- `article_factory.topics` - turns semantic clusters and curated cluster maps into article ideas.
- `article_factory.generator` - builds evidence packs, prompts, briefs, and LLM drafts.
- `article_factory.codex_task` - prepares Codex-only writing tasks without external LLM APIs.
- `article_factory.quality` - checks generated articles against structure and risk rules.
- `article_factory.ai_memory` - exports a compact wiki snapshot for external memory systems.
- `article_factory.mcp_server` - exposes status, search, topic selection, draft generation, and memory export as MCP tools.
- `article_factory.doctor` - checks local providers, Docker, Ollama, OpenAI key, and optional PDF support.

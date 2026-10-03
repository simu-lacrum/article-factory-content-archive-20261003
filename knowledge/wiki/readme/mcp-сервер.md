---
source: README.md
heading: "MCP-сервер"
---

## MCP-сервер

В проекте есть простой stdio MCP server. Его можно подключить к MCP-клиенту как локальный инструмент:

```json
{
  "mcpServers": {
    "article-factory": {
      "command": "python",
      "args": [
        "-m",
        "article_factory.mcp_server",
        "--root",
        "C:\\Users\\User\\Desktop\\articles"
      ]
    }
  }
}
```

Инструменты:

- `article_factory_status`
- `article_factory_search`
- `article_factory_topics`
- `article_factory_draft`
- `article_factory_codex_task`
- `article_factory_prepare`
- `article_factory_export_memory`
- `article_factory_export_graph`
- `article_factory_graph_bootstrap`

Так Codex сможет сам искать знания, выбирать темы и подготавливать writing tasks через локальную систему.

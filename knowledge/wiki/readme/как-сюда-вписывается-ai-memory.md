---
source: README.md
heading: "Как сюда вписывается ai-memory"
---

## Как сюда вписывается ai-memory

`ai-memory` полезен как долговременная память агента между сессиями, но ядро контентной системы здесь локальное: SQLite + markdown wiki. Команда:

```powershell
python -m article_factory ai-memory export
```

создаёт `memory/ai-memory-export/` с `index.md`, `project-summary.md`, `topic-priorities.md`, `source-inventory.md`, `semantic-clusters.md`. Эти файлы можно подключить к `ai-memory` или любому MCP/wiki-memory инструменту как сжатый снимок проекта.

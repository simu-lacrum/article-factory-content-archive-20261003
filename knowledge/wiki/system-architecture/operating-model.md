---
source: SYSTEM_ARCHITECTURE.md
heading: "Operating model"
---

## Operating model

1. Put sources into the workspace.
2. Run `python -m article_factory prepare --spec "..." --count N --game dota2 --language en`.
3. Codex opens `CURRENT_CODEX_TASK.md`, reads prompts/evidence, and writes the articles.
4. Run `review` on the generation manifest.
5. Publish manually after review.
6. Add published URLs to `published/articles.csv`.

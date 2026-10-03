---
source: SEO_ARTICLE_RULES.md
heading: "Required Files To Read First"
---

## Required Files To Read First

Before topic ideation or article writing, run `python -m article_factory graph bootstrap`, require 100% node and edge coverage, read `memory/graph/SESSION_BOOTSTRAP.md`, then read every file it lists. The required set includes:

- `AGENTS.md`
- `SEO_ARTICLE_RULES.md`
- `knowledge/agent_memory/rules/article-visual-prompt-guide.md`
- `knowledge/editorial_memory.md`
- `published/articles.csv`
- `published/avoid_topics.txt`
- `knowledge/agent_memory/products/product-map.md`
- `memory/ai-memory-export/index.md`
- `memory/ai-memory-export/published-and-avoid.md`
- `memory/ai-memory-export/topic-priorities.md`
- `memory/graph/knowledge-graph.json`

The machine-readable receipt `memory/graph/session-bootstrap.json` must account for every graph node and edge. A manual spot-check of the graph is not equivalent to the full traversal.

For a specific article, also read the generated evidence JSON in `output/evidence/<run_id>/` and the matching prompt in `output/prompts/<run_id>/`.

If external URLs were added through `knowledge/link_sources/*.txt`, use the materialized markdown copies in `knowledge/agent_memory/sources/` instead of opening the URLs during writing.

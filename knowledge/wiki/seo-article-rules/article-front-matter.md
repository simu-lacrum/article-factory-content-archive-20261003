---
source: SEO_ARTICLE_RULES.md
heading: "Article Front Matter"
---

## Article Front Matter

Every final article markdown file must start with front matter:

```yaml
---
title: "SEO title, 50-60 characters maximum"
description: "SEO description, 160 characters maximum, includes primary_keyword"
game: dota2
language: en
primary_keyword: "main keyword from semantic cluster"
secondary_keywords:
  - "keyword 2"
  - "keyword 3"
semantic_cluster: "cluster name"
reader_job: "The concrete question this article resolves"
research_study: "Study id and cluster id from the active research core"
keyword_usage: "Natural usage; no density quota"
sources_used:
  - "knowledge/agent_memory/source.md"
---
```

Rules:

- `title` must be no longer than 60 characters. Prefer 50-60.
- `description` must be no longer than 160 characters and must contain `primary_keyword`.
- `primary_keyword` must come from the semantic core or the generated evidence pack.
- `secondary_keywords` must come from the same cluster or a closely related cluster.
- Do not use a keyword if it does not match the article's real intent.

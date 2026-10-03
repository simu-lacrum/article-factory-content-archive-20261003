---
source: AGENTS.md
heading: "Publication Memory"
---

## Publication Memory

After an article is published, add it:

```powershell
python -m article_factory published add --title "<TITLE>" --slug "<SLUG>" --game dota2 --language en --url "<URL>"
python -m article_factory ingest
```

This prevents duplicate topic selection in future runs.

For broader duplicate prevention, add patterns to `published/avoid_topics.txt`.

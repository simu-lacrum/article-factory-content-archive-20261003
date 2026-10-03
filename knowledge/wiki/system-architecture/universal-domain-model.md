---
source: SYSTEM_ARCHITECTURE.md
heading: "Universal domain model"
---

## Universal domain model

The code treats `dota2` and `cs2` as current domains, not the only possible domains. Unknown future CSVs are assigned to `general` unless a file name or headers allow detection. Commands accept arbitrary `--game` values, so future domain-specific importers can be added without changing the article pipeline.

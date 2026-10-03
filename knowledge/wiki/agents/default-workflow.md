---
source: AGENTS.md
heading: "Default Workflow"
---

## Default Workflow

1. Complete the mandatory session memory bootstrap above.

2. Inspect the current state:

```powershell
python -m article_factory doctor
python -m article_factory status
```

3. Prepare the full writing workflow from the user's natural-language spec:

```powershell
python -m article_factory prepare --spec "<USER SPEC>" --count <N> --game dota2 --language en
```

Use `--rebuild` if the source set changed substantially. Use `--links links.txt` if the user provided a list of URLs.
Persistent URL sources live in `knowledge/link_sources/*.txt`. They are materialized into local markdown files in `knowledge/agent_memory/sources/` and then ingested automatically.

4. Open `CURRENT_CODEX_TASK.md`, `SEO_ARTICLE_RULES.md`, the visual prompt guide, and the generated `output/codex_tasks/<run_id>/TASK.md`.

5. For each article, read its prompt and evidence JSON, then write the final markdown article yourself to `output/articles/<run_id>/`.

6. Run review:

```powershell
python -m article_factory review output\runs\<run_id>.json
```

7. Fix every review issue before finishing.

8. Memory and the audited graph bootstrap are exported by `prepare`; rerun manually if you changed sources after preparing:

```powershell
python -m article_factory ai-memory export
python -m article_factory graph bootstrap
```

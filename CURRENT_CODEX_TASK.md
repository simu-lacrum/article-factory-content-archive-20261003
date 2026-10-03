# Current Codex Article Task

This project is Codex-first. Do not call an external LLM API. Codex writes the articles itself.

## User Spec

Write fresh Russian SEO articles for gaming product research. Avoid duplicates. Article 1: читы Dota 2 — evaluate feature scope and evidence. Article 2: читы на Дедлок — evaluate page claims and support. Use two image slots and FAQs.

## Main Task File

[TASK.md](C:\Users\User\Desktop\articles\output\codex_tasks\20261002-155808-591496\TASK.md)

## Output

- Articles directory: `C:\Users\User\Desktop\articles\output\articles\20261002-155808-591496`
- Manifest: `C:\Users\User\Desktop\articles\output\runs\20261002-155808-591496.json`
- Article index: `C:\Users\User\Desktop\articles\output\codex_tasks\20261002-155808-591496\ARTICLE_INDEX.md`

## Required Finish Check

Run `python -m article_factory review output\runs\20261002-155808-591496.json` and fix every issue.

## Memory

- ai-memory export: `C:\Users\User\Desktop\articles\memory\ai-memory-export`
- graph JSON: `C:\Users\User\Desktop\articles\memory\graph\knowledge-graph.json`
- graph Mermaid: `C:\Users\User\Desktop\articles\memory\graph\knowledge-graph.mmd`
- full graph traversal: nodes `5407/5407`, edges `5458/5458`
- mandatory session report: `C:\Users\User\Desktop\articles\memory\graph\SESSION_BOOTSTRAP.md`

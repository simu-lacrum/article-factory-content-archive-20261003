# Codex Instructions for Article Factory

This project is Codex-first. Do not require OpenAI API, Ollama, or any external LLM provider to write articles. Codex is the writer.

## Mandatory Session Memory Bootstrap

This section applies to **every new Codex dialog in this workspace**, including article work, research, code changes, maintenance, and follow-up tasks. It must run before planning or taking task actions.

1. From the project root, run:

```powershell
python -m article_factory graph bootstrap
```

2. Require `status: PASS`, node coverage `100%`, and edge coverage `100%`. The command deterministically traverses every connected component, every node (including isolated nodes), and validates every edge. Reading a random subset, only the Mermaid file, or only search results does not satisfy this requirement.
3. Read `memory/graph/SESSION_BOOTSTRAP.md` completely.
4. Read every file listed under `Required reading` completely. This includes the canonical visual guide at `knowledge/agent_memory/rules/article-visual-prompt-guide.md`.
5. Do not continue if coverage is incomplete, a mandatory instruction node is absent, or a required file is missing. Fix the graph/bootstrap problem first.
6. Re-run the bootstrap after any change to graph facts, required instructions, or the source set.

For article and visual tasks, all image prompts must follow `article-editorial-poster-v1`; Nano Banana Pro / `gemini-3-pro-image` is the default target model. Number generated assets across the current run and alternate B/A (odd = warm narrative B, even = tactile industrial A); real screenshots do not consume an index. Every B prompt must actually attach two files from the persistent warm-story reference set, assign one as composition and one as render/palette/typography, and pass 4/5 fidelity. Use exact mapped colors: Cluster `#635FD5`, Melonity `#FF1469`; in A they are small 3–8% semantic accents, while in B they replace the dominant yellow/amber field and occupy roughly 35–70% of the frame. Every reference image must have an explicit role, and every final prompt must pass the guide's minimum contract and score at least 80/100.

## Goal

When the user asks for SEO articles, use the local Article Factory as memory, source retrieval, topic selection, evidence packing, and quality gate.

Mandatory article rules live in `SEO_ARTICLE_RULES.md`. Read that file before generating topic ideas, article briefs, or final article drafts.
Product mapping lives in `knowledge/agent_memory/products/product-map.md`. Use Melonity for Dota 2, and use cluster.center for Deadlock and CS2.

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

## Writing Rules

- Use only evidence-backed facts or mark uncertainty explicitly.
- Do not invent current patch, meta, prices, ban waves, anti-cheat status, product status, or guarantees.
- Keep product integration native, grounded, and limited to claims present in project memory, imported sources, user-provided specs, or freshly verified sources.
- Never expose internal provenance in final article bodies. Do not write "local sources", "local evidence", "evidence pack", "knowledge base", or similar wording to the reader. Use those inputs silently and write from expert experience.
- Product mapping is mandatory: Dota 2 -> Melonity; Deadlock -> cluster.center; CS2 -> cluster.center.
- Do not provide operational instructions for bypassing anti-cheat, evading detection, exploiting vulnerabilities, or implementing cheat features.
- Avoid generic AI filler. Use the evidence pack, semantic cluster, search intent, mistakes, examples, checklists, FAQ, and internal-link ideas.
- Do not use markdown tables in ideas, briefs, or final articles. Use bullet lists, numbered lists, and comparison lists.
- Match the imported Medium article style: direct, practical, conversational, lightly slangy, gamer-aware, and free from water, bureaucratic wording, corporate filler, or academic over-explaining.
- Use simple living language and light gamer slang where it sounds natural, but keep the article credible and useful.
- Keep volume normal and useful: enough to satisfy the search intent, but only the essential material unless the user explicitly asks for a longer piece.
- Every final article needs SEO front matter, a description up to 160 characters that contains the primary keyword, image placement notes, and a FAQ block at the end.
- Every generated-image slot must name Nano Banana Pro / `gemini-3-pro-image` unless the user selects another model, include its global generated index and alternating B/A branch, apply the exact mapped brand color (Cluster `#635FD5`; Melonity `#FF1469`) with the correct role—small 3–8% accent in A, dominant 35–70% field replacing yellow/amber in B—attach and name two warm-story references for every B asset, include the complete prompt contract, pass B-fidelity 4/5 when applicable, and pass the visual guide's 80/100 gate.
- If a topic is `restricted`, do not write operational how-to content. Write only high-level educational/risk-aware content or ask for safer topic selection.

## Publication Memory

After an article is published, add it:

```powershell
python -m article_factory published add --title "<TITLE>" --slug "<SLUG>" --game dota2 --language en --url "<URL>"
python -m article_factory ingest
```

This prevents duplicate topic selection in future runs.

For broader duplicate prevention, add patterns to `published/avoid_topics.txt`.

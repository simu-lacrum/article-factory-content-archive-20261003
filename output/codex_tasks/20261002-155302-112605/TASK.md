# Codex Article Task

You are Codex. Write the final articles yourself. Do not call OpenAI API, Ollama, or any external LLM provider.

## User Spec

Create 12 distinct SEO articles with images and exact search intent. Do not use Medium. Each article must have the primary key phrase in title, H1, description, and opening where natural, include relevant LSI, a practical checklist, a short FAQ, and 2 real image placement slots. No operational instructions for bypassing anti-cheat, evasion, exploitation, or cheat implementation. Use high-level, evidence-aware editorial framing. Prepare these exact article targets and languages: (1) Russian for MetaSkins root https://metaskins.gg/ with primary phrase скинченджер КС2, anchors скинченджер кс2 and скинченджер; (2) English for MetaSkins /en https://metaskins.gg/en with primary phrase skinchanger dota 2, anchors skinchanger dota 2 and skinchanger cs2; (3) Russian for cluster.center/ru/cs2 https://cluster.center/ru/cs2 with primary phrase читы кс2, anchors читы кс2 and приватный чит для кс2; (4) Russian for cluster.center/ru/deadlock https://cluster.center/ru/deadlock with primary phrase читы дедлок, anchors читы дедлок and приватный чит на дедлок; (5) Russian for cluster.center/ru https://cluster.center/ru with primary phrase читы для игр, anchors читы and читы для игр; (6) English for cluster.center/en/cs2 https://cluster.center/en/cs2 with primary phrase cheats for cs2, anchors cheats for cs2, cs2 hacks, private cheats cs2; (7) English for cluster.center/en/deadlock https://cluster.center/en/deadlock with primary phrase deadlock cheats, anchors deadlock cheats, deadlock hacks, private cheat for deadlock; (8) English for cluster.center/en https://cluster.center/en with primary phrase cheats for games, anchors cheats for games, cheats, hacks; (9) Russian for melonity.gg https://melonity.gg/ with primary phrase читы Dota 2, anchors читы для доты, читы дота 2, читы dota 2, чит на доту; (10) English for melonity.gg/en https://melonity.gg/en with primary phrase dota 2 cheats, anchors dota 2 cheats, dota 2 hack, cheats for dota 2, private dota 2 cheat; (11) English for melonity.gg/en/deadlock https://melonity.gg/en/deadlock with primary phrase cheats deadlock, anchor cheats deadlock; (12) Russian for melonity.gg/deadlock https://melonity.gg/deadlock with primary phrase читы на Дедлок, anchors читы на дедлок and чит deadlock. Map Dota 2 to Melonity and CS2/Deadlock to cluster.center; MetaSkins articles may discuss cosmetic terminology. Avoid direct duplicates of already published topics by choosing fresh angles such as evidence checklists, scope, terminology, update notes, and comparison criteria.

## Output Directory

`C:\Users\User\Desktop\articles\output\articles\20261002-155302-112605`

## Required Workflow

1. Run `python -m article_factory graph bootstrap`; require PASS and 100% node/edge coverage.
2. Read `memory/graph/SESSION_BOOTSTRAP.md` and every required file it lists, including `SEO_ARTICLE_RULES.md` and the full visual prompt guide.
3. Read `knowledge/agent_memory/products/product-map.md`.
4. For each item below, read the `prompt` and `evidence` files.
5. Write a complete article to the target output path.
6. Use only facts supported by the evidence pack or mark uncertainty explicitly.
7. Do not mention local sources, local evidence, evidence packs, or the knowledge base in the final article body. Use those inputs silently and write from an expert editorial voice.
8. Keep native product integration grounded and follow product mapping: Dota 2 -> Melonity; Deadlock/CS2 -> cluster.center.
9. Do not provide operational instructions for bypassing anti-cheat, evading detection, exploiting vulnerabilities, or implementing cheat features.
10. Do not use markdown tables. Use lists, numbered lists, and comparison lists.
11. Match the imported Medium style: direct, practical, conversational, lightly slangy, gamer-aware, no water, no bureaucratic wording, no academic filler.
12. Number generated assets across the run and alternate style branches: odd = B warm narrative, even = A tactile industrial; real screenshots do not consume an index.
13. Build every generated-image prompt with `article-editorial-poster-v1`, target Nano Banana Pro by default, and use the exact mapped color (Cluster #635FD5; Melonity #FF1469) with the correct branch role: small 3–8% accent in A, dominant 35–70% field replacing yellow/amber in B. Require a QA score of at least 80/100. Every B asset must actually attach two persistent warm-story reference files with explicit composition and render/palette/typography roles and pass 4/5 reference fidelity.
14. After writing all articles, run `python -m article_factory review output\runs\20261002-155302-112605.json`.
15. Fix every `fail` or `needs_review` finding before considering the task done.

## Articles

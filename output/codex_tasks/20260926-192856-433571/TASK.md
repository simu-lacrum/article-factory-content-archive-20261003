# Codex Article Task

You are Codex. Write the final articles yourself. Do not call OpenAI API, Ollama, or any external LLM provider.

## User Spec

Write 12 unique English Tier-2 editorial articles, one for each supplied source page in knowledge/link_sources/network-t2-deadlock-dota-20260926.txt. Cover six Deadlock targets and six Dota 2 targets, matching the target page intent exactly. Keep all articles high-level, evidence-led, risk-aware, non-operational: do not explain bypasses, evasion, exploit implementation, or cheat deployment. Use real images or GIFs from each source page, with SEO front matter, <=160 character primary-keyword descriptions, image placement notes, FAQ, and native product mapping: Deadlock -> cluster.center, Dota 2 -> Melonity. Build distinct Tier-2 angles suitable for syndication on hosted editorial blogs.

## Output Directory

`C:\Users\User\Desktop\articles\output\articles\20260926-192856-433571`

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
14. After writing all articles, run `python -m article_factory review output\runs\20260926-192856-433571.json`.
15. Fix every `fail` or `needs_review` finding before considering the task done.

## Articles

### 1. Deadlock sandbox commands: a task-based reference

- Game: `deadlock`
- Language: `en`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260926-192856-433571\01-deadlock-sandbox-commands-a-task-based-reference.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260926-192856-433571\01-deadlock-sandbox-commands-a-task-based-reference.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260926-192856-433571\01-deadlock-sandbox-commands-a-task-based-reference.md`

### 2. Is there a parry cheat in Deadlock? What auto-parry claims mean

- Game: `deadlock`
- Language: `en`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260926-192856-433571\02-is-there-a-parry-cheat-in-deadlock-what-auto-parry-claims-mean.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260926-192856-433571\02-is-there-a-parry-cheat-in-deadlock-what-auto-parry-claims-mean.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260926-192856-433571\02-is-there-a-parry-cheat-in-deadlock-what-auto-parry-claims-mean.md`

### 3. Deadlock soul aimbot, soul triggerbot and soul ESP: what changes?

- Game: `deadlock`
- Language: `en`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260926-192856-433571\03-deadlock-soul-aimbot-soul-triggerbot-and-soul-esp-what-changes.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260926-192856-433571\03-deadlock-soul-aimbot-soul-triggerbot-and-soul-esp-what-changes.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260926-192856-433571\03-deadlock-soul-aimbot-soul-triggerbot-and-soul-esp-what-changes.md`

### 4. Deadlock cheat comparisons: start with the feature you need to understand

- Game: `deadlock`
- Language: `en`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260926-192856-433571\04-deadlock-cheat-comparisons-start-with-the-feature-you-need-to-understand.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260926-192856-433571\04-deadlock-cheat-comparisons-start-with-the-feature-you-need-to-understand.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260926-192856-433571\04-deadlock-cheat-comparisons-start-with-the-feature-you-need-to-understand.md`

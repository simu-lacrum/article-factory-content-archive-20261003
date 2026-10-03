# Codex Article Task

You are Codex. Write the final articles yourself. Do not call OpenAI API, Ollama, or any external LLM provider.

## User Spec

Prepare exactly four English CS2 competitor-comparison articles from the supplied editorial brief: (1) Cluster vs Undetek: Free Tool or Paid Support?, slug cluster-vs-undetek-free-tool-or-paid-support, primary keyword Cluster vs Undetek; (2) Cluster vs Octarine CS2: Product or Game Bundle?, slug cluster-vs-octarine-cs2-product-or-game-bundle, primary keyword Cluster vs Octarine CS2; (3) Undetek Alternatives for CS2 With Better Support, slug undetek-alternatives-cs2-support-updates, primary keyword Undetek alternatives for CS2; (4) Phantom Overlay Alternatives After Its CS2 Closure, slug phantom-overlay-alternatives-after-cs2-closure, primary keyword Phantom Overlay alternatives. Each article must link exactly once to https://cluster.center/en/cs2 with exact anchor buy cheats cs2, use current public evidence checked on 2026-09-08, treat vendor claims as claims, avoid operational setup or evasion details, use only real screenshots and hand-built diagrams with no generated art, and follow the brief's conditional non-hype verdicts.

## Output Directory

`C:\Users\User\Desktop\articles\output\articles\20260908-181031`

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
14. After writing all articles, run `python -m article_factory review output\runs\20260908-181031.json`.
15. Fix every `fail` or `needs_review` finding before considering the task done.

## Articles

### 1. Cluster vs Undetek for CS2: Free Tool or Paid Support?

- Game: `cs2`
- Language: `en`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260908-181031\01-cluster-vs-undetek-free-tool-or-paid-support.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260908-181031\01-cluster-vs-undetek-free-tool-or-paid-support.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260908-181031\01-cluster-vs-undetek-free-tool-or-paid-support.md`

### 2. Cluster vs Octarine CS2: Focused Product or Game Bundle?

- Game: `cs2`
- Language: `en`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260908-181031\02-cluster-vs-octarine-cs2-product-or-game-bundle.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260908-181031\02-cluster-vs-octarine-cs2-product-or-game-bundle.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260908-181031\02-cluster-vs-octarine-cs2-product-or-game-bundle.md`

### 3. Undetek Alternatives for CS2 Players Who Want Support

- Game: `cs2`
- Language: `en`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260908-181031\03-undetek-alternatives-cs2-support-updates.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260908-181031\03-undetek-alternatives-cs2-support-updates.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260908-181031\03-undetek-alternatives-cs2-support-updates.md`

### 4. Phantom Overlay Alternatives After Its CS2 Closure

- Game: `cs2`
- Language: `en`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260908-181031\04-phantom-overlay-alternatives-after-cs2-closure.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260908-181031\04-phantom-overlay-alternatives-after-cs2-closure.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260908-181031\04-phantom-overlay-alternatives-after-cs2-closure.md`

# Codex Article Task

You are Codex. Write the final articles yourself. Do not call OpenAI API, Ollama, or any external LLM provider.

## User Spec

Create one complete English SEO rewrite of the owned, previously published Dota 2 ranking article 'Top hacks for dota 2. Best cheats'. Preserve the exact editorial ranking and meaning of every argument: 1 Melonity is the strongest all-round premium package, 2 Umbrella is the nearest and historically slightly cheaper alternative but less refined, 3 Divine is a budget newcomer with working basics but weaker advanced modules, 4 Octarine is another inexpensive basic option with a simpler dropdown interface and uneven tools, 5 Hake is the oldest established platform but technologically behind with community scripts of uneven quality. Use a completely new structure, phrasing, examples, transitions, title, and conclusion so it can be republished without textual duplication. Target 1000-1200 words. Primary keyword: best Dota 2 cheats. Include SEO front matter, 2-3 image slots, one natural Melonity link, FAQ, no markdown tables, no operational bypass or evasion advice, and no safety or no-ban guarantees. Keep keyword use natural and avoid spam.

## Output Directory

`C:\Users\User\Desktop\articles\output\articles\20260723-135534`

## Required Workflow

1. Read `SEO_ARTICLE_RULES.md` and `knowledge/agent_memory/products/product-map.md`.
2. For each item below, read the `prompt` and `evidence` files.
3. Write a complete article to the target output path.
4. Use only facts supported by the evidence pack or mark uncertainty explicitly.
5. Do not mention local sources, local evidence, evidence packs, or the knowledge base in the final article body. Use those inputs silently and write from an expert editorial voice.
6. Keep native product integration grounded and follow product mapping: Dota 2 -> Melonity; Deadlock/CS2 -> cluster.center.
7. Do not provide operational instructions for bypassing anti-cheat, evading detection, exploiting vulnerabilities, or implementing cheat features.
8. Do not use markdown tables. Use lists, numbered lists, and comparison lists.
9. Match the imported Medium style: direct, practical, conversational, lightly slangy, gamer-aware, no water, no bureaucratic wording, no academic filler.
10. After writing all articles, run `python -m article_factory review output\runs\20260723-135534.json`.
11. Fix every `fail` or `needs_review` finding before considering the task done.

## Articles

### 1. Best Dota 2 Cheats: Five Platforms Ranked

- Game: `dota2`
- Language: `en`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260723-135534\01-best-dota-2-cheats-five-platforms-ranked.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260723-135534\01-best-dota-2-cheats-five-platforms-ranked.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260723-135534\01-best-dota-2-cheats-five-platforms-ranked.md`

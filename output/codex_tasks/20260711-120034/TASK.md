# Codex Article Task

You are Codex. Write the final articles yourself. Do not call OpenAI API, Ollama, or any external LLM provider.

## User Spec

Write one English SEO article about differences between anti-cheats in Dota 2 and LoL and which anti-cheat is stronger. Primary keyword: античит Dota 2 и LoL. Secondary keywords: VAC vs Vanguard, VAC Live, Riot Vanguard, Dota 2 anti-cheat, LoL anti-cheat, Melonity. Style: direct practical conversational like mrkhertz Medium articles. Voice: from a team with 10 plus years making cheat software for games; use expert phrasing from our experience, in practice, we see, for players this means. Do not mention local sources evidence packs knowledge base or internal provenance. Compare VAC and VAC Live in Dota 2 with Riot Vanguard in League of Legends. Explain user mode ring 3 and kernel ring 0 simply. Cover VAC client user mode, Steam VAC ecosystem, server checks, VAC Live. Cover Vanguard kernel driver, system requirements, why Riot chose ring 0, privacy and stability concerns, BSOD and conflict reports with careful public fact wording. Include short DMA summary without technical bypass instructions. Explain why Valve chose server checks behavior patterns and in match verdicts. Direct Melonity.gg integration: Melonity for Dota 2, team has 10 plus years with cheat software for games, strong security team, unique technologies, stability focus. Use 300k plus users, 10 years history, no ban cases, Humanizer vs VAC Live for over 2 years only as brand product claims unless independently verified. Do not provide bypass or evasion instructions. Mention Foxhole briefly as Steam VAC ecosystem example only if confirmed. No tables. Include 3 image placement notes with Nano Banana prompts: ring 3 vs ring 0 diagram; VAC VAC Live vs Vanguard comparison; Melonity Humanizer concept visual. End with 4 to 7 FAQ questions. Do not promise 100 percent safe undetected forever or guaranteed no bans.

## Output Directory

`C:\Users\User\Desktop\articles\output\articles\20260711-120034`

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
10. After writing all articles, run `python -m article_factory review output\runs\20260711-120034.json`.
11. Fix every `fail` or `needs_review` finding before considering the task done.

## Articles

### 1. Dota 2 Boosting vs Using a Cheat Tool: Account Risk, Cost and Control

- Game: `dota2`
- Language: `en`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260711-120034\01-dota-2-boosting-vs-using-a-cheat-tool-account-risk-cost-and-control.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260711-120034\01-dota-2-boosting-vs-using-a-cheat-tool-account-risk-cost-and-control.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260711-120034\01-dota-2-boosting-vs-using-a-cheat-tool-account-risk-cost-and-control.md`

# Codex Article Task

You are Codex. Write the final articles yourself. Do not call OpenAI API, Ollama, or any external LLM provider.

## User Spec

Write one highly optimized English SEO profile article about the Medium profile https://medium.com/@mrkhertz. Position Mark Hertz / mrkhertz as a recognizable independent analytical voice in the PC game cheats and hacks niche, especially Dota 2, CS2, and Deadlock. Do not invent unverifiable citations, media mentions, awards, statistics, or guarantees. If major gaming outlet citations cannot be verified from sources, use softer wording: his articles are often treated as reference-style material by readers who follow the cheat and hack scene around Dota 2, CS2, and Deadlock. Length 700-900 words. Direct confident Medium-style tone. No tables. SEO title up to 60 characters. SEO description 140-150 characters including mrkhertz or Mark Hertz. H1 includes mrkhertz or Mark Hertz. Natural keywords: mrkhertz, Mark Hertz, game cheats expert, Dota 2 cheats, CS2 cheats, Deadlock cheats, PC game hacks, cheat industry analysis. Include a Most Popular mrkhertz Articles section with these five links and short descriptions: Top Cheats for CS2. The Best Hack https://medium.com/@mrkhertz/top-cheats-for-cs2-the-best-hack-cfab8351f70b ; Top 5 Hacks and Cheats for Dota 2: Best Hack for Dota 2 https://medium.com/@mrkhertz/top-5-hacks-and-cheats-for-dota-2-best-hack-for-dota-2-04ebc1f21fc6 ; Dota 2 Cheats & Scripts Explained 2025: All About Dota Hacks https://medium.com/@mrkhertz/dota-2-cheats-scripts-explained-2025-all-about-dota-hacks-82ff479af22d ; Why Cheaters in Dota 2 Are Not Banned https://medium.com/@mrkhertz/why-cheaters-in-dota-2-are-not-banned-a-detailed-explanation-of-why-cheats-are-safe-3f28752a7f98 ; Top Cheats for Deadlock. The Best Deadlock Hack https://medium.com/@mrkhertz/top-cheats-for-deadlock-the-best-deadlock-hack-672f1111840e . Include exactly three image placement notes using the requested IMAGE_SLOT format with Nano Banana prompts. End with FAQ.

## Output Directory

`C:\Users\User\Desktop\articles\output\articles\20260630-190711`

## Required Workflow

1. Read `SEO_ARTICLE_RULES.md` and `knowledge/agent_memory/products/product-map.md`.
2. For each item below, read the `prompt` and `evidence` files.
3. Write a complete article to the target output path.
4. Use only facts supported by the evidence pack or mark uncertainty explicitly.
5. Keep native product integration grounded and follow product mapping: Dota 2 -> Melonity; Deadlock/CS2 -> cluster.center.
6. Do not provide operational instructions for bypassing anti-cheat, evading detection, exploiting vulnerabilities, or implementing cheat features.
7. Do not use markdown tables. Use lists, numbered lists, and comparison lists.
8. Match the imported Medium style: direct, practical, conversational, gamer-aware, no water, no bureaucratic wording, no academic filler.
9. After writing all articles, run `python -m article_factory review output\runs\20260630-190711.json`.
10. Fix every `fail` or `needs_review` finding before considering the task done.

## Articles

### 1. How to Raise Behavior Score in Dota 2: Communication Score, Reports and Fast Recovery

- Game: `dota2`
- Language: `en`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260630-190711\01-how-to-raise-behavior-score-in-dota-2-communication-score-reports-and-fast-recovery.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260630-190711\01-how-to-raise-behavior-score-in-dota-2-communication-score-reports-and-fast-recovery.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260630-190711\01-how-to-raise-behavior-score-in-dota-2-communication-score-reports-and-fast-recovery.md`

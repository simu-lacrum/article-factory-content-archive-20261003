# Codex Article Task

You are Codex. Write the final articles yourself. Do not call OpenAI API, Ollama, or any external LLM provider.

## User Spec

Topic: How to Raise Behavior Score in Dota 2: Communication Score, Reports and Fast Recovery
Game: dota2
Language: en
Article count: 1
Target volume: 1800-2400 words
Audience: Dota 2 players with low or unstable Behavior Score / Communication Score who want practical, non-operational recovery advice before returning to ranked.
Required outline:
- What Behavior Score and Communication Score mean in Dota 2
- How to check your current score
- What actually lowers your score: abandons, reports, griefing, chat abuse
- How often Behavior Score updates
- Fast recovery plan: Turbo, mute, support picks, commends, no chat fights
- Why low Behavior Score feels like a hidden pool
- Where Melonity fits: fewer mechanical mistakes, better awareness, less tilt, cleaner execution
- Soft CTA: try Melonity free for 7 days before grinding ranked again
SEO requirements: title <= 60 characters, description <= 160 characters containing primary keyword, H2/H3 structure, FAQ with 4-7 questions, 2-5 image placement notes, internal-link suggestions, native Melonity integration with a clearly visible link.
Safety/factual limits: use local memory/evidence only for factual claims; do not invent patch/meta/prices/ban waves/anti-cheat status/current product guarantees; do not provide bypass, evasion, exploit, or cheat implementation instructions.

## Output Directory

`C:\Users\User\Desktop\articles\output\articles\20260622-183400`

## Required Workflow

1. For each item below, read the `prompt` and `evidence` files.
2. Write a complete article to the target output path.
3. Use only facts supported by the evidence pack or mark uncertainty explicitly.
4. Keep native Melonity integration grounded and avoid unsupported guarantees.
5. Do not provide operational instructions for bypassing anti-cheat, evading detection, exploiting vulnerabilities, or implementing cheat features.
6. After writing all articles, run `python -m article_factory review output\runs\20260622-183400.json`.
7. Fix every `fail` or `needs_review` finding before considering the task done.

## Articles

### 1. How to Raise Behavior Score in Dota 2: Communication Score, Reports and Fast Recovery

- Game: `dota2`
- Language: `en`
- Prompt: `C:\Users\User\Desktop\articles\output\prompts\20260622-183400\01-how-to-raise-behavior-score-in-dota-2-communication-score-reports-and-fast-recovery.md`
- Evidence: `C:\Users\User\Desktop\articles\output\evidence\20260622-183400\01-how-to-raise-behavior-score-in-dota-2-communication-score-reports-and-fast-recovery.json`
- Target: `C:\Users\User\Desktop\articles\output\articles\20260622-183400\01-how-to-raise-behavior-score-in-dota-2-communication-score-reports-and-fast-recovery.md`

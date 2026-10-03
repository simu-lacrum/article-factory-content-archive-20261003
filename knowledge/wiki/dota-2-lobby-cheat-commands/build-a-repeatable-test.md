---
source: knowledge/agent_memory/sources/dota2cheat-rewrite-2026-09/dota-2-lobby-cheat-commands.md
heading: "Build a repeatable test"
---

## Build a repeatable test

Change one variable at a time. For a damage test, fix the hero level, talent, items, target armor, and position. Use `-refresh`, repeat five times, and record the result. If you add a level, a neutral item, and a resistance effect at once, the number is not useful because you cannot tell which change mattered.

For a combo, start with normal cooldowns and one target. Test the order, interruption, movement, spell immunity, and manual cancellation. Unlimited resources can teach the order, but the final run should use ordinary timing. A sequence that only works after repeated refreshes may not transfer to a real game.

![Image 3: Dota 2 practice sequence in a controlled environment](https://dota2cheat.com/assets/dota2/dota2-0eb56c882cc68ef7e94b88ea.webp)

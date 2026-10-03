---
source: knowledge/agent_memory/sources/dota2cheat-rewrite-2026-09/write-dota-2-script.md
heading: "Build a five-step test loop"
---

## Build a five-step test loop

1.   Create the smallest addon or bot package that loads.
2.   Run it in a private local lobby with one hero and one scenario.
3.   Log the trigger, selected target, action, and reason for any skip.
4.   Test one normal case and several failure cases.
5.   Reset the lobby and repeat with the same inputs.

The [private-lobby command guide](https://dota2cheat.com/guides/dota-2-lobby-cheat-commands) can help create repeatable states. A test that only succeeds after unlimited mana, artificial cooldowns, or all vision is not a complete behavior test.

![Image 4: Dota 2 script test settings in a private demo](https://dota2cheat.com/assets/dota2/dota2-5fd8aca410d79dca16eb219b.webp)

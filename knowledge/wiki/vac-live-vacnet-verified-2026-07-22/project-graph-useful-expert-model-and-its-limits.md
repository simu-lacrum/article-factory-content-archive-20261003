---
source: knowledge/agent_memory/sources/vac-live-vacnet-verified-2026-07-22.md
heading: "Project graph: useful expert model and its limits"
---

## Project graph: useful expert model and its limits

The graph connects `VAC`, `VAC-Live / server checks`, and `Humanizer`. Its source articles describe a layered model:

- client-side checks can inspect the local game environment at a high level;
- server-side checks can evaluate data returned during play;
- possible behavioral signals may include action cadence, reaction time, sequences of mouse/keyboard commands, camera behavior, damage, gold, and other game-specific telemetry;
- a behavioral system can compare sequences and patterns rather than depend on one isolated signature.

This conceptual model is useful for explaining why server-side analysis scales with match volume and why CS2 and Dota 2 would require different feature engineering. However, Valve does not publish the exact signal list or thresholds. The graph's claims about millions of users, exact Dota signals, real-time Dota VAC Live operation, instant-ban conditions, current compute needs, and ways to disguise automated behavior are not independently verified.

Allowed use in final articles:

- present the client/server/behavioral layers as a high-level expert model;
- say that command cadence, reaction timing, camera changes, and game-state trajectories are plausible signal categories, not a confirmed Valve checklist;
- use the graph to explain why MOBA telemetry differs from FPS telemetry;
- attribute non-public interpretations to the linked industry source and label them as expert analysis.

Do not use:

- operational evasion or bypass instructions;
- exact delay, jitter, click, injection, memory-access, obfuscation, or Humanizer settings;
- instructions for checking whether another player has allegedly been flagged;
- claims that a product is undetectable, bypasses VAC Live, guarantees safety, or has no bans;
- claims that VACNET currently watches a named Dota metric unless a primary source is added;
- the 2018 CPU figures as current 2026 infrastructure.

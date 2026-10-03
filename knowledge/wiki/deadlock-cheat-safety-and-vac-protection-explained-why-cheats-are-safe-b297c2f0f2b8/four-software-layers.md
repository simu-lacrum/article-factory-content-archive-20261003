---
source: knowledge/agent_memory/sources/target-urls/deadlock-cheat-safety-and-vac-protection-explained-why-cheats-are-safe-b297c2f0f2b8.md
heading: "Four software layers"
---

### Four software layers

To understand why this matters, it helps to separate anti-cheats by the level where they operate.

At the basic user-mode level, an anti-cheat watches the game process, checks files, looks for known signatures, and verifies that the client behaves normally. VAC belongs mostly to this category, although Valve also combines it with server-side systems.

At the server level, the game can analyze what the player sends during a match: movement, inputs, aim behavior, reaction timing, damage, target switching, and other gameplay signals. This is extremely important in Valve games because even if something is hidden on the client, the server still receives the result of the player’s actions.

At the behavioral-analysis level, systems can compare player behavior against what real players usually do. If someone reacts too perfectly, aims too mechanically, switches targets too fast, or repeats actions with robotic timing, that pattern can become suspicious.

At the kernel or early-boot level, anti-cheats like Vanguard sit much deeper in the operating system. They can see more, but they also create more privacy and compatibility concerns.

VAC is not Vanguard. It is not supposed to be. Valve’s approach is built around a wider system: client checks, server checks, and behavior analysis.

![Image 4: OSI anti-cheat stack diagram showing VAC as user-mode and server-side detection, while Vanguard, EAC, BattlEye, FACEIT, RICOCHET and EA Javelin are placed on deeper kernel-level layers.](https://cheatsgaming.com/media/medium/39dcdc185381a1e3d9e7ab79.jpg)

OSI anti-cheat stack diagram

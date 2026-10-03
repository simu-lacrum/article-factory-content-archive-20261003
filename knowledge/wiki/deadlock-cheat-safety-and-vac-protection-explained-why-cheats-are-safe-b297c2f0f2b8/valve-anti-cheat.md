---
source: knowledge/agent_memory/sources/target-urls/deadlock-cheat-safety-and-vac-protection-explained-why-cheats-are-safe-b297c2f0f2b8.md
heading: "Valve Anti-Cheat"
---

### Valve Anti-Cheat

VAC is not the same type of anti-cheat as Vanguard. It does not operate as an early-boot kernel anti-cheat that loads before Windows and controls the system from the deepest level. VAC works mostly at the user software level and through Valve’s own game and server ecosystem.

This is an important difference. Because of the level where VAC operates, it is limited in what it can directly observe on a computer. For example, it is not built like kernel anti-cheats that can deeply inspect drivers, low-level system behavior, or everything running below normal user-mode software.

Most anti-cheats in games work closer to this regular software level. The exception is aggressive kernel-level protection such as Vanguard, which is known for running much deeper in the system.

That does not automatically mean VAC is weak. It means Valve chose a different model. Instead of putting a heavy anti-cheat driver into every user’s system, Valve relies on a combination of client checks, server-side checks, delayed detection, and behavior analysis.

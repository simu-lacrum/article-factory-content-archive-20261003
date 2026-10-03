---
source: knowledge/agent_memory/sources/vac-live-vacnet-verified-2026-07-22.md
heading: "Core terminology"
---

## Core terminology

- Steam Support describes VAC as an automated system that detects identifiable cheats installed on a user's computer. VAC bans are permanent; an erroneous ban is removed automatically. This is the safe general definition of classic VAC.
- Valve's 2018 GDC talk used the name `VacNet` for a deep-learning system trained to identify cheating behavior from game data without adding client-side instrumentation.
- Valve's 6 June 2023 CS2 Limited Test notes documented a `live ban`: VAC could ban during a match and gracefully terminate it at the end of the round. The notes described the sanction and match-handling behavior, not a complete technical architecture.
- Valve's 19 August 2024 CS2 notes documented limited testing of `VacNet 3.0` on a subset of matches and provided a feedback address for incorrectly cancelled matches.
- Reporting after the 7 May 2026 CS2 update found that client strings changed the visible name from `VAC Live` to `VACNET` and that match chat began identifying the sanctioned player. Valve's public 7 May patch notes did not document this anti-cheat change.
- Therefore, `VAC`, `VacNet/VACNET`, and `VAC Live` should not be treated as three interchangeable names. A safe explanatory model is: VAC is the broader anti-cheat ecosystem; VacNet/VACNET is the behavioral-analysis lineage/name; VAC Live describes the in-match verdict and cancellation experience. The last sentence is an editorial inference from Valve's public terminology, not an architecture disclosure by Valve.

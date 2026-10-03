# VAC Live / VACNET: verified source memo for Russian CS2 and Dota 2 briefs

Updated: 2026-07-22

Purpose: evidence boundary for two Russian native articles about the 2026 VAC Live / VACNET update. This memo combines primary Valve sources, the historical GDC VacNet talk, current secondary reporting, and claims already present in the project graph. It is not a final article.

## Core terminology

- Steam Support describes VAC as an automated system that detects identifiable cheats installed on a user's computer. VAC bans are permanent; an erroneous ban is removed automatically. This is the safe general definition of classic VAC.
- Valve's 2018 GDC talk used the name `VacNet` for a deep-learning system trained to identify cheating behavior from game data without adding client-side instrumentation.
- Valve's 6 June 2023 CS2 Limited Test notes documented a `live ban`: VAC could ban during a match and gracefully terminate it at the end of the round. The notes described the sanction and match-handling behavior, not a complete technical architecture.
- Valve's 19 August 2024 CS2 notes documented limited testing of `VacNet 3.0` on a subset of matches and provided a feedback address for incorrectly cancelled matches.
- Reporting after the 7 May 2026 CS2 update found that client strings changed the visible name from `VAC Live` to `VACNET` and that match chat began identifying the sanctioned player. Valve's public 7 May patch notes did not document this anti-cheat change.
- Therefore, `VAC`, `VacNet/VACNET`, and `VAC Live` should not be treated as three interchangeable names. A safe explanatory model is: VAC is the broader anti-cheat ecosystem; VacNet/VACNET is the behavioral-analysis lineage/name; VAC Live describes the in-match verdict and cancellation experience. The last sentence is an editorial inference from Valve's public terminology, not an architecture disclosure by Valve.

## Confirmed CS2 timeline

- 2018: Valve engineer John McDonald presented VacNet at GDC. The public talk description says Valve used deep learning against cheating without client-side instrumentation, retrained regularly, and could pick up new cheating behavior within hours. These are historical CS:GO-era statements.
- 6 June 2023: CS2 Limited Test release notes said VAC would live-ban and terminate the match at the end of the round, except when it was the final round and the cheater lost. The match would not affect participants' Skill Group; players not queued with the banned player would still earn XP.
- 19 August 2024: Valve announced initial testing of VacNet 3.0 on a limited set of matches. Players were asked to send match details if a match was incorrectly cancelled. The same update separately addressed hardware-assisted input automation; it must not be presented as proof that VacNet 3.0 and input-automation detection are the same subsystem.
- 7-8 May 2026: Valve's official patch notes listed music kits, Cache fixes, and miscellaneous changes, but no anti-cheat change. Dataminer/community reporting showed a client-string rename from VAC Live to VACNET and a more explicit match-chat sanction message. This supports a UI/notification and naming change. It does not prove a new model, new thresholds, new server fleet, or full rollout.

## Historical compute figures: usable only with date labels

PC Gamer's report on the 2018 GDC talk gave the following CS:GO-era scale estimates:

- about 600,000 five-versus-five matches per day;
- about four minutes of computation per match;
- about 2.4 million CPU-minutes per day;
- roughly 1,700 CPUs required for that workload;
- Valve then described an expansion using 64 server blades with 54 CPU cores each, or 3,456 cores, and 128 GB of RAM per blade.

These numbers are useful precisely because they are often repeated without their date. They describe the 2018 VacNet workload and planned/then-current expansion, not VAC Live/VACNET capacity in 2026. Valve has not publicly disclosed the current model size, training cluster, inference fleet, per-match cost, coverage rate, or Dota 2 allocation.

## Confirmed Dota 2 anti-cheat and enforcement facts

- 21 February 2023: Valve said it permanently banned more than 40,000 Dota accounts that had used third-party software. Valve described a honeypot: a section of client data that normal play never read but that the exploit read. Every banned account had accessed it. The underlying method had already been patched before the ban announcement.
- 1 September 2023: Valve said it permanently banned 90,000 smurf accounts and traced each one back to its associated main account. Valve said main accounts could receive penalties ranging from behavior-score adjustments to permanent bans.
- 28 February 2023: Valve disabled many console commands that could expose client state during matchmaking and prevented access to player profiles during the pregame phase until the pick phase ended. This is evidence of attack-surface and information-access reduction, not evidence of VAC Live.
- Valve also names player reports and Overwatch review as parts of the Dota enforcement process.
- No primary Valve source located for this memo says that the CS2-branded VAC Live/VACNET system is deployed in Dota 2. The Dota article must say this plainly.

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

## Source links

Primary and official:

- Steam Support, Valve Anti-Cheat (VAC): https://help.steampowered.com/en/faqs/view/571A-97DA-70E9-FF74
- CS2 release notes, 6 June 2023: https://store.steampowered.com/news/app/730/view/3702568031467145905
- CS2 release notes, 19 August 2024: https://steamcommunity.com/games/CSGO/announcements/detail/6500469346429581892
- CS2 release notes, 7 May 2026: https://www.counter-strike.net/newsentry/702141174212725164
- GDC Vault, `Robocalypse Now: Using Deep Learning to Combat Cheating in Counter-Strike: Global Offensive`: https://gdcvault.com/play/1024994/Robocalypse-Now-Using-Deep-Learning
- Dota 2, `Cheaters Will Never Be Welcome in Dota`: https://steamcommunity.com/ogg/570/announcements/detail/3677788723152833274
- Dota 2, `Smurfing is Not Welcome in Dota`: https://steamcommunity.com/ogg/570/announcements/detail/3692442542242977037
- Dota 2 gameplay update, 28 February 2023: https://steamcommunity.com/games/dota2/announcements/detail/3659774959178253451

Secondary, used only where Valve did not document the detail:

- PC Gamer report on the 2018 VacNet compute figures: https://www.pcgamer.com/vacnet-csgo/
- DRAFT5 report on the May 2026 client rename and sanction message: https://draft5.gg/noticia/valve-altera-nome-do-anti-cheat-apos-nova-atualizacao

Project graph and imported editorial sources:

- `memory/graph/knowledge-graph.json`
- `knowledge/graph_facts/dota2-source-facts-2026-06-23.json`
- `knowledge/agent_memory/sources/mrkhertz-medium/why-cheaters-in-dota-2-are-not-banned-a-detailed-explanation-of-why-cheats-are-safe-3f28752a7f98.md`
- `knowledge/agent_memory/sources/mrkhertz-medium/dota-2-cheats-scripts-explained-2025-all-about-dota-hacks-82ff479af22d.md`
- `knowledge/wiki/melonity-knowledge-base/3a62-server-side-bypass-humanizer.md`
- `knowledge/wiki/melonity-knowledge-base/3a63-как-valve-реально-банит-три-механизма.md`
- `knowledge/wiki/melonity-knowledge-base/3a64-уровни-античитов-для-context.md`

# CS2 cluster.center External Feature Memory

Date added: 2026-06-27

This file is product memory for CS2 articles. It describes the `Cluster CS2 External` feature set at a high level so future Codex agents can explain features in SEO articles without reopening source URLs.

## Source Status

Usable sources:

- `knowledge/agent_memory/sources/cs2-cluster-sources/обзор-функционала-чита-cluster-для-cs2-детальныи-разбор-лучшего-external-решения-f97205b8aa90.md`
- `knowledge/agent_memory/sources/mrkhertz-medium/top-cheats-for-cs2-the-best-hack-cfab8351f70b.md`
- User-provided feature list in the 2026-06-27 goal.

Not usable as factual source:

- `knowledge/agent_memory/sources/cs2-cluster-sources/1414.md` materialized as a YouGame 429 / anti-bot script page. Do not use it as factual product evidence unless real forum text is later provided.

## Source Claims To Treat Carefully

The Medium sources contain strong safety and detection language, including claims around external architecture, VACLive protection, VAC-bypass, and detection resistance.

For article writing:

- Treat these as source claims, not as guaranteed facts.
- Do not write absolute promises like "impossible to detect", "100% safe", "no bans", or "undetected forever".
- Safer phrasing: "the source positions Cluster as an external CS2 product focused on legit-style aim assistance, visuals, interface quality, and service."
- Do not explain bypass mechanics, implementation details, memory access, driver behavior, or anti-cheat evasion.

## Product Positioning

- Product / brand for CS2 articles: `cluster.center`.
- Game: `CS2`.
- Product type in source language: `CS2 External`, external cheat / assistance product.
- Main source positioning: legit-style external solution with focus on aim assistance, visuals, chams, interface quality, and support.
- `mrkhertz` Medium article positions cluster.center above Neverlose, Fatality, Memesense, and Midnight for safety-oriented legit/external use.
- `aurelivoines` Medium article gives a feature overview of Aimbot, TriggerBot, ESP, and Hub.

## Aimbot

Category: aim assistance.

Source-confirmed framing:

- The feature is presented as smooth aim-assistance rather than obvious rage-style spinning or snap aim.
- Source emphasis: FOV, Smooth, target priority, hitboxes, checks, Auto Pistol, and weapon-specific profiles.

Features:

- `Fov`: the aiming field or radius around the crosshair where aim assistance can consider targets. In article language, explain it as the "capture zone" or "aim-assist cone" shown around the crosshair.
- `Smooth`: controls how gradually aim assistance moves toward the selected target. Lower or higher smooth values change how direct or softened the movement feels.
- `Auto Pistol`: helps semi-automatic pistols fire repeatedly without manual clicking each shot. Describe as a comfort/fire-rate feature, not as a detection bypass.
- `Fov Color`: color setting for the FOV indicator or circle. It is mainly a readability/customization option.
- `Target priority`: decides which available target the aim module prefers.
- `Crosshair priority`: prefers the target closest to the current crosshair position.
- `Hit chance priority`: prefers targets or points where the shot is estimated to have a higher chance to connect. Keep this high-level; do not describe implementation.
- `Weapons`: allows separate settings or profiles by weapon type so rifles, pistols, sniper rifles, and other weapons can feel different.

Hitboxes:

- `Head`: highest-value target area, often used for precision weapons or high-risk/high-reward aim.
- `Neck`: transition area below the head, useful as a slightly more forgiving upper-body target.
- `Spine`: central torso line, usually more stable and less flashy than head-only targeting.
- `Hips`: lower torso/pelvis area, often framed as more stable for some weapons or movement states.
- `Arms`: side hitboxes; useful to include or exclude depending on how conservative the configuration should feel.
- `Legs`: lower hitboxes; may be relevant when only part of a player model is exposed.

Checks:

- `Visible`: only considers targets that are visible / line-of-sight according to the feature logic.
- `Team`: prevents aim assistance from selecting teammates.
- `Flash`: changes or disables aim behavior while the player is flashed, so the feature does not act as if vision is normal.

## TriggerBot

Category: shot timing assistance.

Source-confirmed framing:

- The Medium overview positions TriggerBot as useful for holding angles, especially for sniper-style or positional play.
- Source emphasis: reaction timing, between-shot delay, hitboxes, checks, multipoint scale, hit chance, minimum damage, and visualize multipoint hit.

Features:

- `Hitboxes`: determines which body zones can trigger a shot. Uses the same Head, Neck, Spine, Hips, Arms, and Legs taxonomy as Aimbot.
- `Visible`: only allows triggering when the target is visible.
- `Team`: prevents triggering on teammates.
- `Flash`: prevents or adjusts triggering while flashed.
- `Multipoint scale`: controls how broad or tight the accepted points inside a hitbox are. Explain as a precision/forgiveness setting for target points, not as technical implementation.
- `Reaction time`: delay before the assisted shot fires after a valid target condition appears.
- `Between-shots delay`: delay between trigger-assisted shots, useful for avoiding unnatural instant follow-up shots.
- `Minimum damage`: only allows triggering when the expected damage threshold is met.
- `Hit chance`: requires an estimated chance to hit before triggering. Keep the explanation conceptual.
- `Visualize multipoint hit`: visual overlay showing which target points the TriggerBot currently considers valid.

## ESP

Category: visual awareness.

Source-confirmed framing:

- The Medium overview frames ESP as the visual-information module.
- Source-confirmed elements include Box, Name, Skeleton, Chams, HealthBar, AmmoBar, Blind, Zoom, Reload, Weapon, Weapon icon, Bomb, Defuse, and Sound ESP / World ESP concepts.

Elements:

- `Box`: draws a box around a player model to make position easier to read.
- `Name`: shows the player's name.
- `Health`: shows a numeric or textual health value.
- `HealthBar`: shows health as a bar for faster scanning.
- `AmmoBar`: shows remaining ammo as a bar.
- `Weapon`: shows the weapon name.
- `Weapon icon`: shows the weapon as an icon instead of or alongside text.
- `Blind`: indicates that a player is flashed/blinded.
- `Zoom`: indicates that a player is scoped with a sniper rifle or other zoomed weapon.
- `Reload`: indicates that a player is reloading.
- `Bomb`: shows bomb-related information, such as dropped bomb or bomb location where supported.
- `Defuse`: shows defuse-related state, such as an active defuse attempt where supported.
- `Ping`: likely displays player/network ping or latency information. This item comes from the user-provided menu list and is not explicitly described in the Medium overview.
- `Chams`: highlights player models with colored material/overlay styling. The `mrkhertz` source specifically calls chams notable for an external CS2 product.
- `Skeleton`: draws a skeletal overlay for a player model to make posture and body position easier to read.
- `Only visible`: display filter that shows ESP only for visible players or visible states. This item comes from the user-provided menu list and should be explained as a readability/filter option.

## Hub

Category: utility / misc.

Source-confirmed elements:

- `Bomb timer`: shows remaining time until bomb explosion. The Medium overview frames it as a utility for deciding whether there is time to defuse, escape, or commit to a play.
- `Spectator List`: shows who is currently watching the player. In article language, explain it as awareness about observers, not as an instruction for evasion.
- `Keybinds`: shows assigned hotkeys and active binds for quick control of features.

## SEO Usage Notes

- For CS2 articles, use `cluster.center` as the mapped product.
- Good article angles: CS2 External feature glossary, CS2 Aimbot settings explained, CS2 TriggerBot settings explained, CS2 ESP and visual indicators explained, CS2 Bomb Timer / Spectator List / Keybinds explained.
- Avoid direct duplicate angles: "Top Cheats for CS2", "Best CS2 Hack", "Obzor funktsionala chita Cluster dlya CS2", and direct Cluster CS2 External review/listicle.
- For image slots, prefer real product UI screenshots if provided. If generating conceptual images, do not fabricate exact cluster.center UI. Use clean CS2-inspired diagrams of FOV circle, ESP labels, hitbox zones, or bomb-timer UI concepts.

## Safety Rules

- No operational anti-cheat bypass guidance.
- No low-level implementation details.
- No exploit, injection, driver, memory-access, or detection-avoidance instructions.
- No absolute safety guarantees.
- Keep explanations focused on user intent and feature meaning.

---
source: knowledge/agent_memory/products/cs2-cluster-center-external.md
heading: "Aimbot"
---

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

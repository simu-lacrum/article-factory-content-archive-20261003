---
title: "Deadlock Projectile Aim: Travel Time, Lead and Cover"
description: "Deadlock projectile aim explained through travel time, lead, elevation and cover—plus why one rule cannot fit every weapon."
game: deadlock
language: en
primary_keyword: "Deadlock projectile aim"
secondary_keywords: ["Deadlock aim prediction", "projectile travel time", "target lead", "vertical aim", "Deadlock cover"]
slug: "deadlock-projectile-aim-travel-time-lead-cover"
risk_level: restricted
visuals: none
---

# Deadlock Projectile Aim: Travel Time, Lead and Cover

An enemy cuts diagonally across a short passage. Your crosshair is centered on the model when you fire, yet the projectile sails behind them. With a slow projectile, being perfectly on target can be the reason the shot misses: the target is already leaving the point you aimed at.

That is the core of Deadlock projectile aim. The shot has to meet a moving target in three-dimensional space after spending time in flight. Distance, movement direction, elevation, and the way a player exits cover all change that meeting point. A single rule such as “aim ahead” is too blunt to explain every weapon or every fight.

## Being on target is not the same as arriving on target

The crosshair shows a direction at the moment of input. A projectile hit depends on where the target and projectile are when their paths finally cross. Those are related ideas, but they are not interchangeable.

Think of two snapshots:

- The first is the target’s visible position when the shot starts.
- The second is the point the target may occupy when the projectile arrives.

Against a stationary opponent, the two points can overlap. Against someone moving sideways, they separate. The longer the flight lasts, the more room there is for that separation to grow.

This is also why a clean-looking crosshair recording does not settle the question. The frame can show accurate placement on the model while saying nothing about travel time or the target’s next step. “I was on him” describes the first snapshot, not the interception.

## Travel time turns distance into a moving problem

Distance matters because it changes how long the world can change after the projectile leaves. A small amount of lateral movement may be irrelevant at close range and decisive farther away. The screen-space lead can look similar in both cases while representing very different arrival timing.

Imagine the same opponent running across your view in two situations. At close range, the projectile needs only a short trip, so the target does not travel far before impact. At a longer range, the same movement speed creates a larger gap between the visible model and the useful meeting point.

This does not mean “farther always equals much more lead.” Projectile speed, the opponent’s direction, and the remaining line of sight all matter. A fast shot at long range may demand less anticipation than a slower shot from closer in. Distance is a multiplier on timing, not a complete answer by itself.

The practical reading is simple: identify whether the weapon behaves like an immediate line or a visible traveler. Then judge the shot by arrival, not by how satisfying the crosshair looked at release.

## Lateral movement needs lead; closing movement needs restraint

Sideways movement creates the clearest lead problem because the target is leaving the line of fire. If the opponent keeps the same direction and speed, the meeting point sits ahead of the visible model. The exact amount changes with distance and projectile behavior, but the relationship is easy to see.

Movement toward or away from you behaves differently. A target running almost straight at you produces less sideways separation on screen. Adding the same horizontal lead used for a strafing target can manufacture a miss that was never necessary.

Diagonal movement combines both cases. Part of the motion changes range; another part crosses the line. That is why fixed screen-space habits break down. They treat every target as if it were moving across a flat poster.

Direction can also change between release and arrival. A player who sees the firing cue may stop, reverse, dash, or use cover. Prediction is therefore an estimate based on a readable movement state, not knowledge of the next input. The less stable the movement, the less confidence any projected meeting point deserves.

## Elevation changes the line, not just the screen position

Deadlock fights are not played on a flat lane diagram. Stairs, rooftops, slopes, drops, and jumps alter the path in depth as well as height. A target rising on stairs is not merely moving upward on your monitor; the three-dimensional meeting line is changing.

This becomes obvious when a projectile clips the lip of a platform or passes under a jumping target. The visible model may occupy the expected horizontal position, yet the path is blocked or vertically misaligned. A useful mental model has to include the route through space, not just a two-dimensional offset.

Three common elevation mistakes are worth separating:

- Treating a slope like flat ground and leading only sideways.
- Tracking the center of a jumping model without considering the projectile’s arrival height.
- Ignoring nearby geometry because the target itself remains visible.

The last one is especially sneaky. Visibility of the model does not mean the whole projectile route is clear. A railing, ledge, or corner can matter for the path even when the player looks exposed.

## Cover creates an exit window, not a clean prediction

When someone disappears behind a wall, it is tempting to place the crosshair just beyond the edge and assume they will continue. Sometimes they do. Sometimes they stop, reverse, or change pace while hidden.

That makes a cover exit a window of possibilities rather than one reliable point. The longer the target is occluded, the more uncertain the old movement becomes. A brief pass behind a thin post preserves more information than a full second behind a building.

Good reasoning separates three moments:

1. The last confirmed movement before cover.
2. The earliest plausible reappearance.
3. The direction and speed actually shown on exit.

Firing at the first possible exit can catch a committed runner, but it also commits to the weakest information. Waiting for the reappearance improves certainty while giving up some time. That tradeoff is the real cover problem.

## Why one aim profile cannot describe every weapon

Weapons that differ in projectile speed, range, cadence, and role do not create the same interception problem. A profile that feels sensible for a fast, direct shot can lag behind a slower projectile. A rule tuned around distant lateral movement can overlead close targets or opponents closing the gap.

Cadence changes the lesson too. With a single deliberate shot, the first meeting point carries most of the weight. With repeated projectiles, the player may correct after observing misses, but target movement can also change between shots. Treating the entire sequence as one frozen calculation hides that feedback loop.

This is where feature language can become misleading. “Projectile prediction” sounds complete, but the label does not tell you:

- Which weapon behaviors it is meant to cover.
- Whether elevation and obstruction are part of the description.
- How uncertainty is shown when movement changes.
- Whether different target types are treated separately.

Those questions matter more than the label count on a feature page.

## What a feature comparison should clarify

A useful comparison should describe scope before making a quality claim. Does the page distinguish fast and slow projectiles? Does it explain whether the concept applies to players, creeps, or other targets? Does it separate a stable lateral run from a cover exit?

That is also the right way to read cluster.center or any other Deadlock product page: as a list of stated capabilities that still needs context. A broader [Deadlock cheat feature comparison](https://medium.com/@aurelivoines/top-4-cheats-for-deadlock-comparison-of-features-prices-and-the-best-software-choice-0f737d360121) can show which products claim projectile-oriented aim tools, but the label still needs to be read against weapon type and match context.

Before taking a prediction claim seriously, ask for plain answers to four questions:

- What kind of projectile is being discussed?
- What movement state is assumed?
- How are elevation and cover handled at a conceptual level?
- What happens when the information is uncertain or stale?

If those answers are missing, the feature name is marketing shorthand, not a full explanation of behavior.

The best question is not “does it have prediction?” It is “for which flight behavior and situation is that prediction actually described?”

## FAQ

### What is projectile lead in Deadlock?

Projectile lead means aiming toward a future meeting point rather than only at the target’s current visible position. The useful amount depends on travel time, distance, movement direction, and the path through the environment.

### Does more distance always require more lead?

Not by itself. Greater distance usually gives the target more time to move, but projectile speed and movement direction can outweigh distance. A fast projectile at range may need less anticipation than a slow one closer in.

### Why does elevation affect projectile aim?

Elevation changes the three-dimensional path between shooter and target. Stairs, jumps, ledges, and slopes can move the meeting point or put geometry in the route even when the target looks centered on screen.

### Can projectile prediction account for cover?

It can describe a likely exit based on the last visible movement, but cover adds uncertainty. The hidden player may stop, reverse, or change pace, so an exit point should be treated as a possibility rather than a known destination.

### Can a prediction feature make every shot land?

No feature label can remove spread, obstruction, sudden movement changes, or incomplete information. The honest way to judge the claim is by its stated weapon scope, assumptions, and failure cases.

---
memory_type: "external_source"
source_url: "https://dota2cheat.com/guides/dota-2-lobby-cheat-commands"
source_list: "knowledge/link_sources/dota2cheat-rewrite-2026-09.txt"
imported_at: "2026-09-25T20:31:37"
fetch_method: "jina_reader"
do_not_duplicate_topic: false
tags:
  - "external_source"
  - "local_agent_memory"
---

# Dota 2 Lobby Cheat Commands for Private Practice

> This page is a local markdown copy for agent memory. Future Codex agents should read this file instead of fetching the source URL during article work.

Source URL: https://dota2cheat.com/guides/dota-2-lobby-cheat-commands

Title: Dota 2 Lobby Cheat Commands for Private Practice

URL Source: https://dota2cheat.com/guides/dota-2-lobby-cheat-commands

Published Time: 2026-02-19T00:00:00Z

Markdown Content:
![Image 1: Dota 2 private lobby practice interface](https://dota2cheat.com/assets/dota2/dota2-8f9db8f2e6a3545d547aacfd.webp)

**Dota 2 lobby cheat commands are built-in practice controls, not a matchmaking cheat.** In a custom lobby where the host enables cheats, they can set up gold, levels, items, cooldowns, heroes, vision, and repeatable tests in seconds. They do not carry into ordinary matchmaking, and they are not a reason to install an external loader.

Command names and permissions can change with a client update. If a command is rejected, use the game's autocomplete and check the current client instead of downloading a replacement executable.

![Image 2: Dota 2 private lobby practice interface](https://dota2cheat.com/assets/dota2/dota2-8f9db8f2e6a3545d547aacfd.webp)

## Set up a controlled lobby

1.   Open **Play**, create a custom lobby, and choose a local host when the client offers that option.
2.   Enable the lobby's **cheats** setting before starting.
3.   Add bots or a friend only when the drill needs another unit.
4.   Start the game, open chat, and enter one command at a time.
5.   Write down the hero, patch, items, levels, and target state so the test can be repeated.

Keep this environment private and consensual. Never test commands in a public match or try to turn a lobby option into a third-party information advantage.

## Useful command families

| Command | Use in a private lobby |
| --- | --- |
| `-gold 5000` | Add a controlled amount of player gold for an item timing test. |
| `-lvlup 5` | Increase the selected hero's level without replaying early waves. |
| `-item item_blink` | Create an item by its internal name; use autocomplete when names differ. |
| `-refresh` | Restore health, mana, and cooldowns before the next repetition. |
| `-respawn` | Respawn the controlled hero after a failed or lethal test. |
| `-createhero npc_dota_hero_axe enemy` | Spawn a named practice target; verify the internal name in autocomplete. |
| `-allvision` / `-normalvision` | Compare a known vision state, then return to ordinary visibility. |
| `-spawncreeps` | Generate a wave when testing lane timing or area damage. |

These are commonly documented private-lobby commands, not a promise that every spelling remains enabled. The Valve Developer Community Workshop Tools documentation explains the supported custom-content environment, while the official Dota 2 update history is the right place to check for client changes.

## Build a repeatable test

Change one variable at a time. For a damage test, fix the hero level, talent, items, target armor, and position. Use `-refresh`, repeat five times, and record the result. If you add a level, a neutral item, and a resistance effect at once, the number is not useful because you cannot tell which change mattered.

For a combo, start with normal cooldowns and one target. Test the order, interruption, movement, spell immunity, and manual cancellation. Unlimited resources can teach the order, but the final run should use ordinary timing. A sequence that only works after repeated refreshes may not transfer to a real game.

![Image 3: Dota 2 practice sequence in a controlled environment](https://dota2cheat.com/assets/dota2/dota2-0eb56c882cc68ef7e94b88ea.webp)

## Vision, lanes, and target drills

Use `-allvision` only to inspect a known map state, then restore `-normalvision`. For ward practice, place the ward, move the target through high and low ground, and note the edge of vision. For lane work, spawn a wave, keep the normal camera, and compare last hits across several attempts.

Do not confuse this with a maphack. A host-controlled lobby exposes a deliberate test state; matchmaking is expected to hide information from players. Our [detection guide](https://dota2cheat.com/guides/dota-2-cheat-detection) explains why external access to hidden client data has different account consequences.

![Image 4: How hacks work in Dota 2 interface screenshot](https://dota2cheat.com/assets/dota2/dota2-329284f6d2b6b690e3ba0951.webp)

## Save a drill that another player can repeat

Write the starting hero, level, items, target, map position, command sequence, and expected observation in one short note. Re-run the same sequence after a Dota patch and mark the date. If a command stops working, remove it from the note rather than substituting an unverified executable. This keeps the drill useful for learning instead of turning it into a collection of stale forum snippets.

Use the [script taxonomy guide](https://dota2cheat.com/guides/dota-2-scripts-guide) when a desired action needs code rather than a one-off lobby command. A supported bot or custom game has a documented boundary; a public-match loader does not.

## Finish and reset the session

*   Run the final repetition with normal cooldowns, mana, and visibility.
*   Disable any temporary lobby settings before creating another game.
*   Save the drill name with the hero and patch, then discard it after a rework.
*   Never move a command or external script into public matchmaking.

For supported development rather than manual commands, follow our [Dota 2 Workshop scripting flow](https://dota2cheat.com/guides/write-dota-2-script). For account and conduct boundaries, read the [smurf-ban guide](https://dota2cheat.com/guides/dota-2-smurf-ban-guide). Private practice is useful precisely because its scope is explicit.

Found an outdated claim or broken source? [Send a correction request](https://dota2cheat.com/corrections).

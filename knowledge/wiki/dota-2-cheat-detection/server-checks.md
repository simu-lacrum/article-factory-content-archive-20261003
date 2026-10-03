---
source: knowledge/agent_memory/sources/network-t2-deadlock-dota-20260926/dota-2-cheat-detection.md
heading: "Server checks"
---

#### Server checks

Server checks are VAC modules that are loaded onto Valve’s official servers and check the data returned by players in real time to detect suspicious activity on the part of players.

It’s not hard to imagine what data Valve checks: speed, net worth, damage, mouse and keyboard commands.

The entire VACnet is based on these server checks, which are trained on data from millions of users and have a rough idea of what a person is capable of in terms of reaction time, button press speed, etc. Obviously, there are some conditional constants, for example, a person cannot fire an entire magazine in CS2 in one second, so when VAC sees such data from a player on the server, it instantly bans them.

Overall, such a system is a brilliant, technically complex solution that can compensate for the shortcomings of user-mode anti-cheats. It is worth noting that, as with any neural network, hallucinations can occur or false positives can happen, so they approach this with caution.

However, there are also brilliant engineers working on cheats like Melonity who have been able to get around this.

> _By the way, if you’d like to try cheats for CS2, Deadlock, or other games available on Steam without worrying about your account, I recommend this__cheat store for CS2, Deadlock, and other games__. I personally vouch for it._

---
source: knowledge/agent_memory/sources/mrkhertz-medium/maphack-for-dota-2-everything-you-need-to-know-how-to-download-it-a5126f8bc05f.md
heading: "2. Incomplete map hack (present day)"
---

### 2. Incomplete map hack (present day)

As I mentioned earlier, Valve stopped storing player position data on their servers, so it became impossible to retrieve it. However, map hacking is one of the most crucial features of a cheat, so cheat developers weren’t going to let that slide.

Dota cheat developers came up with a partial map hack implementation. The developers at Melonity were the first to create this and [add it to their cheat](https://melonity.gg/en) so you cam try maphack in it.

The method involves using indirect information about the enemy to display their position such as placing a ward, accidentally entering the line of sight of an ally or an ally’s ward, or using an ability.

This is precisely why the current map hack implementation is called “partial,” since it essentially provides an approximate enemy position. 

In Melonity, an icon appears at the location where the enemy was, along with the amount of time since they were last there. As soon as the map hack receives updated data on the enemy’s position, it removes the previous icon and creates a new one.

![Image 3](https://miro.medium.com/v2/resize:fit:302/0*aDG8WPw-Db1EhUhC.png)

MapHack indicator

Currently, this method is used everywhere where map hacks are present.

It’s far from certain that Valve specifically decided to cut off this functionality for cheaters; most likely, the decision to stop collecting data on players’ coordinates in-game was made to optimize server capacity usage. Around this time, Valve began actively implementing server-side checks and the much-maligned VAC-Live, which requires massive computing power. By the way, I wrote a separate article about VAC-Live and how modern Dota cheats, such as Melonity, deal with it; I highly recommend it to any player interested in the game and cheats — [link](https://medium.com/@mrkhertz/dota-2-cheats-scripts-explained-2025-all-about-dota-hacks-82ff479af22d).

That’s all for now. Thanks for reading. If you have any ideas for my next article, I invite you to leave a comment below.

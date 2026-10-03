---
source: knowledge/agent_memory/sources/network-t2-deadlock-dota-20260926/dota-2-cheat-detection.md
heading: "How does it work?"
---

#### How does it work?

Himanizer is an extremely complex system of mathematical algorithms that were created after a thorough analysis of all Valve checks (the developers’ capabilities in terms of the data collected were also analyzed, so all potential detection vectors are implemented in them), but if I try to simplify it for the average person to understand, I would try to describe it using the simplest examples of how it works.

Let’s take mouse orders as a basis. Scripts, such as those that control illusions, constantly click and control each illusion separately. For the server, this may seem strange, because a person clicks on the map and switches between illusions in a fraction of a second, and also manages to control the hero. To do this, the humanizer creates micro-delays in keystrokes, clicks on random places, and performs the actions that ordinary people perform (very similar to how vac live works, right?). In this way, the server is fooled, and what can we say, sometimes even to the human eye, such gameplay looks normal.

![Image 8: Humanizer working with a mouse movement](https://dota2cheat.com/assets/dota2/dota2-4089b23118af2faf2e7d8e0b.webp)

Humanizer working with a mouse movement

However, there is also a camera in Dota that displays an image with a fixed field of view on the screen. Its position is fixed to the player and always follows them, but in Dota, the entire map is always rendered at once, and the camera position can be changed using the aforementioned Camera Hack.

The camera position is also sent to the server, so it is quite a difficult task to make it think that the value is within the normal range when you can see the entire map in front of you at once, but the humanizer does it perfectly.

![Image 9: Why cheaters in Dota 2 are not banned: a detailed explanation of why cheats are safe — image 8](https://dota2cheat.com/assets/dota2/dota2-bf6a945f657e3e1527d354c3.webp)

This video clearly shows how himanizer interacts with the camera and mouse commands, hiding them from the server.

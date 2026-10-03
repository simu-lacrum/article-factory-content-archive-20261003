---
source: melonity-knowledge-base.md
heading: "3A.6.4. Уровни античитов — для context"
---

#### 3A.6.4. Уровни античитов — для context

Чтобы пользователь понимал почему VAC «слабее» некоторых других:

| Анти-чит | Уровень | Игры | Уязвимости |
| --- | --- | --- | --- |
| **VAC** | User-mode (Ring 3) | CS2, Dota 2, TF2 | Не видит kernel-level cheats; wave-based bans |
| **EAC** (Easy Anti-Cheat) | Kernel + user | Apex, Fortnite, Rust | Видит почти всё; обходится только DMA/external |
| **BattlEye** | Kernel | PUBG, R6, Tarkov | Сильный, но обходится |
| **Vanguard** | Ring-0 + early boot | Valorant | Самый жёсткий — загружается до Windows; у Dota нет аналога |
| **FACEIT AC** | Kernel | CS2 (FACEIT) | Обходится только DMA |
| **VACnet** | Server ML | CS2 (только) | Behavioral analysis — ловит даже undetected cheats |
| **Ricochet** | Kernel + ML | Call of Duty | Server-side ML |

> **Контентный edge:** Для Dota 2 Valve **сознательно не делает kernel anti-cheat** (как Vanguard). Причины: privacy concerns (kernel anti-cheat имеет полный доступ к ПК пользователя — фотки, документы), кросс-платформенность (Linux/Mac), стабильность с��стемы. Vanguard известен конфликтами с другими anti-cheats; VAC — нет.

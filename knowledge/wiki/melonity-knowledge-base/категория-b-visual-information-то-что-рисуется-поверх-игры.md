---
source: melonity-knowledge-base.md
heading: "Категория B: Visual / Information (то, что рисуется поверх игры)"
---

#### Категория B: Visual / Information (то, что рисуется поверх игры)

Это **самая популярная категория среди новичков** — не «играет за тебя», а просто показывает информацию. Самая безопасная с точки зрения VAC-Live (см. 3A.7), потому что не отдаёт команды на сервер.

##### B.1. Visualizing player events (события на карте)

| Скрипт | Что делает | Польза |
| --- | --- | --- |
| **Visible by Enemy (VBE)** | Анимация-индикатор когда твой герой в зоне видимости врага (включая True Sight через Sentry/Gem) | Знаешь, когда тебя видят → можешь избежать ганка / wards / Track |
| **Show Hidden Spells** | Подсвечивает Sun Strike (Invoker), Light Strike Array (Lina), Blast Off (Techies), Sacred Arrow (Mirana), Torrent (Kunkka), Charge of Darkness (Spirit Breaker) — все «невидимые» абилки | Главная защита от глобальных скиллов; уворачиваешься заранее |
| **Show Illusions** | Помечает оригинал героя (Phantom Lancer, Naga, Manta) | Не тратишь damage на иллюзии в teamfight'ах |
| **AOE Radius Display** | Радиусы скиллов и предметов (Black Hole, Reverse Polarity, Echo Slam) | Точный позиционный edge |
| **Manabars ESP** | Показывает ману всех врагов | Знаешь когда у Lina нет маны на стан → атакуешь |
| **Cooldown ESP** | Видишь CD каждого скилла врагов | Идёшь на врага именно когда ult в downtime |
| **Show Dropped Items** | Все дропы на карте (включая в фоге) | Не теряешь Gem'�� и ва��ные предметы |
| **Killable Indicator** | Иконка над врагом, когда у тебя достаточно урона/маны на kill | Никогда не упускаешь дайв за неубиваемым врагом |

##### B.2. Continuous information (HUD overlay)

| Скрипт | Что показывает | Польза |
| --- | --- | --- |
| **Roshan Timer** | Точное время респа Roshan-а (не только текстовый) | Контроль самого важного объекта на карте |
| **Rune Timer** | До респа bounty/water/wisdom рун | Стабильное преимущество в фарме |
| **Tormentor / Lotus Pool indicator** | Респ tormentor-ов и лотосов | Тимплеи на ключевых объектах |
| **Camp status** | Какие camps под контролем врага (с stack/free) | Где farm, где не идти |
| **Net worth panel** | Точный нетворс всех 10 героев | Понимаешь power balance в каждый момент |
| **MetaPicker / Build Helper** (Melonity-эксклюзив) | На основе DotaBuff анализирует draft и предлагает best pick + build | Помощь в pick phase для новичков |

##### B.3. Skin Changer / Inventory Changer

Технически отдельный модуль, визуально классифицируется как visual. **Не «открывает скины» — а локально подменяет item ID** в твоём инвентаре. На сервере у тебя обычные предметы, в твоём клиенте — premium skins.

**Что включает:**
- Все скины всех героев (включая Arcana, Persona, Immortal items)
- Все ландшафты карты (Diretide, Spring Cleaning, Reef's Edge, Low Poly map от Melonity)
- Курсор-паки, weather effects, sound packs
- Dota+ функции (chat wheel расширение, hero stats screen)

**Современная имплементация (Melonity 2026):** репликация механики применения официальных скино�� Valve — **FPS не падает**, в отличие от старых имплементаций.

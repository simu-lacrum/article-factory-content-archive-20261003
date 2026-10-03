---
source: melonity-knowledge-base.md
heading: "Категория A: Hero Scripts (Auto-Combo, Auto-Cast)"
---

#### Категория A: Hero Scripts (Auto-Combo, Auto-Cast)

Самая ценная категория — автоматизация механически сложных герое��. Превращает hard-skill heroes в простые пики.

##### Топ-10 героев, для которых hero scripts критичны:

| Герой | Что автоматизирует скрипт | Почему важен |
| --- | --- | --- |
| **Invoker** | Авто-инвок Sun Strike (E+E+E+R), Cold Snap (Q+Q+W+R), Tornado→EMP→Meteor→Deafening Blast wombo combo, переключение Quas/Wex/Exort | Самый mechanically complex hero в игре; авто-комбо позволяет beginner играть на уровне 5K MMR |
| **Arc Warden** | Spark Wraith spam в правильные точки, контроль Tempest Double для фарма, синхронные касты на оригинале и клоне | Управление 2 героями одновременно вручную почти невозможно |
| **Pudge** | Auto Hook с предсказанием движения цели, Auto Rot, авто-Dismember на низком HP врага | Hook — самая viral-способность в Dota; auto-prediction делает skillshot 95% попаданий |
| **Skywrath Mage** | Auto-cast Concussive Shot + Ancient Seal + Mystic Flare combo, kill steal с ультой | #1 герой среди читеров по статистике GOSU.AI |
| **Storm Spirit** | Авто-расчёт траектории Ball Lightning, идеальные кэтчи врагов | Ball Lightning требует точного расчёта ман�� и ра��ст��яния — скрипт делает это мгновенно |
| **Tinker** | Авто-Rearm, Soul Ring + Boots of Travel + Blink rotation | Бесконечный спам способностей с идеальным таймингом |
| **Techies** | Идеальная установка мин по choke points, авто-Blast Off с правильным HP-итемизацией | Полностью использует setup-потенциал героя |
| **Morphling** | Авто-Morph под нужный stat (HP/Agility), Replicate с правильным таймингом | Слишком много расчётов вручную |
| **Meepo** | Контроль 5 копий одновременно, авто-Poof в одну точку | Управление 5 героями = humanly almost impossible |
| **Nature's Prophet** | Глобальный Sprout с предсказанием движения, Teleportation в идеальные точки фарма | Globальная мобильность + кастомизация фарма |
| **Huskar** | Armlet abuse (флип�� Armlet д��я регена) — делает героя «бессмертным» | Armlet toggle на правильном HP — практически невозможно вручную |

**Что делает Auto-Combo алгоритмически:**

1. Определяет цель (наводка курсора + враг с лучшим kill-potential).
2. Считает damage всех скиллов и предметов в инвентаре.
3. Сравнивает с HP цели + magic resist + статусные эффекты.
4. Если kill confirmed → запускает последовательность нажатий с `microdelays` (10-50 мс между кастами).
5. Использует Humanizer (см. 3A.7) — добавляет случайные движения мыши и микродрожание, чтобы выглядеть как человек.

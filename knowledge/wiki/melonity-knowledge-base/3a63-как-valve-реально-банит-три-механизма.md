---
source: melonity-knowledge-base.md
heading: "3A.6.3. Как Valve реально банит — три механизма"
---

#### 3A.6.3. Как Valve реально банит — три механизма

Только один механизм даёт «мгновенный бан» — остальные работают волнами или через коммьюнити-репорты.

| Механизм | Срабатывание | Обходится через |
| --- | --- | --- |
| **VAC signature match** | Если в памяти найдена сигнатура известного чита — instant ban | Manual mapping + obfuscation + ежедневные обновления |
| **VAC-Live (server-side)** | Real-time проверки — большинство случаев = wave ban через 1-4 недели | Humanizer |
| **Overwatch (community-led)** | Игроки репортят, опытные модераторы смотрят replay → ban | Humanizer (replay должен выглядеть legit) + не быть слишком очевидным в публичных играх |
| **HWID-ban** | После повторного нарушения — ban привязывается к hardware | HWID Spoofer |
| **VACnet (neural network)** | ML-модель находит статистические аномалии — wave ban | Behavioral baseline matching в Humanizer |

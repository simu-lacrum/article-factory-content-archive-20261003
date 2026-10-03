---
source: melonity-knowledge-base.md
heading: "3A.6.2. Server-side bypass — Humanizer"
---

#### 3A.6.2. Server-side bypass — Humanizer

**Humanizer** — самая важная и сложная технология. Это набор математических алгоритмов, имитирующих **поведение настоящего игрока**, чтобы серверные проверки VAC не обнаруживали «нечеловеческую» активность.

**Что VAC-Live проверяет на сервере:**
- Скорость и pattern движений мыши (camera position deltas)
- Скорость и pattern нажатий клавиш
- Reaction times (реакция между событием и кастом)
- Click coordinates (идеальные клики ровно по центру целей = подозрительно)
- Camera position vs unit position (если камера всё время «смотрит» через fog of war = MapHack)
- Action patterns (если каждый combo идеально таймингован = bot-pattern)
- Net worth / damage / gold trajectories (сравнение с baseline своего MMR)

**Как Humanizer обходит:**

1. **Microdelays** — между кастами скр��птом добавляется случайная задержка 10-80 мс, имитирующая человеческую реакцию.
2. **Mouse jitter** — даже при идеальном клике курсор «дрожит» на ±2-5 пикселей вокруг центра.
3. **Camera lock** — камера, передаваемая на сервер, привязана к герою (как у обычного игрока), хотя локально ты видишь Camera Hack-зум.
4. **Random additional clicks** — иногда добавляются «лишние» клики по карте, как настоящий игрок (мисс-клики).
5. **Action queue smoothing** — если скрипт хочет нажать 6 кнопок за 100 мс, Humanizer растягивает их на 250-400 мс с jitter.
6. **Behavioral baseline matching** — анализирует «обычный» уровень игры на текущем MMR и не позволяет статам выходить за этот baseline (нет 100/0/100 на Crusader-2).

**Важный факт для FAQ:** **Humanizer не делает чит «инвизом»** — он делает гейплей **статистически нормальным**, чтобы neural network VACnet не флагнула паттерн.

---
source: melonity-knowledge-base.md
heading: "3A.5. Particle ESP — родственник MapHack"
---

### 3A.5. Particle ESP — родственник MapHack

Технически отдельный feature, но связан. **Как это работает:**

Сервер всегда отправляет клиентам **particle effects** (всполохи скиллов, blood splashes от атак, эффект�� предметов) — даже когд�� они в fog of war, потому что без этого нельзя корректно отображать игру при выходе из тумана.

Particle ESP включает рендер ВСЕХ particles, в том числе:
- Sunstrike (Invoker) — уже видишь куда летит за 1.7 сек
- Чужие телепорты (TP particles)
- Skill casts (Lina stun, Pudge Hook trail)
- Smoke of Deceit (видишь когда враги под смоком)
- Blood splash от атак на крипов леса
- Anti-Mage Blink particle, Storm's Ball Lightning trail

**Польза:** косвенный MapHack + раннее предупреждение глобальных скиллов.

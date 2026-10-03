---
source: knowledge/agent_memory/rules/article-visual-prompt-guide.md
heading: "11.3. Real screenshot — доказательство"
---

### 11.3. Real screenshot — доказательство

Показывает фактический интерфейс или событие. Генеративная модель может создать только нейтральную рамку/фон, но не должна менять содержимое скриншота. В промпте явно писать: «keep every pixel of the screenshot content unchanged; only extend the outer background».

Real screenshot не получает `generated_sequence_index` и не влияет на A/B-чередование. Если модель генерирует только внешнюю рамку вокруг неизмененного скриншота, ветка назначается рамке как обычному generated asset, но содержимое screenshot остается фактическим и неизменным.

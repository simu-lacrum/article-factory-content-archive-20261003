---
source: knowledge/agent_memory/rules/article-visual-prompt-guide.md
heading: "6. Специфика Nano Banana Pro"
---

## 6. Специфика Nano Banana Pro

Основная целевая модель — Nano Banana Pro, официальное имя модели в Gemini API: `gemini-3-pro-image`. Это reasoning-driven модель для сложного графического дизайна, профессиональных ассетов, локальных правок, бренд-консистентности и точной работы с текстом. Она принимает текст и изображения, поддерживает thinking, Search grounding, многошаговое редактирование и изображения до 4K.

Официальные проектные ориентиры на дату обновления этого гайда:

- Nano Banana Pro поддерживает 1K, 2K и 4K.
- Поддерживаемые пропорции Pro: `1:1`, `2:3`, `3:2`, `3:4`, `4:3`, `4:5`, `5:4`, `9:16`, `16:9`, `21:9`.
- В API размер задается как `1K`, `2K` или `4K` — с заглавной `K`.
- Для Pro допускается до шести объектных референсов высокой точности, до пяти референсов людей для сохранения идентичности и до трех style references. Лимиты могут различаться по пользовательским поверхностям, поэтому перед серийной генерацией нужно проверить конкретный интерфейс.
- Модель умеет рендерить разборчивый многоязычный текст лучше предыдущих поколений, но финальная орфографическая проверка все равно обязательна.
- Все созданные Google изображения получают SynthID; это учитывать при политике публикации и прозрачности.

Официальные источники для повторной проверки возможностей:

- [Gemini API: image generation](https://ai.google.dev/gemini-api/docs/image-generation)
- [Gemini 3 Pro Image model](https://ai.google.dev/gemini-api/docs/models/gemini-3-pro-image)
- [Google: 7 tips for Nano Banana Pro](https://blog.google/products-and-platforms/products/gemini/prompting-tips-nano-banana-pro/)

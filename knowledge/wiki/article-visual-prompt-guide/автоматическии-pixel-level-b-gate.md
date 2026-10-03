---
source: knowledge/agent_memory/rules/article-visual-prompt-guide.md
heading: "Автоматический pixel-level B gate"
---

### Автоматический pixel-level B gate

После генерации ветки B и до ручной проверки 4/5 запустить:

```powershell
python -m article_factory visual-fidelity "<CANDIDATE_IMAGE>" --accent "#635FD5"
```

Для Melonity заменить accent на `#FF1469`. Аргумент сохранен под именем `--accent` для обратной совместимости, но в B он означает доминирующий brand field. Команда сравнивает результат со всеми восемью постоянными warm-story references по насыщенности, световому характеру, доле темной массы и присутствию теплых вторичных объектов, одновременно проверяя, что mapped-цвет действительно заменил желто-янтарное поле и занимает примерно 25–75% пикселей с учетом света и теней. Порог — 75/100 без автоматических flags. Это не заменяет ручную проверку layout, shape language, depth и typography mass; она идет следующим шагом.

---
source: SEO_ARTICLE_RULES.md
heading: "Image Placement Notes"
---

## Image Placement Notes

Every article must include image placement notes directly in the markdown. Do not attach images silently.

Use this exact format:

```markdown
<!-- IMAGE_SLOT_01
Placement: after "## Section Heading"
Type: real screenshot | product UI | gameplay screenshot | generated image | diagram
Purpose: what the image should help the reader understand
Suggested file name: dota-2-example-topic-01.webp
Alt text: concise SEO-friendly alt text
Caption: optional caption for the article
If generated, Nano Banana prompt:
Write the full prompt here. Keep text readable, avoid fake UI labels unless needed.
Generated sequence index: 1, 2, 3...
Style branch: A | B1 | B2 | B3
Mapped product and brand color role: Cluster #635FD5 | Melonity #FF1469 | none; A = small semantic accent, B = dominant field replacing yellow/amber
Model: Nano Banana Pro / gemini-3-pro-image
Aspect ratio and size: 16:9, 2K
Typography mode: art-first | text-in-image
Reference roles: Image A = composition; Image B = material; etc.
Visual style version: article-editorial-poster-v1
Prompt QA score: 0-100
-->
```

Rules:

- Use 2-5 image slots for normal articles.
- At least one image should support the main explanation, not just decorate the page.
- If an image should be a real screenshot, say exactly what screen/state/action it should show.
- If the image can be generated, include a ready-to-send Nano Banana prompt.
- Do not invent product screenshots that could misrepresent the UI. Use generated conceptual images only when a real screenshot is not required.
- Treat Nano Banana Pro / `gemini-3-pro-image` as the default generator unless the user explicitly selects a different model.
- Number generated conceptual images globally across the current article batch. Odd generated indices use branch B (`warm narrative editorial ad`, submode B1/B2/B3); even generated indices use branch A (`tactile industrial product poster`). This B-first order ensures that a one-cover article actually uses the new reference family. Real screenshots and verified product/game UI do not consume an index. Adjacent generated images may not repeat a branch.
- Compile every generated-image prompt through `knowledge/agent_memory/rules/article-visual-prompt-guide.md`. It must define the generated sequence index, style branch, asset role, factual article thesis, one physical visual metaphor, one hero, aspect ratio, composition, palette roles, mapped brand color role, materials, camera, lighting, typography mode, reference roles, constraints, priority order, and output size.
- Apply the exact mapped brand color by branch: Cluster / `cluster.center` uses `#635FD5` for Deadlock and CS2; Melonity uses `#FF1469` for Dota 2. In branch A keep it as one 3–8% semantic accent and never as a global wash. In branch B use it as the dominant 35–70% field that replaces the warm-story reference's yellow/amber background; do not leave yellow dominant or reduce the mapped color to a small token.
- Assign one explicit function to every attached reference (composition, material, palette, subject identity, lighting, or camera). Do not give the model an undifferentiated pile of references.
- For every branch-B asset, actually attach two files from `knowledge/agent_memory/references/article-editorial-warm-story-v1/`: one composition reference and one render/palette/typography reference. `Reference roles: none` is an automatic failure. Require at least 4/5 fidelity across layout silhouette, warm/light palette, rounded shape language, depth treatment, and typography mass.
- Prefer `art-first` for article covers: reserve a clean headline safe zone and prohibit letters, pseudo-text, labels, and logos. Use `text-in-image` only with exact quoted copy, language, case, line count, position, and a ban on all other text.
- Use 2K as the normal master size; use 4K for final hero assets, typography-heavy posters, print, or substantial downstream crops. Write the size with an uppercase `K`.
- Score every final prompt with the guide's 100-point rubric. A score below 80, or any automatic rejection condition, requires a rewrite before generation.
- Do not ask for a named brand's or living artist's style. Describe the abstract editorial product-poster properties instead.

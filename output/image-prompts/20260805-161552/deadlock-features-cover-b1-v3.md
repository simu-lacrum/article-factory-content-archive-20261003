---
id: deadlock-features-cover-b1-v3
model: Nano Banana Pro / gemini-3-pro-image
generated_sequence_index: 1
style_branch: B1
aspect_ratio: "16:9"
output_size: 2K
brand_color_role: "Cluster #635FD5 — dominant field replacing yellow/amber"
prompt_qa_score: 100
output_fidelity_status: PASS — automated 100/100, manual 5/5
---

# Deadlock Features Cover — Cluster Field Correction

Version 2 used the wrong color hierarchy. In branch B, Cluster violet is not a small tile accent: it replaces the large yellow field.

## Required uploads

1. `output/image-prompts/20260805-161552/deadlock-features-cover-b1-yellow-source.png`
   - Role: edit target.
   - Preserve: exact composition, character, pose, organizer, props, garden, lighting, camera, typography, copy and line breaks.
   - Change: only the large yellow background field.

2. `knowledge/agent_memory/references/article-editorial-warm-story-v1/reference-01.png`
   - Role: composition guardrail only.
   - Preserve from the active edit target; use this reference only to prevent drift from the headline-left / story-right silhouette.

3. `knowledge/agent_memory/references/article-editorial-warm-story-v1/reference-06.png`
   - Role: render and typography guardrail only.
   - Preserve the rounded warm 2.5D finish, clean masses and large grotesk typography; do not copy its panels, people, text or colors.

## Nano Banana Pro edit prompt

```text
Use Image 1 as the edit target. Make one local palette correction only.

Replace the entire large yellow background field behind the headline and character with exact Cluster violet #635FD5. The violet must become the dominant color field, covering the same area that is yellow in Image 1, approximately 50–65% of the visible frame. Preserve the existing soft light gradient, warm bounce and rounded shadow depth while keeping #635FD5 as the field's clear base hue. No yellow or amber may remain as the dominant background.

Keep everything else exactly unchanged: 16:9 crop, camera, character identity and pose, face, clothing, hands, orange three-compartment organizer, all five tiles including the violet tile in the hands, plants, wooden wall, lighting direction, shadows, material finish and scene depth.

Preserve the headline exactly as shown: "DEADLOCK FEATURES, SORTED" in English uppercase, three lines, heavy dark geometric grotesk, same spelling, comma, size, position and line breaks. Render it exactly once. Do not add any other text, logo, symbol or watermark.

Image 2 is a composition guardrail only: retain the headline-left / narrative-scene-right silhouette and three depth planes. Image 3 is a render and typography guardrail only: retain the warm rounded 2.5D finish, clean large masses and strong typography mass. Do not copy objects, people, source wording, logos, colors or exact layouts from Images 2 or 3.

Do not redesign, move, add, remove or recolor any object other than the large yellow field. Do not introduce industrial machinery, metal chassis, rails, fasteners, UI, HUD, game characters, weapons, cyberpunk light or extra props.

If constraints conflict, prioritize: 1) changing the whole yellow field to #635FD5, 2) preserving every other part of Image 1, 3) exact headline and three-line layout, 4) original rounded lighting and depth.

Output: 2K, 16:9.
```

## Acceptance gate

- The old yellow field is now a Cluster-violet field centered on `#635FD5`.
- The mapped-color field occupies roughly 35–70% of the frame; a small purple tile alone is a failure.
- The headline remains verbatim, once, in the same three-line block.
- Character, organizer, props, camera and warm rounded render remain materially unchanged.
- Manual B fidelity passes at least 4/5 for layout silhouette, light/mapped-field palette, rounded shape language, depth treatment and typography mass.

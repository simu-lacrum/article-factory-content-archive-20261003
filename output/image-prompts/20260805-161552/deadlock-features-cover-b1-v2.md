---
id: deadlock-features-cover-b1-v2
model: Nano Banana Pro / gemini-3-pro-image
generated_sequence_index: 1
style_branch: B1
aspect_ratio: "16:9"
output_size: 2K
brand_accent: "Cluster #635FD5"
prompt_qa_score: 98
output_fidelity_status: rejected — mapped color incorrectly reduced to a small tile accent
---

# Deadlock Features Cover — Superseded B1 Prompt

This version is rejected because it keeps the yellow field and limits Cluster `#635FD5` to one small tile. Use `deadlock-features-cover-b1-v3.md` instead.

The previous industrial-deck prompt is rejected. Do not reuse it or use its generated result as a reference.

## Required uploads

1. `knowledge/agent_memory/references/article-editorial-warm-story-v1/reference-01.png`
   - Role: composition only.
   - Inherit: large upper/left headline mass, lower/right narrative scene, human-to-oversized-object scale relationship, three depth planes.
   - Do not copy: person, house, vegetable, wording, or exact layout.

2. `knowledge/agent_memory/references/article-editorial-warm-story-v1/reference-06.png`
   - Role: render and typography only.
   - Inherit: warm rounded 2.5D finish, heavy dark grotesk, clean large color fields, restrained grain.
   - Do not copy: people, message, cards, logo, colors, or exact panel geometry.

## Prompt

```text
Create a 16:9 2K warm narrative editorial cover for an English article titled "Deadlock Cheat Features Explained".

Model target: Nano Banana Pro / gemini-3-pro-image. Generated sequence index 1. Use article-editorial-poster-v1 branch B1 only; do not blend in branch A.

Editorial thesis: five familiar feature labels become useful only after they are grouped by the gameplay decision they affect.

Show one calm, friendly, non-identifiable adult guide in a sunlit stylized backyard workshop, placing five oversized unlabeled geometric tiles into one large rounded organizer with three broad compartments. The person, tiles and organizer must read as one simple narrative scene with one action—sorting—not as a technical machine.

Composition: reserve x=5–39% and y=10–48% for the exact two-line headline. Place the guide and organizer across x=42–96% and y=30–94%, with the organizer intentionally cropped by the lower edge. Add one soft out-of-focus leaf cluster in a bottom corner and simplified rounded shrubs behind the scene to create foreground, subject and background planes. The scene must remain readable at 240 px.

Render style: polished 2.5D/soft 3D editorial illustration with rounded forms, broad clean masses, matte clay-like surfaces, gentle ambient occlusion, restrained paper grain and no micro-detail.

Palette roles: a luminous warm yellow field around #F8CC38 should cover roughly 55–65% of the image. Use warm off-white for the five tiles, muted teal for foliage and one clothing area, and soft orange for the organizer. Use exact Cluster violet #635FD5 only on the single tile currently being placed, roughly 4% of the frame; no other purple and no violet lighting.

Lighting: golden summer daylight from upper left, soft bloom, rounded shadows and warm bounce, not studio product lighting.

Camera: near eye level with a slight low three-quarter view, natural 50 mm illustration feel, sharp subject plane and softly defocused foreground.

Typography: render exactly "DEADLOCK FEATURES, SORTED" in English uppercase, two lines, very large heavy geometric grotesk, dark warm charcoal #332922, left aligned inside the reserved area, occupying about 28–34% of the frame. Preserve every character and comma exactly. No other letters, numbers, labels, logos or pseudo-text anywhere.

Reference fidelity: Image A is the uploaded reference-01.png for composition only. Image B is the uploaded reference-06.png for render and typography mass only. Match at least four of five axes: layout silhouette, warm/light palette, rounded shape language, depth treatment and typography mass. Do not copy any source text, people, objects, branding or exact layout.

Hard exclusions: no industrial sorting deck, apparatus, metal chassis, rails, fasteners, concrete tabletop, dark product base, studio product photography, translucent lens, UI, game logo, Deadlock character, weapon, map, HUD, crosshair, hacker imagery, shield, padlock, cyberpunk lighting, fake feature labels or extra objects.

If constraints conflict, prioritize: 1) recognizable warm-reference composition and typography mass, 2) the one sorting action, 3) yellow daylight palette and rounded shape language, 4) exact headline, 5) exact small #635FD5 accent, 6) minor detail.

Output: 2K, 16:9.
```

## Output gate

Reject the result unless it matches at least four of these five reference axes:

- layout silhouette;
- warm/light palette;
- rounded shape language;
- foreground/subject/background depth;
- typography mass.

A mechanically correct sorting metaphor is not enough. Any dark industrial machine, concrete studio surface, metal chassis, missing headline, or `References: none` result is a failed branch-A drift.

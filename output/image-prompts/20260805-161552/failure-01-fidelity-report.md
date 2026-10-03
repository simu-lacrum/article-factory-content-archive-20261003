# Branch-B Fidelity Audit — Rejected Industrial Deck

Candidate: `C:/Users/User/.codex/attachments/da924f3c-d23e-4820-9a69-8dd8c36307d9/image-1.png`

Command:

```powershell
python -m article_factory visual-fidelity "C:\Users\User\.codex\attachments\da924f3c-d23e-4820-9a69-8dd8c36307d9\image-1.png" --accent "#635FD5"
```

Result: **FAIL — 37.0/100**, passing score 75.

## Measured mismatch

- Mean saturation: candidate `0.1698`; reference-set mean `0.6672`.
- Mean luminance: candidate `0.5504`; reference-set mean `0.7293`.
- Warm yellow/amber pixel ratio: candidate `0.0560`; reference-set mean `0.7603`.
- Dark pixel ratio: candidate `0.2515`; reference-set mean `0.0270`.
- Cluster `#635FD5` accent coverage: candidate `0.0009`, below the required practical floor of `0.01`.

Automatic flags:

- `too_desaturated_for_branch_b`;
- `too_dark_for_branch_b`;
- `warm_yellow_amber_field_missing`;
- `dark_industrial_mass_too_large`;
- `mapped_brand_accent_below_1_percent`.

The pixel audit confirms the visual diagnosis: this is a valid branch-A industrial render, not a close branch-B match. A future candidate must also pass the manual 4/5 comparison for layout silhouette, rounded shape language, depth treatment, and typography mass.

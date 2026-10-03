from __future__ import annotations

import colorsys
import math
from pathlib import Path
from statistics import mean
from typing import Any

from PIL import Image


DEFAULT_REFERENCE_DIR = Path(
    "knowledge/agent_memory/references/article-editorial-warm-story-v1"
)


def _hex_rgb(value: str) -> tuple[int, int, int]:
    clean = value.strip().lstrip("#")
    if len(clean) != 6:
        raise ValueError(f"Brand color must be a six-digit hex color, got: {value}")
    try:
        return tuple(int(clean[index : index + 2], 16) for index in (0, 2, 4))  # type: ignore[return-value]
    except ValueError as exc:
        raise ValueError(f"Brand color must be a six-digit hex color, got: {value}") from exc


def image_style_metrics(path: Path, accent: str) -> dict[str, float | int | str]:
    if not path.is_file():
        raise FileNotFoundError(path)
    target = _hex_rgb(accent)
    target_hue, target_saturation, _ = colorsys.rgb_to_hsv(
        target[0] / 255.0, target[1] / 255.0, target[2] / 255.0
    )
    target_degrees = target_hue * 360.0
    with Image.open(path) as source:
        width, height = source.size
        image = source.convert("RGB")
        image.thumbnail((256, 256), Image.Resampling.LANCZOS)
        hsv = image.convert("HSV")
        rgb_pixels = list(image.getdata())
        hsv_pixels = list(hsv.getdata())

    total = max(1, len(rgb_pixels))
    saturation_sum = 0.0
    luminance_sum = 0.0
    warm = 0
    dark = 0
    brand_pixels = 0
    for (red, green, blue), (hue, saturation, value) in zip(rgb_pixels, hsv_pixels):
        sat = saturation / 255.0
        val = value / 255.0
        degrees = hue * 360.0 / 255.0
        luminance = (0.2126 * red + 0.7152 * green + 0.0722 * blue) / 255.0
        saturation_sum += sat
        luminance_sum += luminance
        if 25.0 <= degrees <= 75.0 and sat >= 0.25 and val >= 0.55:
            warm += 1
        if luminance < 0.28:
            dark += 1
        rgb_distance = math.sqrt(
            (red - target[0]) ** 2 + (green - target[1]) ** 2 + (blue - target[2]) ** 2
        )
        hue_distance = abs(degrees - target_degrees)
        hue_distance = min(hue_distance, 360.0 - hue_distance)
        brand_family = (
            hue_distance <= 18.0
            and sat >= max(0.22, target_saturation * 0.45)
            and val >= 0.25
        )
        if rgb_distance <= 55.0 or brand_family:
            brand_pixels += 1

    return {
        "path": str(path),
        "width": width,
        "height": height,
        "aspect_ratio": round(width / max(1, height), 4),
        "mean_saturation": round(saturation_sum / total, 4),
        "mean_luminance": round(luminance_sum / total, 4),
        "warm_pixel_ratio": round(warm / total, 4),
        "dark_pixel_ratio": round(dark / total, 4),
        "brand_field_ratio": round(brand_pixels / total, 4),
        "brand_accent_ratio": round(brand_pixels / total, 4),
    }


def _range_score(value: float, low: float, high: float) -> float:
    if low <= value <= high:
        return 1.0
    if value < low:
        return max(0.0, value / max(low, 1e-6))
    return max(0.0, 1.0 - (value - high) / max(1.0 - high, 1e-6))


def _upper_bound_score(value: float, high: float, hard_max: float) -> float:
    if value <= high:
        return 1.0
    if value >= hard_max:
        return 0.0
    return (hard_max - value) / max(hard_max - high, 1e-6)


def analyze_warm_story_fidelity(
    candidate: Path,
    reference_dir: Path,
    *,
    accent: str,
) -> dict[str, Any]:
    references = sorted(reference_dir.glob("reference-*.png"))
    if len(references) < 2:
        raise ValueError(f"Need at least two warm-story references in {reference_dir}")
    candidate_metrics = image_style_metrics(candidate, accent)
    reference_metrics = [image_style_metrics(path, accent) for path in references]

    profile: dict[str, dict[str, float]] = {}
    for key in ("mean_saturation", "mean_luminance", "warm_pixel_ratio", "dark_pixel_ratio"):
        values = [float(item[key]) for item in reference_metrics]
        profile[key] = {
            "mean": round(mean(values), 4),
            "min": round(min(values), 4),
            "max": round(max(values), 4),
        }

    saturation = float(candidate_metrics["mean_saturation"])
    luminance = float(candidate_metrics["mean_luminance"])
    warm_ratio = float(candidate_metrics["warm_pixel_ratio"])
    dark_ratio = float(candidate_metrics["dark_pixel_ratio"])
    brand_ratio = float(candidate_metrics["brand_field_ratio"])

    component_scores = {
        "saturation": 20.0 * _range_score(saturation, 0.40, 0.98),
        "luminance": 15.0 * _range_score(luminance, 0.38, 0.82),
        "warm_secondary_support": 15.0 * _range_score(warm_ratio, 0.06, 0.45),
        "limited_dark_mass": 15.0
        * _upper_bound_score(
            dark_ratio,
            0.18,
            0.40,
        ),
        "mapped_brand_field": 35.0 * _range_score(brand_ratio, 0.25, 0.75),
    }
    score = round(sum(component_scores.values()), 1)
    flags: list[str] = []
    if saturation < 0.40:
        flags.append("too_desaturated_for_branch_b")
    if luminance < 0.38:
        flags.append("too_dark_for_branch_b")
    if warm_ratio < 0.06:
        flags.append("warm_secondary_support_missing")
    elif warm_ratio > 0.45:
        flags.append("yellow_amber_field_not_replaced")
    if dark_ratio > 0.18:
        flags.append("dark_industrial_mass_too_large")
    if brand_ratio < 0.25:
        flags.append("mapped_brand_field_below_25_percent")
    elif brand_ratio > 0.75:
        flags.append("mapped_brand_field_above_75_percent")

    status = "PASS" if score >= 75.0 and not flags else "FAIL"
    return {
        "status": status,
        "score": score,
        "passing_score": 75,
        "candidate": candidate_metrics,
        "reference_profile": profile,
        "reference_count": len(reference_metrics),
        "accent": accent.upper(),
        "brand_color_role": "branch B dominant field replacing yellow/amber",
        "component_scores": {key: round(value, 1) for key, value in component_scores.items()},
        "flags": flags,
        "scope_note": (
            "This branch-B pixel gate checks saturation, light, warm secondary support, dark mass, and whether the mapped brand color replaced the yellow/amber field. "
            "It does not replace the manual 4/5 check for layout silhouette, rounded shape language, depth treatment, and typography mass."
        ),
    }

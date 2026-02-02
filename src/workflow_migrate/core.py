"""Core logic for workflow_migrate."""

from __future__ import annotations

from dataclasses import dataclass
from statistics import mean
from typing import Any


@dataclass(frozen=True)
class AnalysisResult:
    """Structured analysis output."""

    item_count: int
    score: float
    summary: str
    signals: dict[str, float]


def _numeric_values(records: list[dict[str, Any]]) -> list[float]:
    values: list[float] = []
    for record in records:
        for value in record.values():
            if isinstance(value, (int, float)):
                values.append(float(value))
    return values


def analyze_records(records: list[dict[str, Any]]) -> AnalysisResult:
    """Compute a deterministic quality score from record collections.

    The scoring model is intentionally simple and transparent:
    - coverage: non-empty record ratio
    - richness: average number of keys per record
    - numeric_signal: normalized mean of numeric values
    """
    if not records:
        raise ValueError("records must not be empty")

    non_empty = sum(1 for item in records if item)
    coverage = non_empty / len(records)
    richness = mean(len(item.keys()) for item in records) if records else 0.0
    numeric = _numeric_values(records)
    numeric_signal = min(1.0, abs(mean(numeric)) / 100) if numeric else 0.0

    score = round((coverage * 0.45) + (min(1.0, richness / 8) * 0.35) + (numeric_signal * 0.20), 4)
    summary = (
        "healthy"
        if score >= 0.75
        else "watch"
        if score >= 0.5
        else "at-risk"
    )
    signals = {
        "coverage": round(coverage, 4),
        "richness": round(min(1.0, richness / 8), 4),
        "numeric_signal": round(numeric_signal, 4),
    }
    return AnalysisResult(
        item_count=len(records),
        score=score,
        summary=f"{summary} result for: CLI to convert RPA workflows into agent architectures.",
        signals=signals,
    )

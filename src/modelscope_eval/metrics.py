"""Deterministic baseline metrics."""
from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .evaluator import EvaluationResult


def exact_match(response: str, expected: str) -> bool:
    """Compare stripped strings; not a semantic correctness metric."""
    return response.strip() == expected.strip()


def aggregate_results(results: list[EvaluationResult]) -> dict[str, float | int]:
    """Summarize successful evaluations; empty suites have zero metrics."""
    count = len(results)
    return {
        "total": count,
        "passed": sum(result.passed for result in results),
        "accuracy": sum(result.passed for result in results) / count if count else 0.0,
        "mean_latency_ms": sum(result.latency_ms for result in results) / count if count else 0.0,
    }

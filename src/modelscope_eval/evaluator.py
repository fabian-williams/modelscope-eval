"""Model evaluation primitives."""
from __future__ import annotations
from dataclasses import dataclass
from time import perf_counter
from typing import Callable, Iterable, Mapping
from .metrics import exact_match


@dataclass(frozen=True)
class EvaluationResult:
    prompt: str
    expected: str
    response: str
    latency_ms: float
    passed: bool


def evaluate(model: Callable[[str], str], prompt: str, expected: str) -> EvaluationResult:
    """Call a synchronous text model and score exact-match output.

    Exceptions raised by the model propagate to the caller.
    """
    if not isinstance(prompt, str) or not isinstance(expected, str):
        raise TypeError("prompt and expected must be strings")
    start = perf_counter()
    response = model(prompt)
    latency_ms = (perf_counter() - start) * 1000
    if not isinstance(response, str):
        raise TypeError("model must return a string")
    return EvaluationResult(prompt, expected, response, latency_ms, exact_match(response, expected))


def evaluate_suite(model: Callable[[str], str], cases: Iterable[Mapping[str, str]]) -> list[EvaluationResult]:
    """Evaluate mappings with 'prompt' and 'expected' string fields."""
    results = []
    for index, case in enumerate(cases, start=1):
        try:
            prompt, expected = case["prompt"], case["expected"]
        except KeyError as exc:
            raise ValueError(f"case {index} requires prompt and expected") from exc
        results.append(evaluate(model, prompt, expected))
    return results

"""Portable report writers."""
from __future__ import annotations
from dataclasses import asdict
import json
from pathlib import Path
from .evaluator import EvaluationResult
from .metrics import aggregate_results


def save_json_report(results: list[EvaluationResult], path: str | Path) -> None:
    payload = {"summary": aggregate_results(results), "results": [asdict(r) for r in results]}
    Path(path).write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def _cell(value: object) -> str:
    return str(value).replace("|", "\\|").replace("\n", " ").replace("\r", " ")


def save_markdown_report(results: list[EvaluationResult], path: str | Path) -> None:
    summary = aggregate_results(results)
    lines = ["# Model Evaluation Report", "", f"- Cases: {summary['total']}", f"- Passed: {summary['passed']}", f"- Exact-match accuracy: {summary['accuracy']:.2%}", f"- Mean latency: {summary['mean_latency_ms']:.2f} ms", "", "| Prompt | Expected | Response | Pass | Latency (ms) |", "| --- | --- | --- | --- | ---: |"]
    for r in results:
        lines.append(f"| {_cell(r.prompt)} | {_cell(r.expected)} | {_cell(r.response)} | {'Yes' if r.passed else 'No'} | {r.latency_ms:.2f} |")
    Path(path).write_text("\n".join(lines) + "\n", encoding="utf-8")

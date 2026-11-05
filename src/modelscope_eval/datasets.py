"""Load JSON Lines evaluation datasets."""
from __future__ import annotations
import json
from pathlib import Path


def load_jsonl(path: str | Path) -> list[dict[str, str]]:
    cases: list[dict[str, str]] = []
    with Path(path).open("r", encoding="utf-8") as stream:
        for line_number, raw in enumerate(stream, start=1):
            if not raw.strip():
                continue
            try:
                case = json.loads(raw)
            except json.JSONDecodeError as exc:
                raise ValueError(f"Invalid JSON at line {line_number}") from exc
            if not isinstance(case, dict) or not all(
                isinstance(case.get(key), str) for key in ("prompt", "expected")
            ):
                raise ValueError(f"Line {line_number} needs string prompt and expected")
            cases.append({"prompt": case["prompt"], "expected": case["expected"]})
    return cases

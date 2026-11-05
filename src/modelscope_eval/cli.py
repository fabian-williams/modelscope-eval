"""Command-line interface for deterministic local baselines."""
from __future__ import annotations
import argparse
from pathlib import Path
from .adapters import echo_model, upper_model
from .datasets import load_jsonl
from .evaluator import evaluate_suite
from .metrics import aggregate_results
from .reports import save_json_report, save_markdown_report


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Evaluate deterministic text model adapters")
    parser.add_argument("dataset", type=Path, help="JSONL file with prompt and expected keys")
    parser.add_argument("--adapter", choices=["echo", "upper"], default="echo")
    parser.add_argument("--json", type=Path, default=Path("report.json"))
    parser.add_argument("--markdown", type=Path, default=Path("report.md"))
    args = parser.parse_args(argv)
    model = echo_model if args.adapter == "echo" else upper_model
    results = evaluate_suite(model, load_jsonl(args.dataset))
    save_json_report(results, args.json)
    save_markdown_report(results, args.markdown)
    summary = aggregate_results(results)
    print(f"Evaluated {summary['total']} cases; exact-match accuracy: {summary['accuracy']:.1%}")
    print(f"Reports: {args.json}, {args.markdown}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

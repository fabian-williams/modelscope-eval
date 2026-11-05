"""Small, reproducible text-model evaluation toolkit."""
from .evaluator import EvaluationResult, evaluate, evaluate_suite
from .metrics import aggregate_results, exact_match
from .reports import save_json_report, save_markdown_report

__version__ = "0.1.0"
__all__ = ["EvaluationResult", "evaluate", "evaluate_suite", "aggregate_results", "exact_match", "save_json_report", "save_markdown_report"]

"""Run with: python examples/sample_evaluation.py (after pip install -e .)."""
from modelscope_eval import evaluate_suite, aggregate_results
from modelscope_eval.adapters import upper_model

cases = [{"prompt": "hello", "expected": "HELLO"}, {"prompt": "python", "expected": "PYTHON"}]
results = evaluate_suite(upper_model, cases)
print(aggregate_results(results))

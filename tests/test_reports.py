import json
from modelscope_eval import evaluate_suite, aggregate_results, save_json_report, save_markdown_report
from modelscope_eval.adapters import echo_model


def test_aggregate_empty():
    assert aggregate_results([])["accuracy"] == 0.0


def test_reports(tmp_path):
    results = evaluate_suite(echo_model, [{"prompt": "a|b", "expected": "a|b"}, {"prompt": "x", "expected": "y"}])
    assert aggregate_results(results)["accuracy"] == 0.5
    json_path, md_path = tmp_path / "report.json", tmp_path / "report.md"
    save_json_report(results, json_path)
    save_markdown_report(results, md_path)
    assert json.loads(json_path.read_text())["summary"]["passed"] == 1
    assert "a\\|b" in md_path.read_text()

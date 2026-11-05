import json
from modelscope_eval.cli import main


def test_cli(tmp_path):
    dataset = tmp_path / "cases.jsonl"
    dataset.write_text('{"prompt":"hello","expected":"HELLO"}\n', encoding="utf-8")
    output = tmp_path / "output.json"
    markdown = tmp_path / "output.md"
    assert main([str(dataset), "--adapter", "upper", "--json", str(output), "--markdown", str(markdown)]) == 0
    assert json.loads(output.read_text())["summary"]["accuracy"] == 1.0

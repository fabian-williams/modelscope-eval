import pytest
from modelscope_eval.datasets import load_jsonl


def test_load_jsonl(tmp_path):
    path = tmp_path / "cases.jsonl"
    path.write_text('\n{"prompt":"a","expected":"b"}\n', encoding="utf-8")
    assert load_jsonl(path) == [{"prompt": "a", "expected": "b"}]


def test_invalid_json(tmp_path):
    path = tmp_path / "bad.jsonl"
    path.write_text('{bad}', encoding="utf-8")
    with pytest.raises(ValueError, match="line 1"):
        load_jsonl(path)


def test_missing_fields(tmp_path):
    path = tmp_path / "bad.jsonl"
    path.write_text('{"prompt":"x"}', encoding="utf-8")
    with pytest.raises(ValueError, match="Line 1"):
        load_jsonl(path)

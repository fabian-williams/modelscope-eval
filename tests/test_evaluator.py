import pytest
from modelscope_eval import evaluate, evaluate_suite
from modelscope_eval.adapters import echo_model


def test_evaluate_pass():
    result = evaluate(echo_model, "hello", "hello")
    assert result.passed is True
    assert result.latency_ms >= 0


def test_evaluate_fail():
    assert not evaluate(echo_model, "hello", "goodbye").passed


def test_evaluate_strips_whitespace():
    assert evaluate(lambda _: " yes ", "question", "yes").passed


def test_invalid_model_return():
    with pytest.raises(TypeError, match="model must return"):
        evaluate(lambda _: 123, "question", "answer")


def test_invalid_cases():
    with pytest.raises(ValueError, match="case 1"):
        evaluate_suite(echo_model, [{"prompt": "missing expected"}])


def test_model_error_propagates():
    def broken(_):
        raise RuntimeError("provider failed")
    with pytest.raises(RuntimeError, match="provider failed"):
        evaluate(broken, "a", "b")

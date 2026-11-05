# modelscope-eval

**Reproducible, lightweight text-model evaluation in Python.**

[![Tests](https://github.com/fabian-williams/modelscope-eval/actions/workflows/tests.yml/badge.svg)](https://github.com/fabian-williams/modelscope-eval/actions/workflows/tests.yml)
![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)

> Early-stage development release (v0.1.0). This is a deterministic baseline toolkit, **not** a validated benchmark or comprehensive LLM judge.

## Features

- Evaluate any synchronous `Callable[[str], str]` using exact-match scoring
- Run repeatable prompt/expected-output suites from JSON Lines
- Summarize accuracy and measured wall-clock latency
- Export JSON and Markdown reports
- Run an offline CLI with built-in echo and uppercase adapters
- Test across Python 3.10–3.13 with GitHub Actions

## Install

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e '.[dev]'
```

On Windows, activate using `.venv\Scripts\activate`.

## Quick start: Python API

```python
from modelscope_eval import evaluate_suite, aggregate_results

model = lambda prompt: prompt.upper()
cases = [
    {"prompt": "hello", "expected": "HELLO"},
    {"prompt": "python", "expected": "PYTHON"},
]
results = evaluate_suite(model, cases)
print(aggregate_results(results))
```

## CLI example (offline)

```bash
modelscope-eval examples/sample_cases.jsonl --adapter echo --json report.json --markdown report.md
```

Each JSONL line must contain string fields `prompt` and `expected`:

```json
{"prompt": "hello", "expected": "hello"}
```

`--adapter` supports only `echo` and `upper` in this release. Real model integrations can be supplied through the Python API as callables. No API keys or network access are needed for the included examples.

## Development

```bash
ruff check .
pytest -q
python -m build
```

## Limitations and roadmap

- Exact match is sensitive to wording and does not measure semantic correctness.
- Latency includes local callable overhead and is not a normalized provider benchmark.
- Model exceptions propagate; there are no retries or timeouts yet.
- Token counts, cost tracking, multi-provider adapters, asynchronous evaluation, and richer metrics are planned, not implemented.

See [CONTRIBUTING.md](CONTRIBUTING.md) and [CHANGELOG.md](CHANGELOG.md).

## License

MIT — see [LICENSE](LICENSE).

"""Simple deterministic adapters for examples and tests."""
from __future__ import annotations


def echo_model(prompt: str) -> str:
    """Return the prompt unchanged; useful as a no-network baseline."""
    return prompt


def upper_model(prompt: str) -> str:
    """Uppercase the prompt; useful for deterministic smoke tests."""
    return prompt.upper()

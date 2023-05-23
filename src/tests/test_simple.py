# src/tests/test_simple.py
import pytest
from sms.src.text_classification import main

def test_model_diff():
    seed1 = 42
    seed2 = 1234
    accuracy_diff = abs(main(random_state=seed1) - main(random_state=seed2))
    assert accuracy_diff < 0.1, f"Difference in model accuracy with different seeds is too high: {accuracy_diff}"

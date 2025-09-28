from week2.safe_divide import safe_divide
import pytest

def test_division():
    assert safe_divide(4, 2) == 2

def test_zero():
    with pytest.raises(ValueError, match="Error: Division by zero is not allowed."):
        safe_divide(4, 0)

def test_wrong_input():
    with pytest.raises(ValueError, match="Error: Invalid input. Please enter numbers only."):
        safe_divide(12, "x")

def test_no_args():
    with pytest.raises(TypeError):
        safe_divide()
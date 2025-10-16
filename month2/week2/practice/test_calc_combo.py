import pytest


class Calculator:
    def mul(self, a, b):
        return a * b


@pytest.fixture
def calc():
    return Calculator()


@pytest.mark.parametrize("a,b,expected", [(2, 3, 6), (5, 0, 0), (-1, 5, -5)])
def test_multiplication(calc, a, b, expected):
    assert calc.mul(a, b) == expected

import pytest

from month1.week2.cli_calculator import calculate


@pytest.mark.smoke
@pytest.mark.parametrize(
    "x, a, b, expected",
    [
        ("add", 2, 4, 6),
        ("subtract", 9, 7, 2),
        ("multiply", 3, 3, 9),
        ("divide", 12, 6, 2),
        ("power", 9, 8, 43046721),
        ("sqrt", 16, None, 4),
    ],
)
def test_calculator(x, a, b, expected):
    assert calculate(x, a, b) == expected


@pytest.mark.regression
@pytest.mark.parametrize(
    "x, a, b, error",
    [
        ("divide", 8, None, ValueError),
        ("divide", 9, 0, ZeroDivisionError),
        ("sqrt", -4, None, ValueError),
        ("phone", 8, 6, ValueError),
    ],
)
def test_errors(x, a, b, error):
    with pytest.raises(error):
        calculate(x, a, b)

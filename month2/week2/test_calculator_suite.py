import pytest


@pytest.mark.parametrize("a, b, expected", [(3, 2, 5), (9, -1, 8)])
def test_add(run_calc, a, b, expected):
    assert run_calc.add_(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [(8, 2, 6), (20, 7, 13)])
def test_sub(run_calc, a, b, expected):
    assert run_calc.sub_(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [(4, 2, 2), (9, 3, 3)])
def test_div(run_calc, a, b, expected):
    assert run_calc.div_(a, b) == expected


def test_failure(run_calc):
    with pytest.raises(ZeroDivisionError):
        run_calc.div_(5, 0)


@pytest.mark.parametrize("a, b", [(5, []), ("elo", 7), (None, 8)])
def test_input(run_calc, a, b):
    with pytest.raises(TypeError):
        run_calc.add_(a, b)

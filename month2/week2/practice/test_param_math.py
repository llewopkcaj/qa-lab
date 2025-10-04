import pytest

@pytest.mark.parametrize("a,b,expected", [
    (3, 2, 5),
    (10, 5, 15),
    (1, -1, 0)
])
def test_add(a, b, expected):
    assert a + b == expected

import pytest


@pytest.mark.xfail(reason="Intentional demo from day4")
def test_fail():
    assert 2 + 2 == 8

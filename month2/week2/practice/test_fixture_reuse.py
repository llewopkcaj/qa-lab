import pytest


@pytest.fixture
def numbers():
    return [1, 2, 3, 4, 5]


def test_sum(numbers):
    assert sum(numbers) == 15


def test_max(numbers):
    assert max(numbers) == 5

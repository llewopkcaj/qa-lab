import pytest

# Simulated math_ops.py
def add(a, b): 
    return a + b
def sub(a, b): 
    return a - b
def mul(a, b):
    return a * b
def div(a, b):
    return a / b

# Not necessary to reuse each function
# We could also just write assert a + b == expected here

@pytest.mark.parametrize("a, b, expected", [
    (3, 3, 6), (2, 2, 4), (3, 5, 8)
])  
def test_add(a, b, expected):
    assert add(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (9, 8, 1),
    (5, 2, 3),
    (6, 4, 2)
])
def test_sub(a, b, expected):
    assert sub(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (2, 2, 4),
    (3, 10, 30),
    (6, 8, 48)
])
def test_mul(a, b, expected):
    assert mul(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (8, 2, 4),
    (9, 3, 3),
    (20, 5, 4)
])
def test_div(a, b, expected):
    assert div(a, b) == expected
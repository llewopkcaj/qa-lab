from week2.math_utils import add, mean, describe_person

def test_add():
    assert add(3, 4) == 7
    assert add(-1, 1) == 0
    assert add(-5, -5) == -10

def test_mean():
    assert mean(2, 4, 6) == 4
    assert mean(10, 20, 30) == 20
    assert mean(1.5, 2.5, 3.5) == 2.5
    assert mean(10) == 10
    # empty call would raise ZeroDivisionError because it's calculated differently in original script, but we’ll test that later (day 6?)

def test_describe_person():
    result = describe_person("Alice", age=30, city="New York", profession="Engineer")
    assert "Alice" in result
    assert "30" in result
    assert "New York" in result
    assert "Engineer" in result



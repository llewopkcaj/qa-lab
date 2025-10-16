def test_math():
    assert 2 * 2 == 4


def test_string():
    assert "data.csv".endswith(".csv")


def test_list():
    items = [6, "three", 22, 9, "dog"]
    assert 9 in items

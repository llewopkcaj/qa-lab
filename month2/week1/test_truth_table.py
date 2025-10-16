from month1.week2.truth_table import truth_table


def test_truth_table():
    results = truth_table()
    expected = [True, False, False, True, True, True]
    assert results == expected


def test_truth_table_counts():
    results = truth_table()
    assert results.count(True) == 4
    assert results.count(False) == 2

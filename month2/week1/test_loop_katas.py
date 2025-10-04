from week2.loop_katas import sum_1_to_100, every_third_0_to_30, enumerate_with_index, countdown_from_10, find_first_multiple_of_7

def test_sum_1_to_100():
    result = sum_1_to_100()
    assert result == 5050

def test_every_third_0_to_30():
    result = every_third_0_to_30()
    assert result[0] == 0
    assert result[-1] == 30
    assert all(result[i] - result[i-1] == 3 for i in range(1, len(result)))

def test_enumerate_with_index():
    result = enumerate_with_index(["red", "blue", "green"])
    assert "2: blue" in result
    assert result == ["1: red", "2: blue", "3: green"]

def test_countdown_from_10(): 
    result = countdown_from_10()
    assert result == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

def test_find_first_multiple_of_7():
    assert find_first_multiple_of_7(4) is None
    assert find_first_multiple_of_7(7) == 7
    assert find_first_multiple_of_7(9000000) == 7



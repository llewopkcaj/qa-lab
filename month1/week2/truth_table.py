def truth_table():
    return [
        (5 == 5 or 2 > 10),  # True
        (7 < 3 and 4 == 4),  # False
        (not (8 > 2)),  # False
        (10 != 5 and 3 < 7),  # True
        (6 >= 6 or 2 == 9),  # True
        (not (1 == 2 or 3 > 5)),  # True
    ]

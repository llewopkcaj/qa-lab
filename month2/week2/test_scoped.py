def test_ing_scope(first_connection):
    assert first_connection == 12345


def test_second_test(first_connection):
    assert isinstance(first_connection, int)

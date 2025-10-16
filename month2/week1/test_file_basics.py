from month1.week3.file_basics import write_and_read


def test_write_and_read(tmp_path):
    result = write_and_read(tmp_path / "test.txt")
    assert "Hi there!" in result[0]
    assert "Anyone home?" in result[1]

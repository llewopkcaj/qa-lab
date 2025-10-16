import json

import pytest

from month1.week3.QA_json_to_csv import json_to_csv_from_existing


def test_missing_file(tmp_path):
    missing_path = tmp_path / "nonexistant" / "nopath.json"
    with pytest.raises(FileNotFoundError):
        json_to_csv_from_existing(missing_path)


def test_malformed_file(tmp_path):
    bad_path = tmp_path / "badfile.json"
    bad_path.write_text("{iusdhiufh}")
    with pytest.raises(json.JSONDecodeError):
        json_to_csv_from_existing(bad_path)


def test_empty_file(tmp_path):
    empty_path = tmp_path / "empty.json"
    empty_path.write_text(" ")
    with pytest.raises(json.JSONDecodeError):
        json_to_csv_from_existing(empty_path)


def test_malformed_path_is_directory(tmp_path):
    bad_path = tmp_path / "not_a_file"
    bad_path.mkdir()
    with pytest.raises(IsADirectoryError):
        json_to_csv_from_existing(bad_path)


def test_wrong_input(tmp_path):
    wrong_path = tmp_path / "wrong.json"
    wrong_path.write_text(json.dumps(["a", "b", "c"]))
    with pytest.raises(TypeError, match="Expected JSON to be a list of objects"):
        json_to_csv_from_existing(wrong_path)

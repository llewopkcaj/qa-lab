import json
import csv
from week3.json_profile import first_file, second_file_edit
from week3.json_to_csv import json_to_csv

def test_first_file(tmp_path):
    path = tmp_path / "first.json"
    result = first_file(path)
    assert result["Name"] == "Bobby"
    assert "cool" in result["Skills"]
    assert isinstance(result, dict)

    with open(path) as f:
        on_disk = json.load(f)
    assert on_disk == result

def test_second_file_edit(tmp_path):
    path = tmp_path / "second.json"
    original = first_file(path)
    result = second_file_edit(path)
    assert "fast" in result["Skills"]
    assert len(result["Skills"]) == len(original["Skills"]) + 1

    with open(path) as f:
        saved = json.load(f)
    assert saved == result

def test_json_to_csv(tmp_path):
    json_path = tmp_path / "data.json"
    result = json_to_csv(json_path)
    assert "Wrote 3 rows to" in result  

    csv_path = json_path.with_suffix(".csv")
    with open(csv_path, newline="") as f:
        reader = list(csv.DictReader(f))
        assert result.startswith("Wrote 3 rows to")
        assert len(reader) == 3
        assert any(row.get("King") == "13" for row in reader)
        assert any(row.get("Jordan") == "23" for row in reader)
        assert all(isinstance(v, str) for row in reader for v in row.values())






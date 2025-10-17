import csv
from typing import Any

with open("missing.csv", "w", newline="") as file:
    rows: list[dict[str, str]] = [
        {"color": "elephant"},
        {"color": "sapphire", "shape": "oblong", "size": "medium"},
        {"shape": "sphere", "size": "large"},
        {"color": "polychrome", "size": "small"},
        {"shape": "pyramid", "size": "monumental"},
        {"color": "mauve", "shape": "disk"},
    ]
    fieldnames: list[str] = ["color", "shape", "size"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)


def safe_get(row: dict[str, Any], key: str, default: str = "n/a") -> str:
    val = row.get(key)
    if not val:
        return default
    return str(val)


with open("missing.csv", newline="") as file:
    reader = csv.DictReader(file)
    if reader.fieldnames is not None:
        print(*reader.fieldnames)
        for row in reader:
            final = [safe_get(row, key) for key in fieldnames]
            print(*final)
    else:
        print("No fieldnames found in CSV file.")

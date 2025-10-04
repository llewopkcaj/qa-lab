import json
import csv
from pathlib import Path

def json_to_csv_from_existing(path):
    path = Path(path)

    # 1) Read whatever is already there (this can raise JSONDecodeError)
    with path.open("r") as f:
        pre_csv = json.load(f)

    # 2) Validate structure: expect a list of dicts
    if not isinstance(pre_csv, list) or not all(isinstance(row, dict) for row in pre_csv):
        raise TypeError("Expected JSON to be a list of objects (list[dict]).")

    # 3) Build CSV
    fieldnames = sorted({k for row in pre_csv for k in row.keys()})
    csv_path = path.with_suffix(".csv")

    with csv_path.open("w", newline="") as out:
        writer = csv.DictWriter(out, fieldnames=fieldnames, restval="")
        writer.writeheader()
        writer.writerows(pre_csv)

    return f"Wrote {len(pre_csv)} rows to {csv_path}"

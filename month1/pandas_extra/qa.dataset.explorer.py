import pandas as pd
import sys
from pathlib import Path
import json

if len(sys.argv) < 2:
    print("usage: python qa.dataset.explorer.py <filename>")
    sys.exit(1)

csv_path = Path(sys.argv[1])

if not csv_path.is_file():
    print(f"error: {csv_path} does not exist.")
    sys.exit(1)

data = pd.read_csv(csv_path)
shape = data.shape
null_count = data.isnull().sum().to_dict()
columns = data.columns.tolist()
print(shape, null_count, columns)

chosen_column = str(input(f"Pick a column from {columns}"))
result = data[chosen_column].value_counts(dropna=False).head(5).to_dict()
print(result)

combined = {
    "shape": {"rows": shape[0], "columns": shape[1]},
    "columns": columns,
    "empty cells": null_count,
    "selected column": chosen_column,
    "top values": result
}

with open("colors.json", "w") as f:
    json.dump(combined, f, indent=2)
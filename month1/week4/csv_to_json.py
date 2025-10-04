import csv
import json

try:
    with open("data_reverse.csv", "r") as file:
        reader = csv.DictReader(file)
        rows = list(reader)

    with open("data_reverse.json", "w") as file:
        json.dump(rows, file, indent=4, sort_keys=True)

    print(f"Converted {len(rows)} rows into data_reverse.json")

except FileNotFoundError:
    print("Error: data_reverse.csv not found. Make sure the file exists.")
except Exception as e:
    print(f"Unexpected error: {e}")

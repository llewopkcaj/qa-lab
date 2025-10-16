import csv

with open("missing.csv", "w") as file:
    rows = [
        {"color": "elephant"},
        {"color": "sapphire", "shape": "oblong", "size": "medium"},
        {"shape": "sphere", "size": "large"},
        {"color": "polychrome", "size": "small"},
        {"shape": "pyramid", "size": "monumental"},
        {"color": "mauve", "shape": "disk"},
    ]
    fieldnames = ["color", "shape", "size"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)


def safe_get(row, key, default="n/a"):
    val = row.get(key)
    if not val:
        return default
    return val


with open("missing.csv") as file:
    reader = csv.DictReader(file)
    if reader.fieldnames is not None:
        print(*reader.fieldnames)
        for row in reader:
            final = [safe_get(row, key) for key in fieldnames]
            print(*final)
    else:
        print("No fieldnames found in CSV file.")

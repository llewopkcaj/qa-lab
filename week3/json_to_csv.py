import json
import csv

data = [
    {"Jack": 11, "Queen": 12, "King": 13, "Ace": 14},
    {"Blue": 8, "Orange": 10, "Green": 4, "Pink": 5},
    {"Steph": 30, "Jordan": 23, "Shaq": 34, "Kobe": 8}
]

with open("data.json", "w") as file:
    json.dump(data, file, indent=4)

with open("data.json", "r") as file:
    pre_csv = json.load(file)
    fieldnames = sorted({k for row in pre_csv for k in row.keys()})

    with open ("data.csv", "w", newline="") as new_csv:
        final = csv.DictWriter(new_csv, fieldnames=fieldnames, restval="")
        final.writeheader()
        final.writerows(pre_csv)

        print(f"Wrote {len(pre_csv)} rows to data.csv")


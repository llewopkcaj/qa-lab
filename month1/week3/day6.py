import csv
import os

file_path = os.path.join(os.path.dirname(__file__), "MOCK_DATA.csv")

count = 0
with open(file_path, newline="") as sounds:
    reader = csv.DictReader(sounds)
    for row in reader:
        if row["sound_frequency"] == "Monthly":
            count += 1

print("Number of Monthly Rows:", count)

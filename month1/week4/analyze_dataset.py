import csv
import json

org_count = 0
male_count = 0

with open("MOCK_DATA-2.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        email = row["email"]
        gender = row["gender"]
        if ".org" in email:
            org_count += 1
        if "male" in gender:
            male_count += 1
    summary = {"org_count": org_count, "male_count": male_count}


with open("summary.json", "w") as file:
    json.dump(summary, file, indent=4)

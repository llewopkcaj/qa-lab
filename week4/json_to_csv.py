import json
import csv

with open("data.json", "r") as file:
    reader = json.load(file)
  
with open("data.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "email", "age", "country"])
    writer.writeheader()
    
    for row in reader:
        writer.writerow({
            "name": row.get("name", "n/a"),
            "email": row.get("email", "n/a"),
            "age": row.get("age", "n/a"),
            "country": row.get("country", "n/a")
        })

with open("data.csv", "r") as file:
    csvread = csv.DictReader(file)
    rows = list(csvread)
    print(f"Wrote {len(rows)} rows to data.csv")


     
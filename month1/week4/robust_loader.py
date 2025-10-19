import csv
import json
import sys

if len(sys.argv) < 2:
    print("Usage: python script.py <filename>")
    sys.exit(1)
filename = sys.argv[1]

try:
    if filename.endswith(".csv"):
        with open(filename) as f:
            reader = csv.DictReader(f)
            for row in reader:
                print(row)
    elif filename.endswith(".json"):
        with open(filename) as f:
            json_reader = json.load(f)
            for row in json_reader:
                print(row)
    else:
        print("Unsupported file type", filename)

except (json.JSONDecodeError, FileNotFoundError) as e:
    print("Error: ", e)

except Exception as e:
    print("Unknown error: ", e)

# Week 4 — CSV + JSON Automation Projects

## Pages / Articles Read
- Python Docs: `csv.DictReader`, `DictWriter`
- Python Docs: `json.dump` / `json.load` variations
- Real Python: Reading and Writing CSV Files
- Real Python: Working with JSON Data in Python
- W3Schools: File Handling + JSON Exercises

## Exercises Completed
- `csv_missing.py` — handled missing fields with `.get()`
- `json_pretty.py` — created pretty + minified JSON
- `json_to_csv.py` — converted JSON → CSV
- `csv_to_json.py` — converted CSV → JSON
- `analyze_dataset.py` — analyzed dataset (Gmail count, over-30 count)
- `robust_loader.py` — loaded CSV/JSON with error handling

## Code Snippets I’m Proud Of
```python
# Handling missing CSV keys gracefully
final = [row.get(key, "N/A") for key in fieldnames]

# Pretty vs minified JSON
json.dump(data, f, indent=4, sort_keys=True)
json.dump(data, f)  # minified

# Robust loader with extension detection
if filename.endswith(".csv"):
    reader = csv.DictReader(open(filename))
elif filename.endswith(".json"):
    data = json.load(open(filename))

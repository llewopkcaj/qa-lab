import json
import os

with open("messy.json") as f:
    data = json.load(f)
print(f"UNFORMATTED: \n{data}")

with open("pretty.json", "w") as f:
    json.dump(data, f, indent=4, sort_keys=True)

print(f"PRETTY VERSION: \n{json.dumps(data, indent=2, sort_keys=True)}")

with open("mini.json", "w") as f:
    json.dump(data, f, separators=(",", ":"))

print(rf"MINIMAL VERSION: n\{json.dumps(data, separators=(",", ":"))}")

raw_size = os.path.getsize("messy.json")
pretty_size = os.path.getsize("pretty.json")
mini_size = os.path.getsize("mini.json")

print(f"Raw size:     {raw_size} bytes")
print(f"Pretty size:  {pretty_size} bytes")
print(f"Minified size:{mini_size} bytes")

print(f"Pretty vs Raw:  {pretty_size - raw_size} bytes")
print(f"Minified vs Raw: {mini_size - raw_size} bytes")

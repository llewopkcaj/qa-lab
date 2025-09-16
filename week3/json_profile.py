import json

profile = {"Name": "Bobby", "Age": 82, "Skills": ["cool", "smart", "sneaky"]}

with open("profile.json", "w") as file:
    json.dump(profile, file, indent=4)

with open("profile.json", "r") as file:
    x = json.load(file)

        #print(x) would still print the file
print(f"Name: {x['Name']}")
print(f"Age: {x['Age']}")
print(f"Skills: {', '.join(x['Skills'])}") #for .join the pattern is always: "SEPARATOR".join(LIST_OF_STRINGS)

x["Skills"].append("fast")

with open("profile.json", "w") as file:
    json.dump(x, file, indent=4)
  

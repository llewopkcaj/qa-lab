profile = {"name": "Jack Powell", "age": 25, "focus": "QA Automation"}
routine = ["study python", "breakfast", "work on Sierra Chart", "climb", "snack", "work on writing"]
dashboard = "=====Daily Dashboard=====\n"
for task in range(6):
    dashboard += f"{task+1}.) {routine[task]}\n"
dashboard += (
    f"{profile['name']} is {profile['age']} and is studying python to learn {profile['focus']}"
)
print(dashboard)
with open("dashboard.txt", "w") as file:
    file.write(dashboard)

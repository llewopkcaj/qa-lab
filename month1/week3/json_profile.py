import json

profile = {"Name": "Bobby", "Age": 82, "Skills": ["cool", "smart", "sneaky"]}


def first_file(path):

    with open(path, "w") as file:
        json.dump(profile, file, indent=4)

    with open(path) as file:
        x = json.load(file)
        return x


def second_file_edit(path):
    with open(path) as file:
        x = json.load(file)
        x["Skills"].append("fast")

    with open(path, "w") as file:
        json.dump(x, file, indent=4)
        return x

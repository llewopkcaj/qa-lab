bob = {"name": "Bob", "email": "bobdog@duck.com", "tags": ["dog", "cat", "fish"]}
kelcey = {"name": "Kelcey", "email": "kelsbells@shrug.com", "tags": ["girl", "mean"]}
suey = {"name": "Suey", "email": "sueydo@seemail.com", "tags": ["mid", "ok person"]}
contacts = [bob, kelcey, suey]
for contact in contacts:
    print(contact["name"], "-->", contact["tags"][0])
jimmey = {
    "name": "Jimmey",
    "email": ["jimmey@luck.com", "bimbo@dumb.com"],
    "tags": ["dude", "food"],
}
contacts.append(jimmey)
print(contacts[3]["email"][1])

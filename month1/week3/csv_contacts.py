import csv

data = [
    {"Name": "Deji", "Email": "dejio@email.org", "Tag": "friend"},
    {"Name": "Doja", "Email": "dojey@cat.com", "Tag": "not-friend"},
    {"Name": "Tonk", "Email": "tonkey@bonk.com", "Tag": "enemy"},
]

with open("contacts.csv", "w", newline="") as contacts:
    fieldnames = ["Name", "Email", "Tag"]
    writecontact = csv.DictWriter(contacts, fieldnames=fieldnames)
    writecontact.writeheader()
    writecontact.writerows(data)

with open("contacts.csv") as contacts:
    readcontact = csv.DictReader(contacts)
    for row in readcontact:
        print(row["Name"], row["Email"], row["Tag"])

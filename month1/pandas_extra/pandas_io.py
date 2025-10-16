import pandas as pd

dfile = pd.read_csv("/Users/jackpowell/Documents/qa-month1/week3/contacts.csv")

print(dfile.head())

dfile.to_csv("contacts.copy.csv", index=False)
dfile.to_json("contacts.json", orient="records", indent=4)

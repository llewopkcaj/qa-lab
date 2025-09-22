import pandas as pd

reader = pd.read_csv("/Users/jackpowell/Documents/qa-month1/week5/MOCK_DATA-3.csv")

print(reader["email"].isnull().sum())

reader["email"] = reader["email"].fillna("unknown@mail.com")

print("Before drop:", len(reader))
reader.dropna(subset=["ip_address"], inplace=True)
print("After drop:", len(reader))

reader.to_csv("/Users/jackpowell/Documents/qa-month1/week5/MOCK_DATA-3_clean.csv", index=False)

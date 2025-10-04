import pandas as pd

nofilter = pd.read_csv("/Users/jackpowell/Documents/qa-month1/week4/data_reverse.csv")

filter_rows = nofilter[nofilter["age"] < 30][["name", "email"]]
locfilter = nofilter.loc[nofilter["age"] < 30, ["name", "email"]]
ilocfilter = nofilter.iloc[2:4, 0:2]

print("Boolean filter:\n", filter_rows)
print("\nloc filter:\n", locfilter)
print("\niloc filter:\n", ilocfilter)

import pandas as pd

reader = pd.read_csv("/Users/jackpowell/Documents/qa-month1/week3/MOCK_DATA.csv")
mask = reader["color_family"].str.contains("cool", case=False, na=False)
cool_num = mask.value_counts()
print("Cool vs non-cool rows:\n", cool_num)

summary = (reader.groupby("sound_waveform")["color_saturation"]
        .mean()
        .reset_index())
summary.to_csv("summary.csv", index=False)



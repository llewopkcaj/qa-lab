import pandas as pd

x = pd.Series([9, 0, 6, 2, 1, 8, 9])
print (x)

frame = pd.DataFrame({
    "evens": [0, 2, 4, 6, 8, 10, 12, 14, 16],
    "odds": [1, 3, 5, 7, 9, 11, 13, 15, 17],
    "fib": [1, 2, 3, 5, 8, 13, 21, 34, 55]
})

print(frame.head(), frame.shape, frame.dtypes)

import pandas as pd
df = pd.read_csv('Data\\311_2025_Jan_Dec.csv', low_memory=False)
print(df.head())
print(df.info())

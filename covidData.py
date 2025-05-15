import pandas as pd

df = pd.read_csv('owid-covid-data.csv')
df['date'] = pd.to_datetime(df['date'])

print(df.head())
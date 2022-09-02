import pandas as pd
import openpyxl

df = pd.read_csv('pokemon_data.csv')

df_xlx = pd.read_excel('pokemon_data.xlsx')

print(df)

df.columns

print(df[['Name','Type 1', 'HP']])


# 1- columns, rows?
# 2- what type of?
# 3- missing data?

#info()
"""
number of rows and columns
column name
int64 fload64 object
non null counts
memory usuage of the data frame
"""

import pandas as pd

df = pd.read_json(r"C:\Users\Aman Kumar\Downloads\sample_Data.json")

print(df.tail())

print(df.info())

print(df.describe())

print(f'Shape: {df.shape}')

print(f'Shape: {df.columns}')
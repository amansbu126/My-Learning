"""
select specfic column
filter rows
combine multiple conditions

[] columns access
boolean condition for used to filter data

column = df["column name"]
subset = df["columns1","column2",...]

#based on a single condition

filtered_rows = df[df["column name"]>5000]

#combined multiple condition

filtered_rows = df[(df["column name"]>5000) & (df["column name"]<8000)]
"""

import pandas as pd

data = {
    "Name":['Ross','Anoop','Swaroop','Kiran','Ankit','Shripal','Aman Kumar','Aman Sinha'],
    "Age":[50,45,40,39,38,28,30,29],
    "Salary":[100000,80000,60000,55000,40000,25000,30000,28000],
    "NPS Score":[85,90,56,89,91,67,89,97]
}

df = pd.DataFrame(data)

print(df.head())

#Selection single column
print(df["Name"])

#Selection multiple column

subset=df[["Name","Salary"]]
print(subset)

#get all names where salary is >50000

filter=df[df["Salary"]>50000]
print(filter)

#MULTI CONDITION

filter_multi=df[(df["Salary"]>30000) & (df["Salary"]<50000)]
print(filter_multi)

#using OR condition

filtered_or= df[(df['Age']>30) | (df['NPS Score']>70)]
print(filtered_or)
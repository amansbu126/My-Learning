import pandas as pd

data = {
    "Name":['Ross','Anoop','Swaroop','Kiran','Ankit','Shripal','Aman Kumar','Aman Sinha'],
    "Age":[50,45,40,39,38,28,30,29],
    "Salary":[100000,80000,60000,55000,40000,25000,30000,28000],
    "NPS Score":[85,90,56,89,91,67,89,97]
}

df = pd.DataFrame(data)

print(df)
# square brackets df["columns_mame"]=some_data
df["Bonus"] = df["Salary"] * 0.1
print(df)
# added new column

#using insert() for addition of new column
# df.insert(loc, "column_name, some_data")
# loc-> location

df.insert(0,"emp_id",[1,2,3,4,5,6,7,8])
print(df)

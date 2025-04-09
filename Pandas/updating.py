import pandas as pd

data = {
    "Name":['Ross','Anoop','Swaroop','Kiran','Ankit','Shripal','Aman Kumar','Aman Sinha'],
    "Age":[50,45,40,39,38,28,30,29],
    "Salary":[100000,80000,60000,55000,40000,25000,30000,28000],
    "NPS Score":[85,90,56,89,91,67,89,97]
}

df = pd.DataFrame(data)

print(df)

# .loc[]
# df.loc[row_index,"column_name"]=new_value

df.loc[6,'Salary']=34500

print(df)
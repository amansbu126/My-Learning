import pandas as pd

data = {
    "Name":['Ross','Anoop','Swaroop','Kiran','Ankit','Shripal','Aman Kumar','Aman Sinha'],
    "Age":[50,45,40,39,38,28,30,29],
    "Salary":[100000,80000,60000,55000,40000,25000,30000,28000],
    "NPS Score":[85,90,56,89,91,67,89,97],
    "Gender":['m','m','m','m','m','m','m','m']
}

df = pd.DataFrame(data)
print(df)

# df.drop(column=["column_name"],inplace=True)
#inplace-> it represts/modify the original dataframe

print("post modified")

#df.drop(columns=['Gender'],inplace=True)
#print(df)

df.drop(columns=['Gender','NPS Score'],inplace=True)
print(df)
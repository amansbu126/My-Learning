import pandas as pd

data = {
    "Name":['Ross','None','Swaroop','Kiran','Ankit','Shripal','Aman Kumar','Aman Sinha'],
    "Age":[50,None,40,45,38,28,30,29],
    "Salary":[100000,None,60000,55000,40000,25000,30000,28000],
    "NPS Score":[85,None,90,89,91,67,89,97],
    "Gender":['m',None,'m','m','m','m','m','m']
}

df = pd.DataFrame(data)
print(df)

print(df.isnull())

print(df.isnull().sum())

df.dropna(axis=0,inplace=True)

print(df)
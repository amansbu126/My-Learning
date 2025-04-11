import pandas as pd

data = {
    "Name":['Ross','Anoop','Swaroop','Kiran','Ankit','Shripal','Aman Kumar','Aman Sinha'],
    "Age":[50,48,40,45,38,28,30,29],
    "Salary":[100000,70000,60000,50000,40000,5000,30000,2000],
    "NPS Score":[85,95,90,89,91,67,89,97],
    "Gender":['m','m','m','m','m','m','m','m']
}

df=pd.DataFrame(data)
print(df)

avg_salary=df["Salary"].mean()
print(avg_salary)
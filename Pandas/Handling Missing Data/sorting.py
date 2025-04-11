import pandas as pd

data = {
    "Name":['Ross','Anoop','Swaroop','Kiran','Ankit','Shripal','Aman Kumar','Aman Sinha'],
    "Age":[50,48,40,45,38,28,30,29],
    "Salary":[100000,70000,60000,50000,40000,5000,30000,2000],
    "NPS Score":[85,95,90,89,91,67,89,97],
    "Gender":['m','m','m','m','m','m','m','m']
}

#sort_values()
#df.sort_values(by="column_name",True/false,inplace=True)
#true -> asc
#False -> dec
df=pd.DataFrame(data)
print(df)

#single column
#df.sort_values(by="Salary",ascending=False,inplace=True)
#print(df)

#multi value
print("after sorting")
df.sort_values(by=["NPS Score","Salary"],ascending=[False,True],inplace=True)
print(df)
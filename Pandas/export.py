import pandas as pd

data = {
    "Name":["Mohan","Rohan","Sohan"],
    "Wage":[500,700,900]
}

df=pd.DataFrame(data)
print(df)

#index nhi chahie then we keep index false
#df.to_csv("output.csv",index=False)
df.to_json("output.json",index=False)
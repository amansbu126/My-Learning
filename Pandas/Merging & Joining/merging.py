#pd.merge(df1,df2,on="column_name",how="type of join")
import pandas as pd

#customer dataframe
df_customers=pd.DataFrame({
    "CustomerID":[1,2,3],
    "Name":["Ram","Shyam","Krishna"]
})

#order data
df_orders=pd.DataFrame({
        "CustomerID":[1,2,4],
        "Sales":[2000,500,6789]
})

df_merged=pd.merge(df_customers,df_orders,on="CustomerID",how="outer")
print(df_merged)
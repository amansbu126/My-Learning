#pd.concat([df1,df2]=axis=0,ignore_index=True)
import pandas as pd

#customer dataframe
df_customers1=pd.DataFrame({
    "CustomerID":[1,2,3],
    "Name":["Ram","Shyam","Krishna"]
})

#customer dataframe
df_customers2=pd.DataFrame({
    "CustomerID":[4,5],
    "Name":["Aman","Ankit"]
})

#axis 0 -> vertically
d_concate=pd.concat([df_customers1,df_customers2],axis=0,ignore_index=True)
print(d_concate)

#axis 0 -> horizontally
d_concate=pd.concat([df_customers1,df_customers2],axis=1,ignore_index=True)
print(d_concate)
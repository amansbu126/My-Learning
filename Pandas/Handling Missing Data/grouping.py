import pandas as pd

data = {
    "Campaign":['Ross','Anoop','Swaroop','Kiran','Ankit','Shripal','Aman Kumar','Aman Sinha'],
    "Channel":['Video','Video','Display','Paid Search','Paid Search','Paid Search','Video','Display'],
    "Spend":[100000,70000,60000,50000,40000,5000,30000,2000],
    "Sessions":[85,95,90,89,91,67,89,97],
}

df=pd.DataFrame(data)
print(df)

grouped = df.groupby("Channel")["Spend"].sum()
print(grouped)

grouped_channel_Campaign=df.groupby(["Channel","Campaign"])["Spend"].sum()
print(grouped_channel_Campaign)
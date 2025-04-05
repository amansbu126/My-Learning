import pandas as pd

# Below encoding is used to change file format for cumputer undersatnding language here python is unable to understand henece we need to chnage with encoding
#encoding="utf-8"
#encoding="latin1"

#gcsfs -> to read data from cloud platform
#df= pd.read_excel
#df = pd.read_json



df = pd.read_csv(r"C:\Users\Aman Kumar\Downloads\sales_data_sample.csv",encoding="latin1")

print(df)
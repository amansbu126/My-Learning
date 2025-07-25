import boto3
import json
import psycopg2
import pandas as pd

# AWS + S3 Setup
s3 = boto3.client('s3')


bucket = 'awsdataengineering-755649256616-ap-south-1'
key = 'data-ingestion/raw/data.json'


s3.upload_file(
    Filename='C:/Users/Aman Kumar/OneDrive/2025/My-Learning/project/data_uploads/json_files/data.json',
    Bucket=bucket,
    Key=key
)

# Download and parse JSON
obj = s3.get_object(Bucket=bucket, Key=key)
data = json.loads(obj['Body'].read())

# Convert to DataFrame (if it's a list of records)
df = pd.DataFrame(data)

print(df)
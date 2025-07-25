import boto3
import json
import psycopg2
import pandas as pd

# AWS + S3 Setup
s3 = boto3.client('s3')
bucket = 'your-bucket-name'
key = 'C:/Users/Aman Kumar/OneDrive/2025/My-Learning/project/data_uploads/json_files/data.json'

# Download and parse JSON
obj = s3.get_object(Bucket=bucket, Key=key)
data = json.loads(obj['Body'].read())

# Convert to DataFrame (if it's a list of records)
df = pd.DataFrame(data)

# RDS connection
conn = psycopg2.connect(
    host='your-rds-endpoint',
    port=5432,
    database='your-db-name',
    user='your-db-user',
    password='your-db-password'
)

# Insert into RDS table
cursor = conn.cursor()

for _, row in df.iterrows():
    cursor.execute(
        "INSERT INTO your_table (col1, col2, col3) VALUES (%s, %s, %s)",
        (row['field1'], row['field2'], row['field3'])
    )

conn.commit()
cursor.close()
conn.close()

# (Optional) Move file to /processed/ after success
s3.copy_object(
    Bucket=bucket,
    CopySource={'Bucket': bucket, 'Key': key},
    Key=key.replace("raw/", "processed/")
)
s3.delete_object(Bucket=bucket, Key=key)

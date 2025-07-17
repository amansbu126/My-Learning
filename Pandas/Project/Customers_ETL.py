from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import pandas as pd
from sqlalchemy import create_engine, text

# --- ETL Function ---
def run_etl():
    EXCEL_FILE = "/mnt/c/Users/Aman Kumar/Downloads/Ex_Files_ETL_Python_SQL/Ex_Files_ETL_Python_SQL/Exercise Files/Chapter_2/H+ Sport Customers.xlsx"
    DB_USER = "root"
    DB_PASSWORD = "aman"
    DB_HOST = "localhost"
    DB_PORT = 3306
    DB_NAME = "HR"

    try:
        engine = create_engine(f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")
        with engine.connect() as conn:
            result = conn.execute(text("SELECT NOW();"))
            for row in result:
                print("✅ Connected to MySQL. Current Time:", row[0])
    except Exception as e:
        print("❌ Failed to connect to MySQL:", e)
        return

    try:
        df = pd.read_excel(EXCEL_FILE)
        print(f"🔍 Read {len(df)} rows from Excel.")
    except Exception as e:
        print("❌ Failed to read Excel file:", e)
        return

    try:
        df.to_sql("customers", con=engine, if_exists="append", index=False)
        print("✅ Data loaded into MySQL table 'customers'.")
    except Exception as e:
        print("❌ Failed to load data into MySQL:", e)

# --- Airflow DAG Definition ---
with DAG(
    dag_id="customers_etl_dag",
    start_date=datetime(2023, 1, 1),
    schedule_interval="@daily",
    catchup=False,
    tags=["ETL", "Excel", "MySQL"],
) as dag:
    task_run_etl = PythonOperator(
        task_id="run_excel_to_mysql_etl",
        python_callable=run_etl
    )

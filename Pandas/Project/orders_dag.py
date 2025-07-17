from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from Customers_ETL import run_etl  # or `main` if that’s your function name

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2025, 7, 17),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    dag_id='customers_etl_dag',
    default_args=default_args,
    description='ETL pipeline to load Excel data into MySQL',
    schedule_interval='@daily',  # Change to "@daily" or "0 0 * * *" to schedule
    catchup=False,
)

run_etl_task = PythonOperator(
    task_id='run_customers_etl',
    python_callable=run_etl,  # change to `main` if that’s the function name
    dag=dag,
)

run_etl_task

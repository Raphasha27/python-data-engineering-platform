"""Airflow DAG for data pipeline"""
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator


default_args = {
    'owner': 'data-engineer',
    'depends_on_past': False,
    'start_date': datetime(2026, 8, 27),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}


def ingest_data():
    print("Ingesting data...")
    return "Data ingested"


def transform_data():
    print("Transforming data...")
    return "Data transformed"


def load_data():
    print("Loading data...")
    return "Data loaded"


with DAG(
    'data_pipeline',
    default_args=default_args,
    description='Data engineering pipeline',
    schedule_interval=timedelta(hours=1),
    catchup=False,
) as dag:
    
    ingest = PythonOperator(
        task_id='ingest',
        python_callable=ingest_data,
    )
    
    transform = PythonOperator(
        task_id='transform',
        python_callable=transform_data,
    )
    
    load = PythonOperator(
        task_id='load',
        python_callable=load_data,
    )
    
    ingest >> transform >> load

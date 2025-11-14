"""
Example DAG đơn giản để test Airflow setup.

DAG này chỉ in một message, dùng để kiểm tra Airflow đã hoạt động đúng chưa.
"""

from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    'example_simple_dag',
    default_args=default_args,
    description='Example simple DAG để test Airflow',
    schedule_interval=timedelta(days=1),
    catchup=False,
    tags=['example', 'test'],
) as dag:

    def print_hello():
        """Print hello message"""
        print("Hello from Airflow!")
        return "Hello World"

    hello_task = PythonOperator(
        task_id='print_hello',
        python_callable=print_hello,
    )

    bash_task = BashOperator(
        task_id='bash_hello',
        bash_command='echo "Hello from Bash!"',
    )

    hello_task >> bash_task


"""
Example DAG để chạy dbt project với Cosmos.

Đây là template để tạo DAG cho dbt project mới.
Thay đổi các giá trị sau:
- dag_id: Tên DAG
- project_path: Đường dẫn đến dbt project
- profile_name: Tên profile trong dbt profiles.yml
- tags: Tags cho DAG
- description: Mô tả DAG
"""

from datetime import timedelta
from airflow.utils.dates import days_ago
from airflow import DAG
from cosmos import DbtDag, ProjectConfig, ProfileConfig
from cosmos.profiles import PostgresUserPasswordProfileMapping
from airflow.models import Variable

# Lấy connection ID từ Airflow Variables
# Cấu hình trong Airflow UI: Admin > Variables
# Key: DWH_CONNECTION, Value: postgres_default (hoặc connection ID của bạn)
DWH_CONNECTION = Variable.get('DWH_CONNECTION', default_var='postgres_default')

# Đường dẫn đến dbt project
# Thay 'my_project' bằng tên dbt project của bạn
project_path = '/opt/airflow/dbt/projects/my_project'

default_args = {
    'owner': 'airflow',
    'start_date': days_ago(1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    'execution_timeout': timedelta(minutes=30),
}

# Cấu hình dbt profile
profile_config = ProfileConfig(
    profile_name='my_project',  # Thay bằng tên profile trong profiles.yml
    target_name='dev',  # hoặc 'prod'
    profile_mapping=PostgresUserPasswordProfileMapping(
        conn_id=DWH_CONNECTION,
        profile_args={
            'schema': 'public',  # Schema mặc định
            'threads': 2,
            'connect_timeout': 1800,
            'keepalives_idle': 0,
        },
    ),
)

# Tạo DAG với Cosmos DbtDag
dbt_dag = DbtDag(
    project_config=ProjectConfig(project_path),
    profile_config=profile_config,
    default_args=default_args,
    schedule_interval=None,  # Hoặc cron expression: '0 0 * * *'
    catchup=False,
    max_active_runs=1,
    dag_id='dbt_my_project_transform',
    tags=['dbt', 'transform', 'example'],
    description='Example DAG để chạy dbt transformations',
)


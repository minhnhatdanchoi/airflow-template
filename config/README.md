# Config

Thư mục này chứa các file cấu hình Airflow tùy chỉnh.

Nếu cần override airflow.cfg, đặt file config ở đây và uncomment dòng trong docker-compose.yaml:
```yaml
AIRFLOW_CONFIG: '/opt/airflow/config/airflow.cfg'
```


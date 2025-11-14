# Quick Start Guide

Hướng dẫn nhanh để bắt đầu với Airflow-DBT template.

## Bước 1: Tạo file .env

Tạo file `.env` từ template (hoặc tạo thủ công):

```bash
# Windows PowerShell
Copy-Item .env.example .env

# Linux/Mac
cp .env.example .env
```

## Bước 2: Tạo Fernet Key và Secret Key

Mở Python và chạy:

```python
# Tạo Fernet Key
from cryptography.fernet import Fernet
print("AIRFLOW__CORE__FERNET_KEY=" + Fernet.generate_key().decode())

# Tạo Secret Key
import secrets
print("AIRFLOW__WEBSERVER__SECRET_KEY=" + secrets.token_hex(32))
```

Copy các giá trị vào file `.env`.

## Bước 3: Cấu hình Airflow UID (Linux/Mac)

```bash
echo -e "AIRFLOW_UID=$(id -u)" >> .env
```

Trên Windows, thường dùng `AIRFLOW_UID=50000`.

## Bước 4: Khởi tạo Airflow

```bash
docker-compose up airflow-init
```

## Bước 5: Khởi động services

```bash
docker-compose up -d
```

## Bước 6: Truy cập Airflow UI

Mở trình duyệt: http://localhost:8080

- Username: `airflow`
- Password: `airflow`

## Bước 7: Cấu hình DBT Profile

1. Copy `dbt/.dbt/profiles.yml.example` thành `dbt/.dbt/profiles.yml`
2. Cấu hình connection đến database của bạn

## Bước 8: Tạo DBT Project mới

1. Tạo thư mục trong `dbt/projects/my_project/`
2. Copy cấu trúc từ `dbt/projects/example_project/`
3. Chỉnh sửa `dbt_project.yml` với tên project của bạn
4. Tạo DAG trong `dags/` dựa trên `dags/example_dbt_dag.py`

## Bước 9: Cấu hình Airflow Variables và Connections

Trong Airflow UI:
- **Variables**: Admin > Variables
  - `DWH_CONNECTION`: Connection ID đến database (ví dụ: `postgres_default`)
  
- **Connections**: Admin > Connections
  - Tạo PostgreSQL connection cho dbt
  - Connection ID phải khớp với `DWH_CONNECTION` variable

## Xong!

Bây giờ bạn có thể:
- Tạo DAGs mới trong `dags/`
- Tạo dbt models trong `dbt/projects/`
- Chạy và monitor workflows trong Airflow UI

Xem `README.md` để biết thêm chi tiết.


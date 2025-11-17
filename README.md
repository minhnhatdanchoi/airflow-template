# Airflow-DBT Template

Template tái sử dụng để triển khai Apache Airflow với DBT cho các dự án mới.

## Cấu trúc thư mục

```
.
├── dags/              # Chứa các DAG files của Airflow
├── dbt/               # Chứa các dbt projects
│   ├── projects/      # Các dbt projects
│   └── .dbt/          # DBT profiles và cache
├── plugins/           # Airflow plugins
├── config/            # Airflow config files
├── scripts/           # Utility scripts
├── logs/              # Airflow logs
├── docker-compose.yaml
├── Dockerfile
└── requirements.txt
```

## Yêu cầu

- Docker và Docker Compose
- Python 3.8+ (nếu chạy local)

## Cài đặt

### 1. Clone hoặc copy template này vào dự án mới

### 2. Tạo file `.env` từ `.env.example`

```bash
cp .env.example .env
```

### 3. Cấu hình các biến môi trường trong `.env`

- `AIRFLOW_UID`: User ID (thường là 50000)
- Trên Linux/Ubuntu, chạy `id -u` để lấy giá trị chính xác rồi cập nhật vào `.env`
- `AIRFLOW__CORE__FERNET_KEY`: Fernet key để mã hóa connections, chạy code py dưới
- `AIRFLOW__WEBSERVER__SECRET_KEY`: Secret key cho webserver

Để tạo Fernet key:
```python
from cryptography.fernet import Fernet
Fernet.generate_key().decode()
```

### 4. Khởi tạo Airflow

```bash
docker-compose up airflow-init
```

### 5. Khởi động các services

```bash
docker-compose up -d
```

### 6. Truy cập Airflow UI

Mở trình duyệt và truy cập: http://localhost:8080

- Username: `airflow`
- Password: `airflow`

## Tạo DBT Project mới

### 1. Tạo dbt project

```bash
docker-compose run --rm airflow-worker dbt init my_project
```

Hoặc tạo thủ công trong `dbt/projects/my_project/`

### 2. Cấu hình dbt profile

File profile được lưu tại `dbt/.dbt/profiles.yml`. Cấu hình connection đến database của bạn.

### 3. Tạo DAG cho dbt project

Xem ví dụ trong `dags/example_dbt_dag.py`

## Cấu hình Airflow Variables

Trong Airflow UI, vào Admin > Variables để cấu hình:
- `DWH_CONNECTION`: Connection ID đến data warehouse
- Các biến khác theo nhu cầu dự án

## Cấu hình Airflow Connections

Trong Airflow UI, vào Admin > Connections để cấu hình:
- PostgreSQL connection cho dbt
- Các connections khác (S3, databases, APIs, etc.)

## Development

### Xem logs

```bash
docker-compose logs -f airflow-scheduler
docker-compose logs -f airflow-worker
```

### Chạy DAG thủ công

```bash
docker-compose run --rm airflow-cli dags trigger <dag_id>
```

### Test dbt project

```bash
docker-compose run --rm airflow-worker dbt test --project-dir /opt/airflow/dbt/projects/my_project
```

### Dừng services

```bash
docker-compose down
```

### Dừng và xóa volumes (xóa dữ liệu)

```bash
docker-compose down -v
```

## Customization

### Thêm Python packages

Thêm vào `requirements.txt` và rebuild image:

```bash
docker-compose build
docker-compose up -d
```

### Thêm Airflow plugins

Đặt các plugin trong thư mục `plugins/`

### Cấu hình Airflow

Chỉnh sửa `docker-compose.yaml` hoặc thêm file config trong `config/`

## Troubleshooting

### Permission issues

Đảm bảo `AIRFLOW_UID` trong `.env` khớp với user ID của bạn:

```bash
echo -e "AIRFLOW_UID=$(id -u)" > .env
```

### Port conflicts

Nếu port 8080 đã được sử dụng, thay đổi trong `docker-compose.yaml`:

```yaml
ports:
  - "8081:8080"  # Thay 8081 bằng port khác
```

## License

Apache License 2.0


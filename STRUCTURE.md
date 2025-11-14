# Cấu trúc Template Airflow-DBT

## Tổng quan

Template này cung cấp một cấu trúc sẵn sàng để triển khai Apache Airflow với DBT cho các dự án mới.

## Cấu trúc thư mục

```
.
├── dags/                          # Airflow DAGs
│   ├── __init__.py
│   ├── example_dbt_dag.py        # Example DAG cho dbt project
│   └── example_simple_dag.py     # Example DAG đơn giản để test
│
├── dbt/                           # DBT projects và config
│   ├── .dbt/                      # DBT profiles (không commit)
│   │   └── profiles.yml.example   # Template cho profiles.yml
│   ├── packages.yml               # DBT packages dependencies
│   └── projects/                  # Các dbt projects
│       └── example_project/       # Example dbt project
│           ├── dbt_project.yml
│           └── models/
│               └── example_model.sql
│
├── plugins/                       # Airflow custom plugins
│   └── __init__.py
│
├── config/                        # Airflow config files tùy chỉnh
│   └── README.md
│
├── scripts/                       # Utility scripts
│   └── README.md
│
├── logs/                          # Airflow logs (không commit)
│
├── docker-compose.yaml            # Docker Compose configuration
├── Dockerfile                     # Custom Airflow image
├── requirements.txt               # Python dependencies
├── .env.example                   # Template cho environment variables
├── .gitignore                     # Git ignore rules
├── README.md                      # Hướng dẫn chi tiết
├── QUICKSTART.md                  # Hướng dẫn nhanh
└── STRUCTURE.md                   # File này

```

## Các file quan trọng

### Docker & Configuration
- **docker-compose.yaml**: Cấu hình Airflow cluster với PostgreSQL, Redis, và các services
- **Dockerfile**: Custom Airflow image với các dependencies
- **requirements.txt**: Python packages cần thiết
- **.env.example**: Template cho environment variables

### DAGs
- **example_dbt_dag.py**: Template DAG để chạy dbt project với Cosmos
- **example_simple_dag.py**: DAG đơn giản để test Airflow setup

### DBT
- **dbt/projects/example_project/**: Example dbt project structure
- **dbt/.dbt/profiles.yml.example**: Template cho dbt profiles configuration
- **dbt/packages.yml**: DBT packages dependencies

## Workflow sử dụng

1. **Setup ban đầu**: Làm theo QUICKSTART.md
2. **Tạo dbt project mới**: Copy example_project và chỉnh sửa
3. **Tạo DAG mới**: Copy example_dbt_dag.py và cấu hình
4. **Cấu hình connections**: Setup trong Airflow UI
5. **Deploy**: Chạy `docker-compose up -d`

## Customization

### Thêm Python packages
Thêm vào `requirements.txt` và rebuild:
```bash
docker-compose build
docker-compose up -d
```

### Thêm DBT packages
Thêm vào `dbt/packages.yml` và chạy:
```bash
docker-compose run --rm airflow-worker dbt deps --project-dir /opt/airflow/dbt/projects/my_project
```

### Thay đổi timezone
Sửa trong `docker-compose.yaml`:
```yaml
AIRFLOW__CORE__DEFAULT_TIMEZONE: 'Asia/Ho_Chi_Minh'
TZ: Asia/Ho_Chi_Minh
```

## Notes

- Tất cả logs và cache files đã được thêm vào `.gitignore`
- DBT profiles.yml không được commit (chứa credentials)
- Có thể xóa example files sau khi setup xong
- Timezone mặc định là UTC, có thể thay đổi trong docker-compose.yaml


-- Example dbt model
-- Đây là file mẫu, xóa và tạo models của bạn

{{
  config(
    materialized='view'
  )
}}

select
  1 as id,
  'Hello' as message,
  current_timestamp as created_at


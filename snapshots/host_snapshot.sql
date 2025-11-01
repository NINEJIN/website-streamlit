{% snapshot host_snapshot %}
{{
  config(
    target_schema='silver',
    unique_key='host_id',
    strategy='timestamp',
    updated_at='host_since'   -- 若有更合理的更新时间戳字段可替换
  )
}}
select
  host_id,
  host_name,
  host_since,
  host_is_superhost,
  host_neighbourhood
from {{ ref('stg_host') }}
{% endsnapshot %}

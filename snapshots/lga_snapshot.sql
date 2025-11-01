{% snapshot lga_snapshot %}
{{
  config(
    target_schema='silver',
    unique_key='lga_name',
    strategy='check',
    check_cols=['lga_name']
  )
}}
select
  lga_name
from {{ ref('stg_lga') }}
{% endsnapshot %}

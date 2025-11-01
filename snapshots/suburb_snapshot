{% snapshot suburb_snapshot %}
{{
  config(
    target_schema='silver',
    unique_key='suburb_name',
    strategy='check',
    check_cols=['suburb_name','lga_name']
  )
}}
select
  suburb_name,
  lga_name
from {{ ref('stg_suburb') }}
{% endsnapshot %}

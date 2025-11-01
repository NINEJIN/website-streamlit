-- Suburb -> LGA 对照（SCD2）
select
  suburb_name,
  lga_name,
  dbt_valid_from as valid_from,
  dbt_valid_to   as valid_to,
  case when dbt_valid_to is null then true else false end as is_current
from {{ ref('suburb_snapshot') }}

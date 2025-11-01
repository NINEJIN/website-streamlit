-- 如果做了 snapshot
select
  lga_name,
  dbt_valid_from as valid_from,
  dbt_valid_to   as valid_to,
  case when dbt_valid_to is null then true else false end as is_current
from {{ ref('lga_snapshot') }}

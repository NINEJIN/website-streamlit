select
  host_id,
  host_name,
  host_neighbourhood,
  host_is_superhost,
  host_since,
  dbt_valid_from  as valid_from,
  dbt_valid_to    as valid_to,
  case when dbt_valid_to is null then true else false end as is_current
from {{ ref('host_snapshot') }}

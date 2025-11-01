select distinct
  host_id,
  host_name,
  host_since,
  host_is_superhost,
  host_neighbourhood
from {{ ref('stg_airbnb') }}
where host_id is not null

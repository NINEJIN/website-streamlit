with m as (
  select
    trim(lga_name)    as lga_name,
    trim(suburb_name) as suburb_name
  from {{ source('bronze','lga_suburb_mapping') }}
)
select * from m

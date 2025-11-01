select * from {{ source('bronze','census_g02_raw') }}

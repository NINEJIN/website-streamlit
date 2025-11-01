with base as (
  select
    listing_id,
    host_id,
    listing_neighbourhood,
    property_type,
    room_type,
    accommodates,
    price,
    has_availability,
    availability_30,
    review_scores_rating,
    date_trunc('month', scraped_date)::date as month_start
  from {{ ref('stg_airbnb') }}
  where listing_id is not null
)
select * from base

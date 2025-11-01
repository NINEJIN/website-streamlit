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
    month_start
  from {{ ref('stg_listing') }}
),
facts as (
  select
    listing_id,
    host_id,
    listing_neighbourhood,
    property_type,
    room_type,
    accommodates,
    month_start,

    -- metrics at row-level
    case when has_availability='t' then 1 else 0 end as is_active,
    greatest(0, 30 - coalesce(availability_30,0))    as stays,
    price,
    review_scores_rating
  from base
)
select * from facts

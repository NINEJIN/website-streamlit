with base as (
  select
    -- ids
    nullif(listing_id,'') as listing_id,
    nullif(host_id,'')    as host_id,
    host_name,

    -- dates
    /* scraped_date/host_since 源是 text；尽力解析为 date 或 timestamp */
    try_cast(scraped_date as date)      as scraped_date,
    try_cast(host_since  as date)       as host_since,

    -- flags
    lower(coalesce(host_is_superhost,''))      as host_is_superhost, -- 't'/'f'
    lower(coalesce(has_availability,''))       as has_availability,  -- 't'/'f'

    -- geo / categories
    trim(host_neighbourhood)    as host_neighbourhood,
    trim(listing_neighbourhood) as listing_neighbourhood,
    trim(property_type)         as property_type,
    trim(room_type)             as room_type,

    -- numerics
    nullif(accommodates,'')::int                    as accommodates,
    replace(replace(price,'$',''),',','')::numeric  as price,
    nullif(availability_30,'')::int                 as availability_30,
    nullif(number_of_reviews,'')::int               as number_of_reviews,
    nullif(review_scores_rating,'')::numeric        as review_scores_rating

  from {{ source('bronze','airbnb_raw') }}
),
norm as (
  select
    listing_id, host_id, host_name,
    scraped_date, host_since,
    case when host_is_superhost in ('t','true','1') then 't' else 'f' end as host_is_superhost,
    case when has_availability  in ('t','true','1') then 't' else 'f' end as has_availability,
    host_neighbourhood, listing_neighbourhood,
    property_type, room_type,
    accommodates, price, availability_30, number_of_reviews, review_scores_rating
  from base
)
select * from norm

with f as (
  select
    property_type, room_type, accommodates,
    month_start, listing_id, host_id, is_active, stays, price, review_scores_rating
  from {{ ref('fact_listing_monthly') }}
),
agg as (
  select
    property_type, room_type, accommodates, month_start,
    count(distinct listing_id)                                   as total_listings,
    sum(is_active)                                               as active_listings,
    min(case when is_active=1 then price end)                    as min_price_active,
    max(case when is_active=1 then price end)                    as max_price_active,
    percentile_cont(0.5) within group (order by case when is_active=1 then price end) as median_price_active,
    avg(case when is_active=1 then price end)                    as avg_price_active,
    count(distinct host_id)                                      as distinct_hosts,
    sum(case when is_active=1 then stays*price else 0 end)       as est_revenue_sum_active,
    avg(case when is_active=1 then review_scores_rating end)     as avg_rating_active
  from f
  group by 1,2,3,4
),
host_month as (
  select
    f.property_type, f.room_type, f.accommodates, f.month_start, f.host_id,
    max(case when h.host_is_superhost='t' then 1 else 0 end) as is_superhost_any
  from {{ ref('fact_listing_monthly') }} f
  left join {{ ref('dim_host') }} h
    on f.host_id = h.host_id
   and {{ scd2_asof_join('f.month_start','h.valid_from','h.valid_to') }}
  group by 1,2,3,4,5
),
host_agg as (
  select
    property_type, room_type, accommodates, month_start,
    count(distinct host_id) as hosts_total,
    sum(is_superhost_any)   as hosts_super
  from host_month
  group by 1,2,3,4
),
final as (
  select
    a.property_type, a.room_type, a.accommodates, a.month_start,
    {{ active_listing_rate('a.active_listings','a.total_listings') }}    as active_listing_rate,
    a.min_price_active, a.max_price_active, a.median_price_active, a.avg_price_active,
    a.distinct_hosts,
    {{ superhost_rate('h.hosts_super','h.hosts_total') }}                as superhost_rate,
    a.avg_rating_active,
    {{ pct_change('a.active_listings','lag(a.active_listings) over (partition by a.property_type, a.room_type, a.accommodates order by a.month_start)') }} as pct_change_active,
    {{ pct_change('(a.total_listings - a.active_listings)','lag(a.total_listings - a.active_listings) over (partition by a.property_type, a.room_type, a.accommodates order by a.month_start)') }} as pct_change_inactive,
    sum(a.est_revenue_sum_active) over (partition by a.property_type, a.room_type, a.accommodates, a.month_start) as total_est_revenue_active_sum,
    case when a.active_listings>0 then a.est_revenue_sum_active::numeric / a.active_listings else null end as avg_est_revenue_per_active
  from agg a
  left join host_agg h
    on a.property_type=h.property_type and a.room_type=h.room_type and a.accommodates=h.accommodates and a.month_start=h.month_start
)
select
  property_type, room_type, accommodates, month_start,
  active_listing_rate,
  min_price_active, max_price_active, median_price_active, avg_price_active,
  distinct_hosts, superhost_rate, avg_rating_active,
  pct_change_active, pct_change_inactive,
  total_est_revenue_active_sum as total_number_of_stays, -- 如需纯“次数”请改 sum(stays)
  avg_est_revenue_per_active
from final
order by property_type, room_type, accommodates, month_start;

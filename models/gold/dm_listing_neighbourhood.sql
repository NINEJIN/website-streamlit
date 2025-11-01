with f as (
  select
    listing_neighbourhood,
    month_start,
    listing_id,
    host_id,
    is_active,
    stays,
    price,
    review_scores_rating
  from {{ ref('fact_listing_monthly') }}
),
agg as (
  select
    listing_neighbourhood,
    month_start,
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
  group by 1,2
),
host_flags as (
  -- 需要把 host 维（SCD2）按月对齐，计算 superhost
  select
    h.host_id, h.host_is_superhost, h.valid_from, h.valid_to
  from {{ ref('dim_host') }} h
),
host_month as (
  select
    f.listing_neighbourhood,
    f.month_start,
    f.host_id,
    max(case when h.host_is_superhost='t' then 1 else 0 end) as is_superhost_any
  from {{ ref('fact_listing_monthly') }} f
  left join {{ ref('dim_host') }} h
    on f.host_id = h.host_id
   and {{ scd2_asof_join('f.month_start','h.valid_from','h.valid_to') }}
  group by 1,2,3
),
host_agg as (
  select
    listing_neighbourhood,
    month_start,
    count(distinct host_id)                                  as hosts_total,
    sum(is_superhost_any)                                    as hosts_super
  from host_month
  group by 1,2
),
final as (
  select
    a.listing_neighbourhood,
    a.month_start,
    {{ active_listing_rate('a.active_listings','a.total_listings') }}    as active_listing_rate,
    a.min_price_active,
    a.max_price_active,
    a.median_price_active,
    a.avg_price_active,
    a.distinct_hosts,
    {{ superhost_rate('h.hosts_super','h.hosts_total') }}                as superhost_rate,
    a.avg_rating_active,
    -- MoM 变化（同 neighbourhood 上一月对比）
    lag(a.active_listings) over (partition by a.listing_neighbourhood order by a.month_start) as prev_active,
    lag(a.total_listings)  over (partition by a.listing_neighbourhood order by a.month_start) as prev_total,
    {{ pct_change('a.active_listings','lag(a.active_listings) over (partition by a.listing_neighbourhood order by a.month_start)') }} as pct_change_active,
    {{ pct_change('(a.total_listings - a.active_listings)','lag(a.total_listings - a.active_listings) over (partition by a.listing_neighbourhood order by a.month_start)') }} as pct_change_inactive,
    a.est_revenue_sum_active                                         as total_stays_revenue_active_sum,
    -- 平均每个活跃 listing 的估计营收
    case when a.active_listings>0 then a.est_revenue_sum_active::numeric / a.active_listings else null end as avg_est_revenue_per_active
  from agg a
  left join host_agg h
    on a.listing_neighbourhood=h.listing_neighbourhood and a.month_start=h.month_start
)
select
  listing_neighbourhood,
  month_start,
  active_listing_rate,
  min_price_active, max_price_active, median_price_active, avg_price_active,
  distinct_hosts,
  superhost_rate,
  avg_rating_active,
  pct_change_active,
  pct_change_inactive,
  total_stays_revenue_active_sum as total_number_of_stays, -- 若你要“总入住次数”，可把 stays 求和另算；这里保留 revenue_sum 字段名可自行改名
  avg_est_revenue_per_active
from final
order by listing_neighbourhood, month_start;

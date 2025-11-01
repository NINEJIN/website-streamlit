with host_dim as (
  select host_id, host_neighbourhood, valid_from, valid_to from {{ ref('dim_host') }}
),
-- host_neighbourhood 映射到 LGA 名称（按名字对齐或你有专门的 host->suburb->lga 映射）
lga_dim as (
  select suburb_name, lga_name, valid_from, valid_to from {{ ref('dim_suburb') }}
),
f as (
  select
    fl.host_id, fl.month_start, fl.is_active, fl.stays, fl.price
  from {{ ref('fact_listing_monthly') }} fl
),
-- 把 host 的 neighbourhood 按月对齐（SCD2）
host_asof as (
  select
    f.host_id, f.month_start,
    h.host_neighbourhood
  from f
  left join host_dim h
    on f.host_id = h.host_id
   and {{ scd2_asof_join('f.month_start','h.valid_from','h.valid_to') }}
),
-- 简化做法：如果 host_neighbourhood 与 suburb_name 一致，则可直接 join；否则需你提供映射表
mapped as (
  select
    ha.host_id, ha.month_start,
    coalesce(s.lga_name, ha.host_neighbourhood) as host_neighbourhood_lga
  from host_asof ha
  left join lga_dim s
    on lower(ha.host_neighbourhood) = lower(s.suburb_name)
   and {{ scd2_asof_join('ha.month_start','s.valid_from','s.valid_to') }}
),
agg as (
  select
    m.host_neighbourhood_lga,
    f.month_start,
    count(distinct f.host_id)                                        as distinct_hosts,
    sum(case when f.is_active=1 then f.stays*f.price else 0 end)     as est_revenue_total_active,
    -- 人均（distinct host）
    case when count(distinct f.host_id)>0
         then sum(case when f.is_active=1 then f.stays*f.price else 0 end)::numeric / count(distinct f.host_id)
         else null end                                                as est_revenue_per_host
  from f
  join mapped m on f.host_id=m.host_id and f.month_start=m.month_start
  group by 1,2
)
select
  host_neighbourhood_lga,
  month_start,
  distinct_hosts,
  est_revenue_total_active as avg_estimated_revenue_per_active_listings, -- 若需“Average Estimated Revenue per active listings”，可另外除以活跃 listing 数
  est_revenue_per_host
from agg
order by host_neighbourhood_lga, month_start;

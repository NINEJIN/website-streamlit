{% macro scd2_asof_join(fact_ts, dim_valid_from, dim_valid_to='dbt_valid_to') %}
-- 生成 SCD2 时间点匹配的 join 条件：(valid_from <= fact_ts < valid_to/null)
{{ return("(" ~ dim_valid_from ~ " <= " ~ fact_ts ~ " AND (" ~ dim_valid_to ~ " IS NULL OR " ~ fact_ts ~ " < " ~ dim_valid_to ~ "))") }}
{% endmacro %}

{% macro active_listing_rate(active_count, total_count) %}
    (nullif({{ active_count }},0)::numeric / nullif({{ total_count }},0)) * 100
{% endmacro %}

{% macro superhost_rate(superhost_hosts, total_hosts) %}
    (nullif({{ superhost_hosts }},0)::numeric / nullif({{ total_hosts }},0)) * 100
{% endmacro %}

{% macro pct_change(curr_val, prev_val) %}
    ( ({{ curr_val }} - {{ prev_val }}) / nullif({{ prev_val }},0)::numeric ) * 100
{% endmacro %}

{% macro est_revenue_per_active(stays_sum, price_sum, active_count) %}
    -- 若逐行 revenue=stays*price，建议先 sum(stays*price) 再 / active_count
    (nullif({{ stays_sum }},0)::numeric / nullif({{ active_count }},0))
{% endmacro %}

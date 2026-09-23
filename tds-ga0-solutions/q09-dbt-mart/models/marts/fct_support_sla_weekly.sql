{{ config(
    materialized='table',
    tags=['support', 'operations'],
    meta={'owner': 'orbit_ops', 'freshness': 'daily', 'freshness_warn_after_hours': 24}
) }}

with tickets as (
    select
        ticket_id,
        contact_id,
        coalesce(channel, 'unknown') as channel,
        cast(created_at as date) as created_date,
        created_at,
        resolved_at,
        coalesce(sla_target_hours, 24) as sla_target_hours
    from {{ ref('stg_support_tickets') }}
    where cast(created_at as date) >= current_date - interval '45 day'
),

scored as (
    select
        *,
        date_trunc('week', created_date) as week_start,
        coalesce(datediff('hour', created_at, resolved_at), 0) as resolution_hours,
        case
            when resolved_at is null then 1
            when datediff('hour', created_at, resolved_at) > sla_target_hours then 1
            else 0
        end as is_sla_breach
    from tickets
)

select
    week_start,
    channel,
    count(distinct ticket_id) as total_tickets,
    count(distinct contact_id) as unique_contacts,
    coalesce(sum(is_sla_breach), 0) as sla_breaches,
    round(100.0 * coalesce(sum(is_sla_breach), 0) / nullif(count(distinct ticket_id), 0), 2) as sla_breach_pct,
    round(coalesce(avg(resolution_hours), 0), 2) as avg_resolution_hours
from scored
group by week_start, channel
order by week_start, channel

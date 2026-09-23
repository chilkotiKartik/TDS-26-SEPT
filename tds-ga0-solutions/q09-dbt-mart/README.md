# Q9 · dbt: Operations performance mart (1 mark)

## Question
Orbit Ops wants a dbt **mart model** for the *support* dashboards: **SLA breaches**, **weekly** grain,
**last 45 days**. Must use `{{ config() }}`, `{{ ref() }}`, a date filter, `date_trunc`, domain terms like
"contact", NULL handling, and be ordered for BI.
*(focus metric, grain and window are personalised)*

## Answer — [`models/marts/fct_support_sla_weekly.sql`](models/marts/fct_support_sla_weekly.sql)
- `config()` → `materialized='table'` + freshness metadata in `meta`
- CTE `tickets` reads `{{ ref('stg_support_tickets') }}` and filters `>= current_date - interval '45 day'`
- CTE `scored` flags each ticket: `case when resolved later than SLA target (or never resolved) then 1 else 0 end`
- Final select: `date_trunc('week', …)` × channel with tickets, **unique contacts**, SLA breaches, breach %, avg resolution hours
- `coalesce` everywhere + `nullif` to avoid divide-by-zero, `order by week_start`

## Steps
1. Copy the SQL into the textarea → **Check**.
2. If your variant is different (e.g. *daily* / *on-time %* / *30 days*), change:
   - `date_trunc('week', …)` → `date_trunc('day', …)`
   - the metric `case` expression (the error message tells you which keywords it wants)
   - the interval.

## Gotchas (from the validator)
- The date filter regex is **one line**: `where … date … >=` — and `date` must be a standalone word.
  `where created_date >= …` fails (`_date` isn't a word boundary); `where cast(created_at as date) >= …` passes.
- It literally checks for `{{ config(`, `{{ ref(`, `group by`, `order by`, `coalesce`, and the domain word (here **contact**).

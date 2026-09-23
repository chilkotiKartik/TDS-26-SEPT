# Q2 · Build a Binary Eval Rubric (1 mark)

## Question
Write exactly **5 YES/NO checks** that an LLM judge can use to grade SQL query quality. Each check is run against
20 hidden examples; a check passes if its correlation with the ground-truth label is **> 0.7** and it isn't
degenerate (always YES / always NO). Need **4 of 5** to pass. Uses your AI Pipe token (~100 calls).

Examples given:
- **GOOD** – CTEs (`WITH clean_orders AS …`), `COALESCE`, filter, `GROUP BY`, `ORDER BY`
- **MEDIOCRE** – single `SELECT … GROUP BY` without CTEs
- **POOR** – `SELECT * FROM orders;`

## Answer — [`checks.txt`](checks.txt)
```
Does the query start with a WITH clause that defines a common table expression (CTE)?
Does the query use COALESCE, IFNULL, or NVL to handle NULL values?
Does the query use an aggregate function such as SUM, COUNT, AVG, MIN, or MAX?
Does the final SELECT read FROM a named CTE defined earlier in the query rather than directly from a raw table?
Does the query contain two or more SELECT keywords, such as a CTE followed by a final SELECT?
```

## Why these work
Looking at what separates good from bad SQL in this task, the "good" pattern is very consistent:
**CTE → NULL handling → aggregation**. The bad ones are flat `SELECT`s with no CTE.

| Check | Good examples YES | Poor examples YES | Expected corr |
|-------|:---:|:---:|:---:|
| Starts with WITH / CTE | 10/10 | 0/10 | ≈ 1.0 |
| COALESCE / IFNULL | 9/10 | 0/10 | ≈ 0.9 |
| Aggregate function | 9/10 | 0/10 | ≈ 0.9 |
| Final SELECT reads from CTE | 10/10 | 0/10 | ≈ 1.0 |
| 2+ SELECT keywords | 10/10 | 0/10 | ≈ 1.0 |

## Steps
1. Paste the five lines (one per line, each ending with `?`, each ≥ 24 chars, no duplicates).
2. Click **Check** → paste your AI Pipe token when prompted (get it from <https://aipipe.org/login>).
3. Wait ~1 minute for ~100 judge calls → **Correct** → **Save**.

## Tips for writing good binary checks
- Make every check answerable **from the output alone** — no "is this efficient?".
- Prefer **structural** facts (keywords present/absent) over style opinions.
- Avoid checks that are true for almost everything (degenerate → auto-fail).

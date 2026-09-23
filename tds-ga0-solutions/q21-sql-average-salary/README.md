# Q21 · SQL: Average salary by department (0.5 marks)

## Question
SQLite table `employees(employee_id, name, department, salary)`. Average salary per department,
**rounded to the nearest whole number**, ordered by department name.

## Answer — [`query.sql`](query.sql) ✅
```sql
SELECT department, ROUND(AVG(salary)) AS average_salary
FROM employees
GROUP BY department
ORDER BY department;
```

## Notes
- `GROUP BY` gives one row per department; without it `AVG` collapses the whole table into one number.
- In SQLite `ROUND(x)` = round to 0 decimals (returns a float like `78123.0`, which the checker accepts).

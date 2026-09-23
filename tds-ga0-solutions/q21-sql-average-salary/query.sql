SELECT department, ROUND(AVG(salary)) AS average_salary
FROM employees
GROUP BY department
ORDER BY department;

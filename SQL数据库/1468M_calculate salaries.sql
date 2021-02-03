-- 查询各公司员工的税后工资工资，四舍五入
WITH

tmp AS (
SELECT
	company_id,
	employee_id,
	employee_name,
	salary, 
	MAX(salary) OVER(PARTITION BY company_id) AS max_sal
FROM Salaries   
)

SELECT 
company_id,
employee_id,
employee_name,
CASE 
	WHEN max_sal < 1000  THEN ROUND(salary) 
	WHEN max_sal BETWEEN 1000 AND 10000 THEN ROUND(salary * (1-0.24))
	ELSE ROUND(salary * (1-0.49))
END AS salary
FROM tmp;
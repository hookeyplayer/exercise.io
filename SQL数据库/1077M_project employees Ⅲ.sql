-- 2个表，项目和员工
-- 查询每个项目中所有最有经验的员工
WITH t AS (
SELECT a.project_id, a.employee_id, RANK() OVER(PARTITION BY a.project_id ORDER BY b.experience_years DESC) AS exp
FROM Project AS a
LEFT JOIN Employee AS b
ON a.employee_id = b.employee_id
)

SELECT project_id, employee_id
FROM t
WHERE exp = 1;
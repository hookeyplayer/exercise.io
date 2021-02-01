-- 2个表，项目和员工
-- 查询员工最多的项目
-- 姗姗
SELECT project_id FROM Project
GROUP BY project_id
HAVING COUNT(employee_id) >= 
ALL(SELECT COUNT(employee_id) OVER(PARTITION BY project_id) FROM Project);


-- 法二
WITH 
t AS (
	SELECT COUNT(*) AS c, project_id 
	FROM project 
	GROUP BY project_id
)

SELECT project_id FROM t WHERE t.c = (SELECT MAX(c) FROM t);


-- 法三
SELECT project_id
FROM (
	SELECT project_id,
	RANK() OVER (ORDER BY COUNT(employee_id) DESC) AS r
	FROM Project
	GROUP BY project_id 
) AS a
WHERE r = 1;
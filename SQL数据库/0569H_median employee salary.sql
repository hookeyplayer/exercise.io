-- 找出各公司薪水的中位数
WITH t AS(
SELECT *, 
ROW_NUMBER() OVER(PARTITION BY Company ORDER BY Salary) AS num
FROM Employee),

t1 AS(
SELECT Company AS company_id, 
MAX(num)/2 AS criteria_1, 
MAX(num)/2+1 AS criteria_2, 
ROUND(MAX(num)/2) AS criteria_3
FROM t
GROUP BY Company),

t2 AS(
SELECT * FROM t LEFT JOIN t1 ON t.Company = t1.company_id)

SELECT Id,Company,Salary
FROM t2
WHERE num = criteria_1
OR num = criteria_2
OR num = criteria_3;
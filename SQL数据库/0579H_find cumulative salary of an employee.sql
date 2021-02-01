-- 查询出每个员工三个月的累积工资，其中不包含最近一个月，且按照员工id升序排列，月份降序排列
-- 法一
SELECT E1.id, E1.month,
(IFNULL(E1.salary, 0) + IFNULL(E2.salary, 0) + IFNULL(E3.salary, 0)) AS Salary
FROM
(
SELECT id, MAX(month) AS month FROM Employee
GROUP BY id
HAVING COUNT(*) > 1
) AS maxmonth
LEFT JOIN Employee AS E1 
ON (maxmonth.id = E1.id AND maxmonth.month > E1.month)
LEFT JOIN Employee AS E2 
ON (E2.id = E1.id AND E2.month = E1.month - 1)
LEFT JOIN Employee AS E3 
ON (E3.id = E1.id AND E3.month = E1.month - 2)
ORDER BY id ASC, month DESC;


-- 法二
WITH s AS
(SELECT Id AS id, Month AS month, Salary,
Sum(Salary) OVER (PARTITION BY Id ORDER BY Month) as SumSal,
ROW_NUMBER() OVER (PARTITION BY id ORDER BY id ASC, month DESC) rn
FROM Employee)

SELECT Id,Month,SumSal as Salary
FROM s
WHERE rn > 1;
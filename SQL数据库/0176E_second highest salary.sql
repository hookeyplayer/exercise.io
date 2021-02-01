-- 查询收入第二高的员工薪水，若无则null
-- 1 子查询的两种
-- 必须加 DISTINCT, 否则当不止一个人有第二高薪水的时候会返回多个值
SELECT 
(SELECT DISTINCT Salary
FROM Employee
ORDER BY Salary DESC
LIMIT 1 OFFSET 1)
As SecondHighestSalary;

-- 姗姗
SELECT (
 SELECT 
 DISTINCT a.Salary 
 FROM Employee AS a
 JOIN Employee AS b
 ON a.Salary < b.Salary
 GROUP BY  a.Id
 HAVING COUNT(a.Id) = 1) 
AS SecondHighestSalary;

-- 2
SELECT MAX(Salary) AS SecondHighestSalary FROM Employee
WHERE Salary NOT IN (SELECT MAX(Salary) FROM Employee);

-- 3
SELECT MAX(Salary) AS SecondHighestSalary FROM Employee
WHERE Salary < (SELECT MAX(Salary) FROM Employee);

-- 4
SELECT MAX(CASE WHEN rnk = 2 THEN Salary ELSE null END) AS SecondHighestSalary
FROM (
SELECT Salary, ROW_NUMBER() OVER(ORDER BY Salary DESC) AS rnk FROM Employee
) AS tmp
 

-- 其他
-- 查询最高（子查询）
-- SELECT name, id FROM Employee WHERE Salary=(SELECT MAX(Salary) FROM Employee);

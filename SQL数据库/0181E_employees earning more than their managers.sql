-- 查出薪水比其经理薪水高的员工姓名

-- 自联结 法一
SELECT a.Name AS 'Employee' FROM Employee AS a
JOIN Employee AS b
ON a.ManagerId = b.Id
WHERE a.Salary > b.Salary;


-- 法二
SELECT a.Name AS 'Employee'
FROM Employee AS a, Employee AS b
WHERE a.ManagerId = b.Id
AND a.Salary > b.Salary;
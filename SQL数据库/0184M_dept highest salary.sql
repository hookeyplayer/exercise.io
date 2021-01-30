-- 两张表，Employee 和 Department
-- 查询每个部门中薪水最高的员工姓名和薪水

-- 法一：关联子查询
SELECT b.Name AS Department, a.Name AS Employee, a.Salary AS 'Salary' FROM Employee AS a
INNER JOIN Department AS b
ON a.DepartmentId = b.Id
WHERE a.Salary IN
 (SELECT MAX(Salary) FROM Employee AS c
  WHERE a.DepartmentId = c.DepartmentId
  GROUP BY c.DepartmentId);


-- 法二：联结
SELECT b.Name AS Department, a.Name AS Employee, a.Salary AS 'Salary' FROM Employee AS a
INNER JOIN Department AS b
ON a.DepartmentId = b.Id
INNER JOIN
(SELECT  DepartmentId, MAX(Salary) AS Salary FROM Employee
 GROUP BY DepartmentId) AS c
ON a.DepartmentId = c.DepartmentId
WHERE a.Salary = c.Salary;
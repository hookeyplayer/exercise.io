-- Employee, Department两张表
-- 查询各部门薪水排名前三的员工姓名和薪水
-- 若有并列相同的薪水，则一样返回

SELECT x.Department, x.Employee, x.Salary
FROM
(SELECT b.Name AS Department, 
        a.Name AS Employee, 
        a.Salary AS Salary, 
        DENSE_RANK() OVER (PARTITION BY b.Name 
                           ORDER BY a.Salary DESC) AS dept_rank
FROM Employee AS a
INNER JOIN Department AS b
ON a.DepartmentId = b.Id) AS x
WHERE x.dept_rank <= 3;
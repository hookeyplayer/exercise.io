-- 查询出至少管理5个员工的经理的名称
-- 子查询
SELECT Name FROM Employee WHERE Id IN
(SELECT ManagerId FROM Employee
 GROUP BY ManagerId
 HAVING COUNT(*) >=5);


-- 联结
SELECT Name FROM Employee AS t1 JOIN
(SELECT ManagerId FROM Employee
 GROUP BY ManagerId
 HAVING COUNT(ManagerId) >= 5) AS t2
ON t1.Id = t2.ManagerId;
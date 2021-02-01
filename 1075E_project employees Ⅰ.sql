-- 2张表：项目和员工
-- (project_id, employee_id) 的组合是该表的主键
-- employee_id 是用来联结 Employee 表的外键
-- 查询每个项目的所有员工的平均工作年限，四舍五入到2位数字
SELECT a.project_id, ROUND(AVG(b.experience_years),2) AS average_years FROM Project AS a
JOIN Employee AS b
ON a.employee_id = b.employee_id
GROUP BY a.project_id;
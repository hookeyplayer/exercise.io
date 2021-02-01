-- 2张表，salary和employee
-- 显示部门员工平均工资与公司平均工资的比较结果（较高/较低/相同）
SELECT pay_month, department_id,
CASE WHEN dep_avg > com_avg THEN 'higher'
WHEN dep_avg < com_avg THEN 'lower'
ELSE 'same' END AS comparison
FROM (
SELECT LEFT(a.pay_date, 7) AS pay_month,
b.department_id, AVG(a.amount) AS dep_avg,
(SELECT AVG(amount) FROM salary AS x
 WHERE LEFT(a.pay_date, 7) = LEFT(x.pay_date, 7)
GROUP BY LEFT(x.pay_date, 7)) AS com_avg
FROM salary AS a
JOIN employee AS b
ON a.employee_id = b.employee_id
GROUP BY pay_month, b.department_id
ORDER BY pay_month DESC ) AS tmp;




-- 日期转换
DATE_FORMAT(pay_date, '%Y-%m') AS pay_month
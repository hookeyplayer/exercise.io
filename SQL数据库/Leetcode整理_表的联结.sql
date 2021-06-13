-- Items(item_id, item_name, item_category)
-- Orders(order_id, customer_id, order_date, item_id, quantity)
-- 您是企业所有者，希望获取各类别项目在一周内每一天的销售报告
-- 查询以报告一周中的每一天每个类别产品的销量，查询结果按照商品类别 (category) 升序排序
SELECT 
	a.item_category AS Category,
	SUM(CASE WHEN DAYOFWEEK(b.order_date) = 2 THEN b.quantity ELSE 0 END) AS Monday,
	SUM(CASE WHEN DAYOFWEEK(b.order_date) = 3 THEN b.quantity ELSE 0 END) AS Tuesday,
	SUM(CASE WHEN DAYOFWEEK(b.order_date) = 4 THEN b.quantity ELSE 0 END) AS Wednesday,
	SUM(CASE WHEN DAYOFWEEK(b.order_date) = 5 THEN b.quantity ELSE 0 END) AS Thursday,
	SUM(CASE WHEN DAYOFWEEK(b.order_date) = 6 THEN b.quantity ELSE 0 END) AS Friday,
	SUM(CASE WHEN DAYOFWEEK(b.order_date) = 7 THEN b.quantity ELSE 0 END) AS Saturday,
	SUM(CASE WHEN DAYOFWEEK(b.order_date) = 1 THEN b.quantity ELSE 0 END) AS Sunday
FROM Items AS a
LEFT JOIN Orders AS b
ON a.item_id = b.item_id
GROUP BY a.item_category
ORDER BY a.item_category;

-- 查询2020年6月播放的儿童电影的标题，以任何顺序返回结果表
-- content_id是电视上某个频道中节目的 ID
-- Kids_content是一个枚举（'Y'，'N'）
 -- “ Y”表示内容适合小孩，“ N”表示内容不适合小孩
SELECT DISTINCT a.title
FROM Content AS a
JOIN TVProgram AS b
ON a.content_id = b.content_id
WHERE a.content_type = 'Movies' AND a.Kids_content = 'Y' AND LEFT(b.program_date,7) ='2020-06';


-- 查询所有客户的第一笔订单中即时订单的百分比，四舍五入到小数点后两位
-- 姗姗
SELECT ROUND(100 * COUNT(*)/(SELECT COUNT(DISTINCT customer_id) FROM Delivery), 2) AS immediate_percentage
FROM Delivery AS a
JOIN (
	SELECT 
		customer_id, 
		MIN(order_date) AS first_order
	FROM Delivery
	GROUP BY customer_id
	) AS b
ON a.customer_id = b.customer_id AND a.order_date = b.first_order
WHERE a.order_date = a.customer_pref_delivery_date;


-- Trips(id, Client_Id, Driver_Id, City_Id, Status, Request_at)
-- User(Users_Id, Banned, Role)
-- 找出某时间期间里 每一天 unbanned users' cancellation rate

SELECT 
	a.Request_at AS Day,
	1-ROUND(SUM(CASE WHEN a.Status = 'completed' THEN 1 ELSE 0 END)/COUNT(*),2) AS 'Cancellation Rate' 
FROM Trips AS a
INNER JOIN (SELECT * FROM Users WHERE Role = 'client') AS b
ON a.Client_Id = b.Users_Id
INNER JOIN (SELECT * FROM Users WHERE Role = 'driver') AS c
ON a.Driver_Id = c.Users_Id
WHERE b.Banned = 'No' AND c.Banned = 'No' AND a.Request_at BETWEEN '2013-10-01' AND '2013-10-03'
GROUP BY a.Request_at
ORDER BY a.Request_at


-- 一个国家拥有三所学校，每个学生就读一所学校
-- 该国正在参加比赛，并希望从每所学校中选出一名学生代表该国
-- 即 查找在给定约束下代表国家的所有可能的三元组，不得有重复的学生姓名与ID
SELECT 
	a.student_name AS 'member_A',
	b.student_name AS 'member_B',
	c.student_name AS 'member_C'
FROM SchoolA AS a
JOIN SchoolB AS b
ON a.student_id <> b.student_id AND a.student_name <> b.student_name
JOIN SchoolC AS c
ON a.student_id <> c.student_id AND b.student_id <> c.student_id AND a.student_name <> c.student_name AND b.student_name <> c.student_name;


-- 查询每个部门下的学生数，要列出所有部门，即使该部门没有学生
-- 结果按学生数降序、部门名称升序排列
SELECT 
	a.dept_name,
	COUNT(b.student_id) AS student_number 
FROM department AS a
LEFT JOIN student AS b
ON a.dept_id = b.dept_id
GROUP BY a.dept_name
ORDER BY student_number DESC, a.dept_name;


-- 查询出每个员工三个月的累积工资，其中不包含最近一个月，且按照员工id升序排列，月份降序排列
-- 不懂
SELECT E1.id, E1.month,
(IFNULL(E1.salary, 0) + IFNULL(E2.salary, 0) + IFNULL(E3.salary, 0)) AS Salary
FROM(
	SELECT id, MAX(month) AS month 
	FROM Employee
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


-- 2张表：项目和员工
-- (project_id, employee_id) 的组合是该表的主键
-- employee_id 是用来联结 Employee 表的外键
-- 查询每个项目的所有员工的平均工作年限，四舍五入到2位数字
SELECT a.project_id, ROUND(AVG(b.experience_years),2) AS average_years 
FROM Project AS a
JOIN Employee AS b
ON a.employee_id = b.employee_id
GROUP BY a.project_id;


-- 两张表Employee和Bonus
-- 选出奖金小于1000元的员工姓名及其获得的奖金数
-- 法一
SELECT a.name, b.bonus
FROM Employee AS a
LEFT JOIN Bonus AS b
ON a.empId = b.empId
WHERE b.bonus < 1000 OR b.bonus IS NULL;
-- 法二
SELECT a.name, b.bonus
FROM Employee AS a
LEFT JOIN Bonus AS b
ON a.empId = b.empId
WHERE a.empId NOT IN (
	SELECT empId 
	FROM Bonus 
	WHERE bonus >= 1000);


-- 两张表candidate和vote
-- 找到当选者的名字
-- 注意：本题目中不考虑平票的情况
SELECT Name 
FROM Candidate AS a
JOIN (
	SELECT CandidateId 
	FROM Vote
	GROUP BY CandidateId
	ORDER BY COUNT(*) DESC
	LIMIT 1
	) AS b
ON a.id = b.CandidateId;


-- 两张表，Employee 和 Department
-- 查询每个部门中薪水最高的员工姓名和薪水
SELECT b.Name AS Department, a.Name AS Employee, a.Salary AS 'Salary' 
FROM Employee AS a
INNER JOIN Department AS b
ON a.DepartmentId = b.Id
INNER JOIN (
	SELECT  DepartmentId, MAX(Salary) AS Salary 
	FROM Employee
	GROUP BY DepartmentId
	) AS c
ON a.DepartmentId = c.DepartmentId
WHERE a.Salary = c.Salary;


-- 查询出至少管理5个员工的经理的名称
SELECT Name 
FROM Employee AS t1 
JOIN (
	SELECT ManagerId FROM Employee
	GROUP BY ManagerId
	HAVING COUNT(ManagerId) >= 5
	) AS t2
ON t1.Id = t2.ManagerId;


-- 3张表：雇员、公司、订单
-- 找出没有将产品卖给 'RED' 公司的员工名单
SELECT name 
FROM salesperson
WHERE sales_id NOT IN (
	SELECT b.sales_id 
	FROM company AS a
	INNER JOIN orders AS b
	ON a.com_id = b.com_id
	WHERE a.name = 'RED'
	);


-- 查询每个人的姓名，以及住址
-- 注意：即使有人没有地址，也要将其罗列
SELECT a.FirstName, a.LastName, b.City, b.State 
FROM Person As a 
LEFT JOIN AddressId As b
ON a.PersonID = b.PersonID;


-- 两张表：顾客表和订单表
-- 找出没有下过订单的顾客姓名
SELECT a.Name AS 'Customers' 
FROM Customers AS a
LEFT JOIN Orders AS b
ON a.Id = b.CustomerId
WHERE b.Id IS NULL;



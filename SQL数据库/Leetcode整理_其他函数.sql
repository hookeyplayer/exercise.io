-- 1.1 行列转化 lateral view explode 
-- ab_version一行里有多个id
-- 找到某个ab_version的user_id，就需要把一行转换为很多行，每行后面都带有某个实验组的标志
SELECT * FROM table LATERAL VIEW EXPLODE(SPLIT(ab_version, ',')) vidtb AS vid_explode
WHERE vid_explode in ('1262091');

-- 1.2 随机抽样
SELECT * FROM place ORDER BY rand(1) LIMIT 2;


-- 1.3 聚合函数
-- 1.3.1 COUNT()
-- 查询首次登录后第二天也登录的用户比例
SELECT ROUND(COUNT(DISTINCT b.player_id)/COUNT(DISTINCT a.player_id), 2) AS fraction 
FROM Activity AS a
LEFT JOIN (
	SELECT
		player_id,
		MIN(event_date) AS first_login
	FROM Activity
	GROUP BY player_id) AS b
ON a.player_id = b.player_id AND DATEDIFF(a.event_date, b.first_login) = 1;

-- 食物派送1张表(delivery_id, customer_id, order_date, customer_pref_delivery_date)
-- 如果客户的首选送货日期与订单日期相同，则该订单称为即时订单，否则称为计划订单
-- 查询表中即时订单的百分比，四舍五入到小数点后两位
-- 法一
SELECT 
	ROUND(100*(SELECT COUNT(*) FROM Delivery WHERE order_date = customer_pref_delivery_date) / (SELECT COUNT(*) FROM Delivery), 2) AS immediate_percentage;

-- 法二
SELECT ROUND(IFNULL(100*SUM(order_date=customer_pref_delivery_date)/COUNT(*), 0), 2) AS immediate_percentage
FROM Delivery;


-- IF
-- 找出能构成三角形的记录，并返回no/yes
SELECT 
	*, 
	IF(x + y > z AND x + z > y AND y + z > x, 'Yes', 'No') AS triangle 
FROM triangle;

-- CASE WHEN
-- 找出各公司薪水的中位数 569 不懂
SELECT
    Employee.Id, 
    Employee.Company, 
    Employee.Salary
FROM
    Employee,
    Employee AS alias
WHERE
    Employee.Company = alias.Company
GROUP BY Employee.Company , Employee.Salary
HAVING SUM(CASE WHEN Employee.Salary = alias.Salary THEN 1 ELSE 0 END) >= ABS(SUM(SIGN(Employee.Salary - alias.Salary)))
ORDER BY Employee.Id;

-- 查询所有客户的第一笔订单中即时订单的百分比，四舍五入到小数点后两位
-- 不懂
SELECT round(sum(tag)/count(id),2) AS immediate_percentage
FROM(
	SELECT 
		customer_id AS id,
		CASE
    	   WHEN min(order_date) = min(customer_pref_delivery_date) 
    	   THEN 100.00
    	   ELSE 0 
    	END AS tag
    FROM Delivery AS d1
    GROUP BY customer_id
    ) AS d2;

-- 2张表
-- salary(id, employee_id, amount, pay_date)
-- employee(employee_id, department_id)
-- 显示部门员工平均工资与公司平均工资的比较结果（较高/较低/相同）
-- 法一 姗姗 不懂
SELECT 
	pay_month,
	department_id,
	CASE 
		WHEN dep_avg > com_avg 
		THEN 'higher'
		WHEN dep_avg < com_avg 
		THEN 'lower'
		ELSE 'same' 
	END AS comparison
FROM (
	SELECT 
		LEFT(a.pay_date, 7) AS pay_month,
		b.department_id, 
		AVG(a.amount) AS dep_avg,
		(
			SELECT AVG(amount) 
			FROM salary AS x 
			WHERE LEFT(a.pay_date, 7) = LEFT(x.pay_date, 7)
			GROUP BY LEFT(x.pay_date, 7)) AS com_avg
	FROM salary AS a
	JOIN employee AS b
	ON a.employee_id = b.employee_id
	GROUP BY pay_month, b.department_id
	ORDER BY pay_month DESC
	) AS tmp;

-- 法二
WITH dep_salary AS (
	SELECT
		e.department_id,
		DATE_FORMAT(s.pay_date, '%Y-%m') AS pay_month,
		AVG(s.amount) AS department_average
	FROM salary AS s
	JOIN employee AS e
	ON s.employee_id=e.employee_id
	GROUP BY e.department_id, DATE_FORMAT(s.pay_date, '%Y-%m')
	),

com_salary AS (
	SELECT
		DATE_FORMAT(s.pay_date, '%Y-%m') AS pay_month,
		AVG(s.amount) AS company_average
	FROM salary AS s
	JOIN employee AS e 
	ON s.employee_id=e.employee_id
	GROUP BY DATE_FORMAT(s.pay_date, '%Y-%m')
	)

SELECT 
	dep_salary.pay_month,
	dep_salary.department_id,
	CASE 
		WHEN dep_salary.department_average>com_salary.company_average
		THEN 'higher'
		WHEN dep_salary.department_average<com_salary.company_average
		THEN 'lower'
		ELSE 'same'
	END AS 'comparison'
FROM dep_salary
JOIN com_salary
ON dep_salary.pay_month=com_salary.pay_month

SELECT 
	*, 
	CASE 
		WHEN (x + y > z) AND (x + z > y) AND (y + z > x) 
		THEN 'Yes' 
		ELSE 'No' 
	END AS triangle
FROM triangle;


-- 男女性别交换
UPDATE salary
SET sex = (CASE WHEN sex = 'm' THEN 'f' ELSE 'm' END);

-- 表Department(id, revenue, month) 每个部门每个月的收入
-- 重新排表格，得到id列和所有月收入列，即返回的表有13列
SELECT 
	id,
	SUM(CASE WHEN month = 'Jan' THEN revenue ELSE NULL END) AS Jan_Revenue,
	SUM(CASE WHEN month = 'Feb' THEN revenue ELSE NULL END) AS Feb_Revenue,
	SUM(CASE WHEN month = 'Mar' THEN revenue ELSE NULL END) AS Mar_Revenue,
	SUM(CASE WHEN month = 'Apr' THEN revenue ELSE NULL END) AS Apr_Revenue,
	SUM(CASE WHEN month = 'May' THEN revenue ELSE NULL END) AS May_Revenue,
	SUM(CASE WHEN month = 'Jun' THEN revenue ELSE NULL END) AS Jun_Revenue,
	SUM(CASE WHEN month = 'Jul' THEN revenue ELSE NULL END) AS Jul_Revenue,
	SUM(CASE WHEN month = 'Aug' THEN revenue ELSE NULL END) AS Aug_Revenue,
	SUM(CASE WHEN month = 'Sep' THEN revenue ELSE NULL END) AS Sep_Revenue,
	SUM(CASE WHEN month = 'Oct' THEN revenue ELSE NULL END) AS Oct_Revenue,
	SUM(CASE WHEN month = 'Nov' THEN revenue ELSE NULL END) AS Nov_Revenue,
	SUM(CASE WHEN month = 'Dec' THEN revenue ELSE NULL END) AS Dec_Revenue
FROM Department
GROUP BY id;

-- Spending(user_id, spend_date, platform, amount)
-- （user_id，spend_date）是此表的主键
-- 返回 仅使用 mobile，仅使用 desktop 以及同时使用 mobile 和 desktop 的用户总数
-- 不懂
WITH tmp AS (
	SELECT 
		spend_date, 
		user_id, 
		SUM(amount) AS total_amount,
		CASE WHEN COUNT(DISTINCT platform) = 2 THEN 'both' ELSE platform END AS platform
	FROM Spending
	GROUP BY spend_date, user_id
	),

tmp1 AS (
	SELECT  
		DISTINCT spend_date,
		'mobile' AS platform
	FROM Spending
	UNION ALL
	SELECT  
		DISTINCT spend_date,
		'both'
	FROM Spending 
	UNION ALL
	SELECT  
		DISTINCT spend_date,
		'desktop'
	FROM Spending
	)

SELECT 
	a.spend_date, 
	a.platform, 
	COALESCE(SUM(b.total_amount),0) AS total_amount, 
	-- IFNULL(SUM(b.total_amount), 0) AS total_amount,
	COALESCE(COUNT(DISTINCT b.user_id),0) AS total_users 
	-- IFNULL(COUNT(DISTINCT b.user_id),0) AS total_users 
FROM tmp1 AS a
LEFT JOIN tmp AS b
ON a.spend_date = b.spend_date AND a.platform = b.platform
GROUP BY spend_date, platform;

-- 查询截至2019年7月27日（含）的30天期间每个用户的平均 session 数，四舍五入到小数点后两位
-- 我们要为用户计算的 session 是在该时间段内至少进行了一项活动的会话
SELECT ROUND(COALESCE(AVG(session),0),2) AS average_sessions_per_user 
FROM (
	SELECT DISTINCT user_id, COUNT(DISTINCT session_id) AS session 
	FROM Activity
	WHERE activity_date > DATE_SUB("2019-07-27", INTERVAL 30 DAY)
	GROUP BY user_id
	HAVING session >= 1
) AS tmp;

-- 3张表
-- Users(user_id, join_date, favorite_brand)
-- Orders(order_id, order_date, item_id, buyer_id, seller_id)
-- Items(item_id, item_brand)
-- 查询每个用户的加入日期和他们在2019年以买家身份下的订单数量
SELECT 
	a.user_id AS buyer_id,
	a.join_date,
	COALESCE(b.orders_in_2019, 0) AS orders_in_2019 
FROM Users AS a
LEFT JOIN (
	SELECT 
		buyer_id, 
		COUNT(order_id) AS orders_in_2019 
	FROM Orders
	WHERE YEAR(order_date) = 2019
	GROUP BY buyer_id
	) AS b
ON a.user_id = b.buyer_id;


-- 找出不是被2号顾客推荐来的顾客姓名
-- or is null
-- SQL 的三值逻辑，如果条件只是 WHERE referee_id <> 2，则返回不出 referee_id 为 null 的顾客
SELECT name 
FROM customer
WHERE COALESCE(referee_id, 0) <> 2;

-- 查询以输出带有奇数编号ID和非“无聊”描述的电影
-- 按等级排序结果
SELECT * FROM cinema
WHERE MOD(id, 2) = 1 AND description <> 'boring'
ORDER BY rating DESC;


-- 为相邻的学生换座位
-- 表(id, student)
-- 如果学生总人数为奇数，则无需更改最后一个席位
-- 官方答案 不懂
SELECT 
	(CASE 
		WHEN MOD(id, 2) != 0 AND counts != id 
		THEN id + 1
		WHEN MOD(id, 2) != 0 AND counts = id 
		THEN id
		ELSE id - 1
	END) AS id,
	student
FROM 
	seat,
	(SELECT COUNT(*) AS counts FROM seat) AS seat_counts
ORDER BY id ASC;

-- 姗姗 不懂
SELECT 
	(CASE 
		WHEN tmp.id > (SELECT MAX(id) FROM seat) 
		THEN (tmp.id-1) 
		ELSE tmp.id END) AS id,
	student
FROM (
	SELECT
		id-1 AS id, 
		student 
	FROM seat
	WHERE MOD(id, 2) = 0
	UNION
	SELECT
		id+1 AS id, 
		student 
	FROM seat
	WHERE MOD(id, 2) = 1
	) AS tmp
ORDER BY id;

-- friend_request(sender_id, send_to_id, requester_id)
-- request_accepted(requester_id, accepter_id, accept_date)
-- 找出申请通过率，结果保留两位小数
WITH tr AS (
	SELECT COUNT(sender_id) AS tot_req 
	FROM(
		SELECT sender_id
		FROM friend_request
		GROUP BY sender_id, send_to_id
		) AS t1),

ta AS (
	SELECT COUNT(requester_id) AS tot_act 
	FROM (
		SELECT requester_id
		FROM request_accepted
		GROUP BY requester_id, accepter_id
		) AS t2
	)

SELECT ROUND(IFNULL(ta.tot_act / tr.tot_req,0),2) AS accept_rate
FROM tr, ta;


-- Sales(sale_id, product_name, sale_date)
-- product_name 可能包含前导和/或尾随空格，并且它们不区分大小写 
-- 查询以进行报告小写形式的 product_name ，没有前导空格或尾随空格
-- sale_date 格式（'YYYY-MM'） 
-- 该产品在该月的总销售次数
-- 查询结果按sales_date，product_name 升序返回。
SELECT 
	LOWER(TRIM(product_name)) AS product_name, 
	LEFT(sale_date, 7) AS sale_date,
	COUNT(*) AS total
FROM Sales
GROUP BY LOWER(TRIM(product_name)), LEFT(sale_date, 7)
ORDER BY product_name, sale_date;


-- 查询2020年6月和2020年7月每个月至少花费$100的客户的 customer_id 和customer_name
SELECT 
	customer_id, 
	name 
FROM Customers
WHERE customer_id IN (
	SELECT a.customer_id 
	FROM Orders AS a
	JOIN Product AS b
	ON a.product_id = b.product_id
	WHERE a.order_date BETWEEN '2020-06-01' AND '2020-06-30'
	GROUP BY a.customer_id
	HAVING SUM(a.quantity * b.price) >= 100
	)
AND customer_id IN (
	SELECT a.customer_id 
	FROM Orders AS a
	JOIN Product AS b
	ON a.product_id = b.product_id
	WHERE a.order_date BETWEEN '2020-07-01' AND '2020-07-31'
	GROUP BY a.customer_id
	HAVING SUM(a.quantity * b.price) >= 100
	);


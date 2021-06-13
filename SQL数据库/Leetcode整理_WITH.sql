-- Products(product_id, new_price, change_date)表记录着各商品价格变化的情况
-- 组合主键(product_id, change_date)
-- 查询所有产品在2019-08-16的价格。假设所有产品的价格在变化之前均为10
-- 返回两列的表：product_id和price
-- 不懂
-- 法一
WITH product_list AS (
	SELECT DISTINCT product_id
	FROM Products
	),
recent_price AS (
	SELECT 
		product_id,
		new_price
	FROM (
		SELECT 
			product_id,
			new_price,
			RANK() OVER (PARTITION BY product_id ORDER BY change_date DESC) AS 'rk'
		FROM Products
		WHERE change_date<='2019-08-16'
		) AS tmp 
	WHERE rk=1
	)
SELECT 
	p1.product_id,
	IFNULL(p2.new_price, 10) AS 'price'
FROM product_list AS p1 
LEFT JOIN recent_price AS p2 
ON p1.product_id=p2.product_id;


-- 法二
WITH tmp1 AS (
	SELECT 
		a.product_id, 
		a.new_price AS price 
	FROM Products AS a
	JOIN (
		SELECT 
			product_id, 
			MAX(change_date) AS change_date
		FROM Products
		WHERE change_date <= '2019-08-16'
		GROUP BY product_id
		) AS b
	ON a.product_id = b.product_id AND a.change_date = b.change_date
	),

-- 赋值null以10
tmp2 AS (
	SELECT 
		product_id, 10 AS price 
	FROM Products 
	WHERE change_date > '2019-08-16' AND product_id NOT IN (SELECT product_id FROM tmp1)
	)

SELECT * FROM tmp1
UNION 
SELECT * FROM tmp2
ORDER BY price DESC, product_id ASC;


-- 用户(id, name) 和 登录(id, login_date) 
-- 查询活跃用户的 ID 和名称，活跃用户是指连续5天或以上登录其帐户的用户
-- 查询结果按用户 ID 升序排序
-- 不懂 1454
WITH tmp AS(
	SELECT 
		a.id, 
		a.name, 
		b.login_date,
		ROW_NUMBER() OVER(PARTITION BY a.id ORDER BY b.login_date) AS rnk, 
		DATEDIFF(b.login_date, '2020-01-01') AS diff 
	FROM Accounts AS a
	LEFT JOIN (SELECT 
				   DISTINCT id,
				   login_date
			   FROM Logins
			   ) AS b
	ON a.id = b.id
	)

SELECT 
	DISTINCT id,
	name 
FROM tmp
GROUP BY id, name, diff-rnk
HAVING COUNT(login_date) >= 5;


-- 查询每个用户的最新的3个订单。如果用户订购的订单少于3个，则返回其所有订单
-- 查询结果按 customer_name 升序排序；如果出现平局，按 customer_id 升序排序
-- 如果仍然有平局，按 order_date 降序排序
WITH tmp AS (
	SELECT
		a.name,
		a.customer_id,
		b.order_id,
		b.order_date,
		ROW_NUMBER() OVER(PARTITION BY a.name, a.customer_id ORDER BY b.order_date DESC) AS rnk
	FROM Customers AS a
	JOIN Orders AS b
	ON a.customer_id = b.customer_id
	)

SELECT
	name AS customer_name,
	customer_id,
	order_id,
	order_date
FROM tmp
WHERE rnk <= 3
ORDER BY customer_name, customer_id, order_date DESC;

-- 2张表
-- actions(user_id, post_id, action_date, action, extra)
-- removals(post_id, remove_date)
-- 查询被举报为垃圾邮件后被删除的帖子每日平均百分比，四舍五入到小数点后两位
WITH spam_report AS (
	SELECT
		post_id,
		action_date
	FROM Actions
	WHERE action='report' and extra='spam'
	)
SELECT ROUND(AVG(percent)*100, 2) AS average_daily_percent
FROM (
	SELECT
		s.action_date,
		COUNT(DISTINCT r.post_id) / COUNT(DISTINCT s.post_id) AS percent
	FROM spam_report AS s
	LEFT JOIN Removals AS r
	ON s.post_id=r.post_id
	GROUP BY s.action_date
	) AS tmp;


-- 找出连续至少三条记录体育馆参观人数至少为100人的情况
-- 表：id, visit_date, people
-- 不懂
WITH 

tmp AS (
	SELECT 
		a.visit_date AS date1,
		b.visit_date AS date2,
		c.visit_date AS date3 
	FROM stadium AS a
	LEFT JOIN stadium AS b 
	ON b.id = a.id + 1
	LEFT JOIN stadium AS c
	ON c.id = a.id + 2
	WHERE a.people >= 100
	AND b.people >= 100
	AND c.people >= 100),

tmp1 AS (
	SELECT date1 AS total_date FROM tmp
	UNION
	SELECT date2 AS total_date FROM tmp
	UNION
	SELECT date3 AS total_date FROM tmp)

SELECT * FROM stadium
WHERE visit_date IN (SELECT * FROM tmp1);


-- 2个表，项目和员工
-- 查询员工最多的项目
WITH t AS (
	SELECT
		COUNT(*) AS c, 
		project_id 
	FROM project 
	GROUP BY project_id
	)

SELECT project_id 
FROM t 
WHERE t.c = (SELECT MAX(c) FROM t);


-- 找出拥有好友数最多的用户编号及其拥有的好友数
-- 只有一个用户拥有最多的好友数
-- 好友邀请只能被接受一次，因此要去除重复值
-- 表：requester_id, accepter_id, accept_date
WITH ids AS (
	SELECT DISTINCT requester_id AS id 
	FROM request_accepted
	UNION
	SELECT DISTINCT accepter_id AS id 
	FROM request_accepted),

tmp1 AS (
	SELECT 
		requester_id AS id, 
		COUNT(DISTINCT accepter_id) AS fri_num 
	FROM request_accepted
	GROUP BY requester_id
	),


tmp2 AS (
	SELECT 
		accepter_id AS id, 
		COUNT(DISTINCT requester_id) AS fri_num 
	FROM request_accepted
	GROUP BY accepter_id
	),

tmp3 AS (
	SELECT 
		a.id, 
		(IFNULL(b.fri_num,0) + IFNULL(c.fri_num,0)) AS num
	FROM ids AS a
	LEFT JOIN tmp1 AS b ON a.id = b.id
	LEFT JOIN tmp2 AS c ON a.id = c.id
	)

SELECT * FROM tmp3
ORDER BY num DESC
LIMIT 1;

-- UNION去重且排序
-- UNION ALL不去重不排序
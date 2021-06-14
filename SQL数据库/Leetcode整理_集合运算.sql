-- UNION 针对行列的增加
-- 执行多个SELECT查询语句，并将结果作为单个查询结果集返回
-- 会自动省略重复值（如果想保留，就在UNION后面加上all，其他运算符同理）
-- ①——作为运算对象的记录的列数必须相同
-- ②——作为运算对象的记录中列的类型必须一致（若不一致，可以使用cast函数来进行转换）
-- ③——order by子句只能使用一次，放最后

-- 2个表，赛程 和 运动员
-- Player(player_id, group_id)
-- Matches(match_id, first_player, second_player, first_score, second_score)
-- 赛程表记录了每场比赛的两个参与者及其各自得分情况，其中 match_id 为该表主键
-- 每个组中的获胜者是得分最高的人
-- 如果是平局，则 player_id 编号小的获胜
-- 查询每个组(group_id)中的获胜者
-- 不懂
SELECT 
	group_id,
	player_id 
FROM (
	SELECT 
		a.group_id, 
		a.player_id,
		ROW_NUMBER() OVER(PARTITION BY a.group_id ORDER BY IFNULL(b.score, 0) DESC, a.player_id) AS rnk
	FROM Players AS a
	LEFT JOIN (

		SELECT 
			player_id,
			SUM(score) AS score
		FROM (
			SELECT 
				match_id,
				first_player AS player_id,
				first_score AS score
			FROM Matches

			UNION ALL

			SELECT
				match_id, second_player AS player_id,
				second_score AS score
			FROM Matches
			) AS x
		GROUP BY player_id
		) AS b

	ON a.player_id = b.player_id
	) AS tmp
WHERE rnk = 1;


-- Person(id, name, phone_number)
-- Country(name, country_code)
-- Calls(caller_id, callee_id, duration)
-- 一家电信公司希望在新国家投资
-- 该公司打算在 该国家/地区的平均通话时间 大于 全球平均通话时间 的国家/地区进行投资
-- 查询该公司可以投资的国家/地区
-- 以任何顺序返回
WITH tmp AS (
	SELECT
		caller_id AS call_id,
		duration
	FROM (
		SELECT
			DISTINCT caller_id,
			callee_id,
			duration
		FROM Calls) AS a

	UNION ALL

	SELECT
		callee_id AS call_id,
		duration
	FROM (
		SELECT 
			DISTINCT caller_id,
			callee_id,
			duration
		FROM Calls) AS b
	)

SELECT a.name AS country 
FROM Country AS a
LEFT JOIN Person AS b
ON a.country_code = LEFT(b.phone_number, 3)
LEFT JOIN tmp AS c
ON b.id = c.call_id
GROUP BY a.name
HAVING AVG(c.duration) > (SELECT AVG(duration) FROM tmp);


-- 交易和退款2张表
-- Transactions(id, country, state, amount, trans_date)
-- Chargebacks(trans_id, charge_date)
-- 查询每个月和每个国家/地区的已批准交易的数量及其总金额，拒付金额及其总金额
-- 姗姗
WITH tmp AS (
	SELECT 
		a.trans_id AS id,
		b.country,
		'checkback' AS state,
		b.amount,
		a.trans_date
	FROM Chargebacks AS a
	LEFT JOIN Transactions AS b
	ON a.trans_id = b.id

	UNION ALL
	    
	SELECT * FROM Transactions
	WHERE state = 'approved'
	)

SELECT
	DATE_FORMAT(trans_date, "%Y-%m") AS month,
	country,
	SUM(CASE WHEN state = 'approved' THEN 1 ELSE 0 END) AS approved_count,
	SUM(CASE WHEN state = 'approved' THEN amount ELSE 0 END) AS approved_amount,
	SUM(CASE WHEN state = 'checkback' THEN 1 ELSE 0 END) AS chargeback_count,
	SUM(CASE WHEN state = 'checkback' THEN amount ELSE 0 END) AS chargeback_amount
FROM tmp
GROUP BY DATE_FORMAT(trans_date, "%Y-%m"), country;



-- Users(user_id, user_name, credit)
-- Transactions(trans_id, paid_by, paid_to, amount, transacted_on)
-- 找出所有用户的当前余额，并检查他们是否违反了信用额度（如果其当前信用额小于0）
-- 半懂
WITH tmp AS (
	SELECT 
		paid_by AS user,
		(-1 * amount) AS amount
	FROM Transactions
	UNION ALL 
	SELECT 
		paid_to AS user,
		amount
	FROM Transactions
	),

tmp1 AS (
	SELECT 
		user,
		SUM(amount) AS total
	FROM tmp
	GROUP BY user
	),

tmp2 AS (
	SELECT 
		a.user_id,
		a.user_name,
		(a.credit + IFNULL(b.total, 0)) AS credit
	FROM Users AS a
	LEFT JOIN tmp1 AS b
	ON a.user_id = b.user
	GROUP BY a.user_id
	)

SELECT
	user_id,
	user_name,
	credit,
	CASE
		WHEN credit >= 0 THEN 'No'
		WHEN credit < 0 THEN 'Yes'
	END AS credit_limit_breached
FROM tmp2;


-- Customers(customer_id, customer_name)
-- 查询丢失的客户ID。缺少的ID不在“客户”表中，但在1到表中最大的customer_id之间的范围内
-- 请注意，最大的customer_id将不超过100。按ID升序返回结果表
-- with recursive 是一个递归的查询子句，他会把查询出来的结果再次代入到查询子句中继续查询
-- 不懂
WITH RECURSIVE id_seq AS (
	SELECT 1 AS continued_id
	UNION 
	SELECT (continued_id + 1) FROM id_seq WHERE continued_id < (SELECT MAX(customer_id) FROM Customers) 
	)

SELECT continued_id AS ids
FROM id_seq
WHERE continued_id NOT IN (SELECT customer_id FROM Customers)
ORDER BY ids;

-- 找出所有用户的当前余额，并检查他们是否违反了信用额度（如果其当前信用额小于0）
WITH tmp AS (
	SELECT 
		paid_by AS user,
		(-1 * amount) AS amount
	FROM Transactions
	UNION ALL 
	SELECT 
		paid_to AS user,
		amount
	FROM Transactions
	),

tmp1 AS (
	SELECT 
		user,
		SUM(amount) AS total
	FROM tmp
	GROUP BY user
	),

tmp2 AS (
	SELECT 
		a.user_id,
		a.user_name,
		(a.credit + IFNULL(b.total, 0)) AS credit
	FROM Users AS a
	LEFT JOIN tmp1 AS b
	ON a.user_id = b.user
	GROUP BY a.user_id
	)

SELECT
	user_id,
	user_name,
	credit,
	CASE
		WHEN credit >= 0 
		THEN 'No'
		WHEN credit < 0 
		THEN 'Yes'
	END AS credit_limit_breached
FROM tmp2;


SELECT * FROM student
WHERE class="01" AND age>ALL(SELECT age FROM student WHERE class="02");

SELECT * FROM student
WHERE class="01" AND age>(SELECT MAX(age) FROM student WHERE class="02");

-- 找出拥有好友数最多的用户编号及其拥有的好友数
-- 只有一个用户拥有最多的好友数
-- 好友邀请只能被接受一次，因此要去除重复值
SELECT 
	c.people as id, 
	SUM(c.cnt) AS num
FROM (
	SELECT 
		requester_id AS people,
		COUNT(DISTINCT accepter_id) AS cnt
	FROM request_accepted
	GROUP BY requester_id

	UNION ALL   
	
	SELECT 
		accepter_id AS people, 
		COUNT(DISTINCT requester_id) AS cnt
	FROM request_accepted
	GROUP BY accepter_id 
	) AS c
GROUP BY c.people
ORDER BY SUM(c.cnt) DESC
LIMIT 1;

-- 找到国土面积大于300万平方公里或人口数超过2500万的国家，并显示人口数和国土面积
SELECT 
	name, 
	population, 
	area
FROM World
WHERE area > 3000000
UNION
SELECT 
	name, 
	population, 
	area
FROM World
WHERE population > 25000000;

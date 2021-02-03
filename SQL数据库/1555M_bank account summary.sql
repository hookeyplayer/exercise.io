-- 找出所有用户的当前余额，并检查他们是否违反了信用额度（如果其当前信用额小于0）
WITH

tmp AS (
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
FROM Users a
LEFT JOIN tmp1 b
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
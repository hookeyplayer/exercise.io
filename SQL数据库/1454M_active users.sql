-- 用户 和 登录 2个表
-- 查询活跃用户的 ID 和名称，活跃用户是指连续5天或以上登录其帐户的用户，查询结果按用户 ID 升序排序
WITH

tmp AS(
SELECT 
	a.id, 
	a.name, 
	b.login_date,
	ROW_NUMBER() OVER(PARTITION BY a.id ORDER BY b.login_date) AS rnk, 
	DATEDIFF(b.login_date, '2020-01-01') AS diff 
FROM Accounts a
LEFT JOIN (SELECT 
			   DISTINCT id,
			   login_date
		   FROM Logins) b
	ON a.id = b.id
)

SELECT 
	DISTINCT id,
	name 
FROM tmp
GROUP BY id, name, diff-rnk
HAVING COUNT(login_date) >= 5;
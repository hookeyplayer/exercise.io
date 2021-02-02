-- （user_id，spread_date）是此表的主键
-- 查询每个日期的用户总数,ie，仅使用 mobile，仅使用 desktop 以及同时使用 mobile 和 desktop 的用户总数
WITH

tmp AS (
SELECT spend_date, user_id, SUM(amount) AS total_amount,
CASE WHEN COUNT(DISTINCT platform) = 2 THEN 'both'
ELSE platform END as platform
FROM Spending
GROUP BY spend_date, user_id
),

tmp1 AS (
SELECT  DISTINCT spend_date,'mobile' as platform
FROM Spending
UNION ALL
SELECT  DISTINCT spend_date,'both'
FROM Spending 
UNION ALL
SELECT  DISTINCT spend_date,'desktop'
FROM Spending
)

SELECT a.spend_date, a.platform, 
COALESCE(SUM(b.total_amount),0) AS total_amount, 
COALESCE(COUNT(DISTINCT b.user_id),0) AS total_users 
FROM tmp1 AS a
LEFT JOIN tmp AS b
ON a.spend_date = b.spend_date
AND a.platform = b.platform
GROUP BY spend_date, platform;
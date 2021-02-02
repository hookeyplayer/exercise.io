-- 查询截至2019年7月27日（含）的30天期间的每日活动用户数
-- 如果某天某天至少进行了一项活动，则该用户在某天是活跃的
SELECT activity_date day, COUNT(DISTINCT user_id) active_users 
FROM (
	SELECT DISTINCT activity_date, user_id FROM Activity
	WHERE activity_date > DATE_SUB("2019-07-27", INTERVAL 30 DAY)
	GROUP BY activity_date, user_id
	HAVING COUNT(DISTINCT activity_type) >= 1
) tmp
GROUP BY activity_date;
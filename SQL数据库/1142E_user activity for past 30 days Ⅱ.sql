-- 查询截至2019年7月27日（含）的30天期间每个用户的平均 session 数，四舍五入到小数点后两位
-- 我们要为用户计算的 session 是在该时间段内至少进行了一项活动的会话
SELECT ROUND(COALESCE(AVG(session),0),2) average_sessions_per_user 
FROM (
	SELECT DISTINCT user_id, COUNT(DISTINCT session_id) session 
	FROM Activity
	WHERE activity_date > DATE_SUB("2019-07-27", INTERVAL 30 DAY)
	GROUP BY user_id
	HAVING session >= 1
) tmp;

-- coalesce: return the first non-null value in a list
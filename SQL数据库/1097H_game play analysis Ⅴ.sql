-- 将每个用户首次登录的日期定义为安装日
-- 查询每个安装日，安装的人数以及安装日的留存率
-- 安装日的留存率 = 安装日后的第一天登录的用户比例/安装日安装的用户数
SELECT a.install_dt, COUNT(a.player_id) AS installs,
ROUND(COUNT(b.player_id)/COUNT(a.player_id),2) AS Day1_retention FROM (
SELECT DISTINCT player_id, FIRST_VALUE(event_date) OVER(PARTITION BY player_id ORDER BY event_date) AS install_dt FROM Activity
) AS a
LEFT JOIN Activity AS b
ON a.player_id = b.player_id
AND DATEDIFF(b.event_date, a.install_dt) = 1
GROUP BY a.install_dt;
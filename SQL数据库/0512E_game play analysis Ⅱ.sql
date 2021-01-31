-- 查询每个用户首次登陆的日期所使用的设备

-- 联结
SELECT a.player_id, a.device_id FROM Activity AS a
INNER JOIN
(SELECT player_id, MIN(event_date) AS first_login FROM Activity
GROUP BY player_id
ORDER BY player_id) AS b
ON a.player_id = b.player_id
AND a.event_date = b.first_login
ORDER BY a.player_id;

-- 前一题
-- 查询每个用户首次登陆的日期
-- SELECT player_id, MIN(event_date) AS first_login FROM Activity
-- GROUP BY player_id
-- ORDER BY player_id;


-- 窗口函数
SELECT player_id, device_id FROM (
    SELECT player_id, device_id, 
    RANK() OVER (PARTITION BY player_id ORDER BY event_date) AS rnk
    FROM Activity)
AS tmp
WHERE rnk = 1;
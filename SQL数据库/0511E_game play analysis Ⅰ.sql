-- 查询每个用户首次登陆的日期
-- (player_id, event_date) is the primary key 
SELECT player_id, MIN(event_date) AS first_login FROM Activity
GROUP BY player_id
ORDER BY player_id;
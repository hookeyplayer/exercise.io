-- 按照日期，查询每个用户累积玩的游戏数

-- 关联子查询
SELECT a.player_id, a.event_date,
 (SELECT SUM(games_played) FROM Activity AS b
  WHERE a.player_id = b.player_id
  AND a.event_date >= b.event_date) AS games_played_so_far
FROM Activity AS a
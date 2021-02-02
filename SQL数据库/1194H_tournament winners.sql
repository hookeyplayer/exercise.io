-- 2个表，赛程 和 运动员
-- 赛程表记录了每场比赛的两个参与者及其各自得分情况，其中 match_id 为该表主键
-- 每个组中的获胜者是得分最高的人
-- 如果是平局，则 player_id 编号小的获胜
-- 查询每个组中的获胜者
SELECT 
	group_id,
	player_id 
FROM (
SELECT
a.group_id, a.player_id,
ROW_NUMBER() OVER(PARTITION BY a.group_id ORDER BY IFNULL(b.score,0) DESC, a.player_id) AS rnk
FROM Players a
LEFT JOIN (
	SELECT 
	player_id,
	SUM(score) AS score
		FROM (
			SELECT match_id,
			first_player AS player_id,
			first_score AS score
			FROM Matches

			UNION ALL

			SELECT
				match_id, second_player AS player_id,
				second_score AS score
			FROM Matches
		) x
	GROUP BY player_id
	) AS b
ON a.player_id = b.player_id
) AS tmp
WHERE rnk = 1;
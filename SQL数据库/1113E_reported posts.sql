-- action 列可能的值为 view, like, reaction, comment, report, 以及 share
-- extra 列不是必须的，包含有关操作的可选信息，例如报告原因或反应类型
-- 查询每个"报告原因"昨天报告的帖子数，假设今天是2019-07-05
-- Write an SQL query that reports # of posts reported yesterday for each report reason
SELECT extra AS report_reason, COUNT(DISTINCT post_id) AS report_count
FROM Actions
WHERE extra IS NOT NULL 
AND action = 'report'
AND DATEDIFF("2019-07-05", action_date) = 1
GROUP BY extra;
-- 2张表，actions和removals
-- 查询被举报为垃圾邮件后被删除的帖子每日平均百分比，四舍五入到小数点后两位
SELECT ROUND(AVG(percentage),2) average_daily_percent
FROM (SELECT action_date, (COUNT(DISTINCT b.post_id)/COUNT(DISTINCT a.post_id))*100 percentage 
FROM Actions a
LEFT JOIN Removals  b
ON a.post_id = b.post_id
WHERE a.action = 'report'
AND a.extra = 'spam'
GROUP BY a.action_date
) tmp;
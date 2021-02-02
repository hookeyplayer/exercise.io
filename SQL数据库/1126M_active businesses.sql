-- (business_id, eventtype) 联合主键
-- 查询所有活跃商家 (active business)，返回其编号
-- 活跃商家：至少有一个 event_type 出现的频率高于该类 event_type 出现的平均频率
SELECT business_id FROM (
	SELECT a.business_id,
		   a.event_type,
		   a.occurences,
		   b.avg_occ FROM Events AS a
	LEFT JOIN (SELECT event_type, AVG(occurences) AS avg_occ FROM Events GROUP BY event_type) AS b
ON a.event_type = b.event_type
) AS tmp
WHERE occurences > avg_occ
GROUP BY business_id
HAVING COUNT(*) > 1;
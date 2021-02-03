-- 一家电信公司希望在新国家投资
-- 该公司打算在 该国家/地区的平均通话时间 大于 全球平均通话时间 的国家/地区进行投资
-- 查询该公司可以投资的国家/地区
-- 以任何顺序返回
WITH  

tmp AS (
SELECT
	caller_id AS call_id,
	duration
FROM (
	SELECT
		DISTINCT caller_id,
		callee_id,
		duration
	FROM Calls) a
UNION ALL
SELECT
	callee_id AS call_id,
	duration
FROM (
	SELECT 
		DISTINCT caller_id,
		callee_id,
		duration
	FROM Calls) b
)

SELECT a.name AS country 
FROM Country a
LEFT JOIN Person b
	ON a.country_code = LEFT(b.phone_number, 3)
LEFT JOIN tmp c
	ON b.id = c.call_id
GROUP BY a.name
HAVING AVG(c.duration) > (SELECT AVG(duration) FROM tmp);
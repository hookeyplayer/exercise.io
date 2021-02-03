-- p1和p2是矩形的两个相对角的id，且p1 <p2
SELECT
	a.id AS p1,
	b.id AS p2, 
	ABS(a.x_value - b.x_value) * ABS(a.y_value - b.y_value) AS area
FROM Points a
LEFT JOIN Points b
	ON a.id < b.id
WHERE ABS(a.x_value - b.x_value) <> 0 
AND ABS(a.y_value - b.y_value) <> 0
ORDER BY area DESC, p1, p2;
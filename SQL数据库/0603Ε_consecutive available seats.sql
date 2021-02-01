-- 找出连续座位的编号
SELECT DISTINCT a.seat_id
FROM cinema AS a JOIN cinema AS b
ON ABS(a.seat_id - b.seat_id) = 1
AND a.free = TRUE AND b.free = TRUE
ORDER BY a.seat_id;
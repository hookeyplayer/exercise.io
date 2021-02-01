-- 为相邻的学生换座位
-- 如果学生总人数为奇数，则无需更改最后一个席位
SELECT
(CASE
WHEN MOD(id, 2) != 0 AND counts != id THEN id + 1
WHEN MOD(id, 2) != 0 AND counts = id THEN id
ELSE id - 1
END) AS id,
student
FROM seat,
(SELECT COUNT(*) AS counts FROM seat) AS seat_counts
ORDER BY id ASC;

SELECT 
(CASE WHEN tmp.id > (SELECT MAX(id) FROM seat) THEN (tmp.id-1) ELSE tmp.id END) AS id,
student
FROM (
SELECT id-1 AS id, student FROM seat
WHERE MOD(id, 2) = 0
UNION
SELECT id+1 AS id, student FROM seat
WHERE MOD(id, 2) = 1
) AS tmp
ORDER BY id;
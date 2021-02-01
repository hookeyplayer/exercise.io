-- 坐标点最短距离
SELECT
ROUND(MIN(SQRT(POW(a.x - b.x, 2) + POW(a.y - b.y, 2))),2) AS shortest
FROM point_2d AS a
JOIN point_2d AS b
ON a.x <> b.x OR a.y <> b.y;
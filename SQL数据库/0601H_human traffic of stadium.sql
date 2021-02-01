-- 找出连续至少三条记录体育馆参观人数至少为100人的情况
-- 3 or more consecutive rows and the amount of people more than 100(inclusive)
WITH 
tmp AS (
SELECT a.visit_date AS date1,
b.visit_date AS date2,
c.visit_date AS date3
FROM stadium AS a
LEFT JOIN stadium AS b 
ON b.id = a.id + 1
LEFT JOIN stadium AS c
ON c.id = a.id + 2
WHERE a.people >= 100
AND b.people >= 100
AND c.people >= 100
),

tmp1 AS (
SELECT date1 AS total_date FROM tmp
UNION
SELECT date2 AS total_date FROM tmp
UNION
SELECT date3 AS total_date FROM tmp
)

SELECT * FROM stadium
WHERE visit_date IN 
(SELECT * FROM tmp1);
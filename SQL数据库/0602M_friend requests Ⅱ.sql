-- 找出拥有好友数最多的用户编号及其拥有的好友数
-- 只有一个用户拥有最多的好友数
-- 好友邀请只能被接受一次，因此要去除重复值
-- 法一
SELECT c.people as id, SUM(c.cnt) AS num
FROM (
SELECT requester_id AS people, COUNT(DISTINCT accepter_id) AS cnt
FROM request_accepted
GROUP BY requester_id

UNION ALL   

SELECT accepter_id AS people, COUNT(DISTINCT requester_id) AS cnt
FROM request_accepted
GROUP BY accepter_id 
) AS c

GROUP BY c.people
ORDER BY SUM(c.cnt) DESC
LIMIT 1;


-- 姗姗
WITH

ids AS (
SELECT DISTINCT requester_id AS id FROM request_accepted
UNION
SELECT DISTINCT accepter_id AS id FROM request_accepted
),

tmp1 AS (
SELECT requester_id AS id, COUNT(DISTINCT accepter_id) AS fri_num FROM request_accepted
GROUP BY requester_id
),


tmp2 AS (SELECT accepter_id AS id, COUNT(DISTINCT requester_id) AS fri_num FROM request_accepted
GROUP BY accepter_id
),

tmp3 AS (
SELECT a.id, 
(IFNULL(b.fri_num,0) + IFNULL(c.fri_num,0)) AS num
FROM ids AS a
LEFT JOIN tmp1 AS b ON a.id = b.id
LEFT JOIN tmp2 AS c ON a.id = c.id
)

SELECT * FROM tmp3
ORDER BY num DESC
LIMIT 1;
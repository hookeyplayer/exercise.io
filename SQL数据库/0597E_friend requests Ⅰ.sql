-- 找出申请通过率，结果保留两位小数
-- 子查询
SELECT
ROUND(
    IFNULL(
    (SELECT COUNT(*) FROM (SELECT DISTINCT requester_id,
                           accepter_id from request_accepted)
     AS A)
    /
    (SELECT COUNT(*) FROM (SELECT DISTINCT sender_id,
                           send_to_id FROM friend_request) 
     AS B), 0)
    , 2) 
    AS accept_rate;


-- 法二
WITH 
tr AS (
	-- total unique sent requests
    SELECT COUNT(sender_id) AS tot_req FROM(
    SELECT sender_id
    FROM friend_request
    GROUP BY sender_id, send_to_id) AS t1 
),

ta AS (
	-- total unique accepted requests
    SELECT COUNT(requester_id) AS tot_act FROM  (
    SELECT requester_id
    FROM request_accepted
    GROUP BY requester_id, accepter_id) AS t2
)

SELECT ROUND(IFNULL(ta.tot_act / tr.tot_req,0),2) AS accept_rate
FROM tr, ta;
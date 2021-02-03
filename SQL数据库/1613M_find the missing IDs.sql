-- 查询丢失的客户ID。缺少的ID不在“客户”表中，但在1到表中最大的customer_id之间的范围内
-- 请注意，最大的customer_id将不超过100。按ID升序返回结果表
WITH RECURSIVE id_seq AS (
SELECT 1 as continued_id
UNION 
SELECT (continued_id + 1)
FROM id_seq
WHERE continued_id < (SELECT MAX(customer_id) FROM Customers) 
)

SELECT continued_id AS ids
FROM id_seq
WHERE continued_id NOT IN (SELECT customer_id FROM Customers)
ORDER BY ids; 
-- 查询买了 S8 但是没有买 iPhone 的顾客的 buyer_id
WITH
tmp AS (
SELECT a.buyer_id, b.product_name FROM Sales AS a
JOIN Product AS b
ON a.product_id = b.product_id
)

SELECT DISTINCT buyer_id FROM tmp
WHERE buyer_id NOT IN (SELECT buyer_id FROM tmp WHERE product_name = 'iPhone')
AND buyer_id IN (SELECT buyer_id FROM tmp WHERE product_name = 'S8');
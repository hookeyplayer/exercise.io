-- 2个表，客户和产品，通过product_id联结
-- 找出从“客户”表中购买了“产品”表中所有产品的客户ID
SELECT b.customer_id FROM Product AS a
LEFT JOIN Customer AS b
ON a.product_key = b.product_key
GROUP BY b.customer_id
HAVING COUNT(DISTINCT b.product_key) = (SELECT COUNT(*) FROM Product);
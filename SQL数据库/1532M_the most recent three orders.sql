-- 查询每个用户的最新的3个订单。如果用户订购的订单少于3个，则返回其所有订单
-- 查询结果按 customer_name 升序排序；如果出现平局，按 customer_id 升序排序
-- 如果仍然有平局，按 order_date 降序排序
WITH

tmp AS (
SELECT
	a.name,
	a.customer_id,
	b.order_id,
	b.order_date,
	ROW_NUMBER() OVER(PARTITION BY a.name, a.customer_id ORDER BY b.order_date DESC) AS rnk
FROM Customers a
JOIN Orders b
	ON a.customer_id = b.customer_id
)

SELECT
	name AS customer_name,
	customer_id,
	order_id,
	order_date
FROM tmp
WHERE rnk <= 3
ORDER BY customer_name, customer_id, order_date DESC;
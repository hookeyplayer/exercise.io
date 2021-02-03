WITH

tmp AS (
SELECT
	a.product_name,
	a.product_id,
	b.order_id,
	b.order_date,
	RANK() OVER(PARTITION BY a.product_name, a.product_id ORDER BY b.order_date DESC) AS rnk
FROM Products a
JOIN Orders b
	ON a.product_id = b.product_id
)

SELECT
	product_name,
	product_id,
	order_id,
	order_date
FROM tmp
WHERE rnk = 1
ORDER BY product_name, product_id, order_id;
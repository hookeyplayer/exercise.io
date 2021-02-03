WITH

tmp AS (
SELECT 
	a.customer_id,
	b.product_id,
	c.product_name,
	COUNT(b.order_id) OVER(PARTITION BY a.customer_id, b.product_id) AS freq
FROM Customers a
JOIN Orders b
	ON a.customer_id = b.customer_id
JOIN Products c
	ON b.product_id = c.product_id
),

tmp1 AS (
SELECT 
	customer_id,
	product_id, 
	product_name,
	freq,
	DENSE_RANK() OVER(PARTITION BY customer_id ORDER BY freq DESC) AS rnk
FROM tmp
)

SELECT DISTINCT customer_id, product_id, product_name 
FROM tmp1
WHERE rnk = 1;
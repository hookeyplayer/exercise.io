-- 查询2020年6月和2020年7月每个月至少花费$ 100的客户的 customer_id 和customer_name，以任何顺序返回
SELECT customer_id, name 
FROM Customers
WHERE customer_id IN (
	SELECT a.customer_id 
	FROM Orders a
	JOIN Product b
		ON a.product_id = b.product_id
	WHERE a.order_date BETWEEN '2020-06-01' AND '2020-06-30'
	GROUP BY a.customer_id
	HAVING SUM(a.quantity * b.price) >= 100
)
AND customer_id IN (
	SELECT a.customer_id 
	FROM Orders a
	JOIN Product b
		ON a.product_id = b.product_id
	WHERE a.order_date BETWEEN '2020-07-01' AND '2020-07-31'
	GROUP BY a.customer_id
	HAVING SUM(a.quantity * b.price) >= 100
);
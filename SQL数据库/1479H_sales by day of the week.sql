SELECT 
	a.item_category AS Category,
	SUM(CASE WHEN DAYOFWEEK(b.order_date) = 2 THEN b.quantity ELSE 0 END) AS Monday,
	SUM(CASE WHEN DAYOFWEEK(b.order_date) = 3 THEN b.quantity ELSE 0 END) AS Tuesday,
	SUM(CASE WHEN DAYOFWEEK(b.order_date) = 4 THEN b.quantity ELSE 0 END) AS Wednesday,
	SUM(CASE WHEN DAYOFWEEK(b.order_date) = 5 THEN b.quantity ELSE 0 END) AS Thursday,
	SUM(CASE WHEN DAYOFWEEK(b.order_date) = 6 THEN b.quantity ELSE 0 END) AS Friday,
	SUM(CASE WHEN DAYOFWEEK(b.order_date) = 7 THEN b.quantity ELSE 0 END) AS Saturday,
	SUM(CASE WHEN DAYOFWEEK(b.order_date) = 1 THEN b.quantity ELSE 0 END) AS Sunday
FROM Items AS a
LEFT JOIN Orders AS b
	ON a.item_id = b.item_id
GROUP BY a.item_category
ORDER BY a.item_category;
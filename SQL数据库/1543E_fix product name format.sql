SELECT 
	LOWER(TRIM(product_name)) AS product_name, 
	LEFT(sale_date, 7) AS sale_date,
	COUNT(*) AS total
FROM Sales
GROUP BY LOWER(TRIM(product_name)), LEFT(sale_date, 7)
ORDER BY product_name, sale_date;
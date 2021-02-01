-- 找出下单数最多的顾客，列出customer_number。注意：结果只有一个值，不会存在多个值
-- 法一
SELECT customer_number FROM orders
GROUP BY customer_number
ORDER BY COUNT(*) DESC
LIMIT 1;


-- 法二
SELECT customer_number FROM orders 
GROUP BY customer_number
HAVING COUNT(customer_number) >= ALL 
(SELECT COUNT(customer_number) FROM orders GROUP BY customer_number);


-- 姗姗
SELECT DISTINCT a.customer_number FROM orders AS a
JOIN
(
SELECT customer_number, COUNT(order_number) AS num FROM orders
GROUP BY customer_number
) AS b
ON a.customer_number = b.customer_number
WHERE b.num >= ALL(SELECT COUNT(*) FROM orders
                   GROUP BY customer_number);
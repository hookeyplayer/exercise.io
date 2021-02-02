-- 查询所有客户的第一笔订单中即时订单的百分比，四舍五入到小数点后两位
-- 姗姗
SELECT 
ROUND(100 * COUNT(*)/(SELECT COUNT(DISTINCT customer_id)
	                  FROM Delivery),2) immediate_percentage
FROM Delivery a
JOIN (
	SELECT customer_id, MIN(order_date) first_order
	FROM Delivery
	GROUP BY customer_id
	) b
ON a.customer_id = b.customer_id
AND a.order_date = b.first_order
WHERE a.order_date = a.customer_pref_delivery_date


-- 法二
SELECT round(sum(tag)/count(id),2) immediate_percentage
FROM
(    
    SELECT customer_id id,
    	   CASE
    	   WHEN min(order_date) = min(customer_pref_delivery_date) THEN 100.00
    	   ELSE 0 
    	   END AS tag
    FROM Delivery d1
    GROUP BY customer_id
) d2;
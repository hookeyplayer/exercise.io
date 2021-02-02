-- user, item 和 order 3张表
-- 查询每个用户的加入日期和他们在2019年以买家身份下的订单数量
SELECT a.user_id buyer_id,
	   a.join_date,
	   COALESCE(b.orders_in_2019,0) orders_in_2019 
FROM Users a
LEFT JOIN (
	SELECT buyer_id, COUNT(order_id) orders_in_2019 
	FROM Orders
	WHERE YEAR(order_date) = 2019
	GROUP BY buyer_id
) b
ON a.user_id = b.buyer_id;

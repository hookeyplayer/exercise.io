-- 3个表
-- 查询每个用户出售的第二个商品的品牌（按日期）是否是他们最喜欢的品牌
-- 如果用户售出的商品少于两件，则将该用户的答案报告为否
-- 注意：没有卖家一天卖出一件以上的商品
SELECT a.user_id seller_id, COALESCE(CASE
	                                 WHEN a.favorite_brand = c.item_brand THEN 'yes'
	                                 ELSE 'no' END) 2nd_item_fav_brand 
FROM Users a
LEFT JOIN (SELECT seller_id, item_id 
	       FROM (SELECT seller_id, item_id, ROW_NUMBER() OVER(PARTITION BY seller_id 
	       	     ORDER BY order_date) rnk 
	             FROM Orders) tmp
	       WHERE rnk = 2
) b
ON a.user_id = b.seller_id
LEFT JOIN Items c
ON b.item_id = c.item_id;
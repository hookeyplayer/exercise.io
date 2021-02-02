-- 食物派送1张表
-- 如果客户的首选送货日期与订单日期相同，则该订单称为即时订单，否则称为计划订单
-- 查询表中即时订单的百分比，四舍五入到小数点后两位
SELECT
ROUND(100*(SELECT COUNT(*) 
	       FROM Delivery 
	       WHERE order_date = customer_pref_delivery_date) / (SELECT COUNT(*) FROM Delivery),2) immediate_percentage;
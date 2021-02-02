-- 书籍表和订单表
-- 假设今天是2019年6月23日，找出过去一年内销量少于10本的书籍编号及名称
-- 注意：排除上市时间小于一个月的书籍
SELECT book_id, name FROM Books 
WHERE available_from < DATE_SUB("2019-06-23", INTERVAL 1 MONTH)
AND book_id NOT IN (
	SELECT DISTINCT book_id FROM Orders
	WHERE dispatch_date > DATE_SUB("2019-06-23", INTERVAL 1 YEAR
)
GROUP BY book_id
HAVING SUM(quantity) >= 10);
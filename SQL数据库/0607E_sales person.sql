-- 3张表：雇员、公司、订单
-- 找出没有将产品卖给 'RED' 公司的员工名单
SELECT name FROM salesperson
WHERE sales_id NOT IN (
SELECT b.sales_id FROM company AS a
INNER JOIN orders AS b
ON a.com_id = b.com_id
WHERE a.name = 'RED'
);
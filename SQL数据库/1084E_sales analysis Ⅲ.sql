-- 查询只在 2019 年春季销售的产品编号及产品名称
SELECT DISTINCT a.product_id, b.product_name FROM Sales AS a
JOIN Product AS b
ON a.product_id = b.product_id
WHERE a.product_id NOT IN (SELECT product_id FROM Sales WHERE sale_date < '2019-01-01')
AND a.product_id NOT IN (SELECT product_id FROM Sales WHERE sale_date > '2019-03-31');
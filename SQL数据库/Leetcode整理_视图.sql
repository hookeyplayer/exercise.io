-- 创建视图
CREATE VIEW ProductSum(product_type, cnt_product)
AS
SELECT 
	product_type,
	COUNT(*)
FROM Product
GROUP BY product_type;

-- 使用视图，以视图为基础创建视图
CREATE VIEW ProductSumJim(product_type, cnt_product)
AS
SELECT 
	product_type,
	cnt_product
FROM ProductSum
WHERE product_type="办公用品";

SELECT
	product_type,
	cnt_product
FROM ProductSumJim;

-- 删除视图
DROP VIEW ProductSum;
-- 产品表和销售表
-- 查询全部总销售价格最高的销售员，返回其 seller_id
WITH tmp AS (
SELECT seller_id, RANK() OVER(ORDER BY SUM(price) DESC) AS rnk FROM Sales
GROUP BY seller_id
)

SELECT seller_id FROM tmp
WHERE rnk = 1;
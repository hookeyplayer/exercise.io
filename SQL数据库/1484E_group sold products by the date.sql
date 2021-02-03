-- 查询每个日期的不同产品的销售数量及其名称，每个日期中的已售产品名称应按字典顺序排序
-- 查询结果按 sell_date 升序排序
SELECT
sell_date,
COUNT(DISTINCT product) AS num_sold, 
GROUP_CONCAT(DISTINCT product ORDER BY product) AS products
FROM Activities
GROUP BY sell_date
ORDER BY sell_date;
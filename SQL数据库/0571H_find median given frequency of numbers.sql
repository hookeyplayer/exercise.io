-- 根据每个数字出现的频率找出中位数
-- 法一
SELECT AVG(Number) AS median
FROM 
(
select *, SUM(Frequency) OVER (ORDER BY Number) AS cum_sum, 
          (SUM(Frequency) OVER ())/2.0  AS mid
FROM Numbers
) AS temp
WHERE mid BETWEEN cum_sum - frequency AND cum_sum;


-- 姗姗
SELECT AVG(Number) as median
FROM 
(
select *, sum(Frequency) over (order by Number) as cum_sum,
          ROUND((sum(Frequency) over ())/2.0)  as mid1,
          (sum(Frequency) over ())/2.0 AS mid2,
          (sum(Frequency) over ())/2.0 + 1 as mid3,
          sum(Frequency) over () AS total
from Numbers
) AS temp  
WHERE 
CASE WHEN MOD(total,2) = 0 THEN
(mid2 > cum_sum - frequency and mid2 <= cum_sum)
OR (mid3 > cum_sum - frequency and mid3 <= cum_sum)
ELSE mid1 > cum_sum - frequency and mid1 <= cum_sum
END;
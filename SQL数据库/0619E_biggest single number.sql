-- 查找最大的数字，该数字只出现一次
-- 注意：如果没有这样的数字，则仅输出 null
SELECT MAX(num) AS num FROM
(
SELECT num FROM my_numbers
GROUP BY num
HAVING COUNT(*) = 1
) AS x;
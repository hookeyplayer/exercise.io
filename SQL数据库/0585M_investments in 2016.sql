-- 查找2016年的投资总额，其中需要满足如下两个条件：

-- 2015年投资额不是唯一值 (至少两个政策制定者在2015年的投资额是相等的)
-- 位置是唯一的 (即经度和纬度的组合没有重复值)
-- 法一
SELECT SUM(TIV_2016) TIV_2016
FROM insurance
WHERE TIV_2015 IN 
(SELECT TIV_2015 FROM insurance 
 GROUP BY TIV_2015 
 HAVING COUNT(*) > 1)
AND (lat, lon) IN 
(SELECT lat, lon FROM insurance 
 GROUP BY lat, lon 
 HAVING COUNT(*)=1);


-- 法二
SELECT SUM(insurance.TIV_2016) AS TIV_2016
FROM insurance
WHERE insurance.TIV_2015 IN
(SELECT TIV_2015 FROM insurance
 GROUP BY TIV_2015
 HAVING COUNT(*) > 1)
AND CONCAT(LAT, ",", LON) IN
(SELECT CONCAT(LAT, ",", LON) FROM insurance
 GROUP BY LAT , LON
 HAVING COUNT(*) = 1);


-- 法三
SELECT SUM(a.TIV_2016) AS TIV_2016 FROM insurance AS a
JOIN
(
SELECT LAT, LON FROM insurance
GROUP BY LAT, LON
HAVING COUNT(*) = 1 
) AS b
ON a.LAT = b.LAT
AND a.LON = b.LON
WHERE a.TIV_2015 IN
(SELECT DISTINCT TIV_2015 FROM insurance
GROUP BY TIV_2015
HAVING COUNT(*) > 1);
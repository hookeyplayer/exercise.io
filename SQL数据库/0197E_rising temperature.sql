-- 返回 比前一天温度高的 id
-- 表信息：三列，id+日期+温度

-- 法一
SELECT a.id FROM Weather AS a
JOIN Weather AS b
ON a.recordDate = ADDDATE(b.recordDate, INTERVAL 1 DAY)
WHERE a.temperature > b.temperature;


-- 法二
SELECT a.id FROM Weather AS a 
JOIN Weather AS b 
ON a.recordDate = DATE_ADD(b.recordDate, INTERVAL 1 DAY) 
WHERE a.temperature > b.temperature;


-- 法三
SELECT a.id FROM Weather AS a
JOIN Weather AS b
ON b.recordDate = SUBDATE(a.recordDate, INTERVAL 1 DAY)
WHERE a.temperature > b.temperature;


-- 法四
SELECT a.id FROM Weather AS a
JOIN Weather AS b
ON DATEDIFF(a.recordDate, b.recordDate) = 1
WHERE a.temperature > b.temperature


-- 法五
SELECT a.id FROM Weather AS a  
JOIN Weather AS b  
ON b.recordDate = DATE_SUB(a.recordDate, INTERVAL 1 DAY)  
WHERE a.temperature > b.temperature;
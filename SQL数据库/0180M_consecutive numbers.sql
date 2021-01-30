-- 找出连续出现三次及以上的数字

-- 法一：多次联结
SELECT DISTINCT a.Num AS ConsecutiveNums FROM Logs AS a
INNER JOIN Logs AS b ON  a.Id + 1 = b.Id
INNER JOIN Logs AS c ON a.Id + 2 = c.Id
WHERE a.Num = b.Num
AND b.Num = c.Num;


-- 法二：lead()/LAG()
SELECT DISTINCT Num AS ConsecutiveNums FROM (
SELECT Num, 
LEAD(Num,1) OVER(ORDER BY id) AS lead1,
LEAD(Num,2) OVER(ORDER BY id) AS lead2
FROM Logs
) AS lg
WHERE Num = lead1
AND Num = lead2
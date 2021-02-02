-- 找出连续出现三次及以上的数字

-- 法一：多次联结
SELECT DISTINCT a.Num AS ConsecutiveNums FROM Logs AS a
INNER JOIN Logs AS b ON  a.Id + 1 = b.Id
INNER JOIN Logs AS c ON a.Id + 2 = c.Id
WHERE a.Num = b.Num
AND b.Num = c.Num;

-- 法二
SELECT DISTINCT
    l1.Num AS ConsecutiveNums
FROM
    Logs l1,
    Logs l2,
    Logs l3
WHERE
    l1.Id = l2.Id - 1
    AND l2.Id = l3.Id - 1
    AND l1.Num = l2.Num
    AND l2.Num = l3.Num


-- 法三：lead()/LAG()
SELECT DISTINCT Num AS ConsecutiveNums FROM (
SELECT Num, 
LEAD(Num,1) OVER(ORDER BY id) AS lead1,
LEAD(Num,2) OVER(ORDER BY id) AS lead2
FROM Logs
) AS lg
WHERE Num = lead1
AND Num = lead2

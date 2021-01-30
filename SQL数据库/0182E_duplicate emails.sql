-- 查询重复的邮箱
-- 法一：having
SELECT Email FROM Person
GROUP BY Email
HAVING COUNT(Id) > 1;


-- 法二：子查询
SELECT Email FROM
 (SELECT Email, COUNT(id) AS num
  FROM Person
  GROUP BY Email) AS tmp
WHERE num > 1;


-- 法三：自联结
SELECT DISTINCT a.Email FROM Person AS a
JOIN Person AS b
ON a.Email = b.Email
AND a.Id <> b.Id;
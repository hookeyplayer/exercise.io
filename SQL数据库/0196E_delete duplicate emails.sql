-- 删除邮件重复的行，当有重复值时，保留Id最小的行
-- 法一
DELETE p1 FROM Person p1, Person p2
WHERE p1.Email = p2.Email AND p1.Id > p2.Id;


-- 法二
DELETE FROM Person
WHERE Id NOT IN
(SELECT MinId FROM
 (SELECT Email, MIN(Id) AS MinId FROM Person
  GROUP BY Email) AS tmp);


-- 法三
DELETE FROM Person
WHERE Id IN
(SELECT a.Id FROM (SELECT * FROM Person) AS a
 INNER JOIN (SELECT * FROM Person) AS b
 ON a.Id > b.Id AND a.Email = b.Email);
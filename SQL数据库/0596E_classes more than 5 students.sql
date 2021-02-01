-- 列出至少有5名学生的课程名称
-- 每个学生只算作一次
-- 法一
-- 子查询
SELECT class FROM
(SELECT class, COUNT(DISTINCT student) AS num
 FROM courses
 GROUP BY class) AS temp_table
WHERE num >= 5;


-- 法二
SELECT class FROM courses
GROUP BY class
HAVING COUNT(DISTINCT student) >= 5;
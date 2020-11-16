-- 表的名称叫courses
-- 列出至少有5名学生的课程名称
-- 其中两列：student和class

-- 方法一
SELECT class 
FROM courses
GROUP BY class
HAVING COUNT(DISTINCT student) >= 5;

-- 方法二
SELECT class FROM
(SELECT class, COUNT(DISTINCT student) AS num
 FROM courses
 GROUP BY class) AS temp_table
WHERE num >= 5;

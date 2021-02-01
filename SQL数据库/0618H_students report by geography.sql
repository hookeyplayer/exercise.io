-- 旋转student表中的大洲列，以便每个学生名按字母顺序显示在其对应大洲下
-- 输出标题应分别为美洲，亚洲和欧洲
-- 已知来自美国的学生人数不少于亚洲或欧洲
-- 法一
WITH continent_pivot AS
(
SELECT
CASE WHEN continent = 'America' THEN name END AS 'America',
CASE WHEN continent = 'Asia' THEN name END AS 'Asia',
CASE WHEN continent = 'Europe' THEN name END AS 'Europe',
ROW_NUMBER() OVER(PARTITION BY continent ORDER BY name) AS rk
FROM student
)

SELECT
MAX(America) AS America,
MAX(Asia) AS Asia,
MAX(Europe) AS Europe
FROM continent_pivot
GROUP BY rk;


-- 法二
SELECT America, Asia, Europe
FROM
(SELECT @r1 := 0, @r2 := 0, @r3 := 0) AS t,
(
SELECT @r1:= @r1 + 1 AS rowid, name AS America
FROM student
WHERE continent = 'America'
ORDER BY name
) AS t1
LEFT JOIN
(
SELECT @r2:= @r2 + 1 AS rowid, name AS Asia
FROM student
WHERE continent = 'Asia'
ORDER BY name
) AS t2
ON t1.rowid = t2.rowid
LEFT JOIN
(
SELECT @r3:= @r3 + 1 AS rowid, name AS Europe
FROM student
WHERE continent = 'Europe'
ORDER BY name
) AS t3
ON t1.rowid = t3.rowid;
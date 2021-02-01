-- 找到国土面积大于300万平方公里或人口数超过2500万的国家，并显示人口数和国土面积
-- 法一
SELECT name, population, area FROM World
WHERE area > 3000000
OR population > 25000000;


-- 法二
-- exists()判断查询子句中是否有记录
SELECT name, population, area
FROM World
WHERE EXISTS (
SELECT population, area
WHERE (population > 25000000) OR (area > 3000000)
);


-- 法三
-- slow
SELECT name, population, area
FROM World
WHERE area > 3000000
UNION
SELECT name, population, area
FROM World
WHERE population > 25000000;

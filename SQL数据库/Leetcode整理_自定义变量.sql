-- 已有的表是姓名和大洋洲
-- 旋转，以便每个学生名按字母顺序显示在其对应大洲下
-- 输出标题应分别为美洲，亚洲和欧洲
-- 已知来自美国的学生人数不少于亚洲或欧洲
-- 自定义函数
SELECT 
	America, 
	Asia, 
	Europe
FROM (SELECT 
		@r1 := 0,
		@r2 := 0, 
		@r3 := 0
		) AS t,
	(SELECT 
		@r1:= @r1 + 1 AS rowid,
		name AS America
	FROM student
	WHERE continent = 'America'
	ORDER BY name
	) AS t1
LEFT JOIN (
	SELECT
		@r2:= @r2 + 1 AS rowid,
		name AS Asia
	FROM student
	WHERE continent = 'Asia'
	ORDER BY name
	) AS t2
ON t1.rowid = t2.rowid
LEFT JOIN (
	SELECT 
		@r3:= @r3 + 1 AS rowid,
		name AS Europe
	FROM student
	WHERE continent = 'Europe'
	ORDER BY name
	) AS t3
ON t1.rowid = t3.rowid;

-- 找出两点之间最短距离
SELECT MIN(ABS(a.x - b.x)) AS shortest
FROM point AS a
JOIN point AS b
ON a.x <> b.x;

-- 不懂
SELECT MIN(dis) AS shortest
FROM (
	SELECT 
		@dis := if(@last_p IS NULL, NULL, x - @last_p) AS dis, 
		@last_p := x
	FROM 
		point,
		(SELECT 
			@dis := NULL, 
			@last_p := NULL) AS temp
		ORDER BY x ASC
	) AS a;
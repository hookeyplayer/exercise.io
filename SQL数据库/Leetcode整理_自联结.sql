-- (business_id, eventtype) 联合主键
-- 查询所有活跃商家 (active business)，返回其编号
-- 活跃商家：至少有一个 event_type 出现的频率高于该类 event_type 出现的平均频率
SELECT business_id 
FROM (
    SELECT 
        a.business_id,
        a.event_type,
        a.occurences,
        b.avg_occ 
    FROM Events AS a
    LEFT JOIN (SELECT event_type, AVG(occurences) AS avg_occ 
    FROM Events 
    GROUP BY event_type) AS b
    ON a.event_type = b.event_type
    ) AS tmp
WHERE occurences > avg_occ
GROUP BY business_id
HAVING COUNT(*) > 1;


-- 坐标点最短距离
SELECT ROUND(MIN(SQRT(POW(a.x - b.x, 2) + POW(a.y - b.y, 2))),2) AS shortest
FROM point_2d AS a
JOIN point_2d AS b
ON a.x <> b.x OR a.y <> b.y;

-- 给定数字的频率查询中位数
-- 不太懂
SELECT AVG(Number) AS median
FROM (
    SELECT N1.Number
    FROM Numbers AS N1
    JOIN Numbers AS N2 
    ON N1.Number >= N2.Number
    GROUP BY N1.Number
    HAVING SUM(N2.Frequency) >= (SELECT SUM(Frequency) FROM Numbers) / 2 
    AND SUM(N2.Frequency) - AVG(N1.Frequency) <= (SELECT SUM(Frequency) FROM Numbers) / 2) AS T;


-- 查询每个用户首次登陆的日期所使用的设备
-- 不太懂
SELECT 
    a.player_id,
    a.device_id 
FROM Activity AS a
INNER JOIN (SELECT
                player_id,
                MIN(event_date) AS first_login
            FROM Activity
            GROUP BY player_id
            ORDER BY player_id) AS b
ON a.player_id = b.player_id AND a.event_date = b.first_login
ORDER BY a.player_id;


-- 找出连续出现三次及以上的数字
-- 多次联结
SELECT DISTINCT a.Num AS ConsecutiveNums 
FROM Logs AS a
INNER JOIN Logs AS b 
ON  a.Id + 1 = b.Id
INNER JOIN Logs AS c 
ON a.Id + 2 = c.Id
WHERE a.Num = b.Num AND b.Num = c.Num;
-- 法二
SELECT DISTINCT a1.Num AS ConsecutiveNums
FROM
    Logs a1,
    Logs a2,
    Logs a3
WHERE
    a1.Id = a2.Id - 1
    AND a2.Id = a3.Id - 1
    AND a1.Num = a2.Num
    AND a2.Num = a3.Num;



-- 将每个用户首次登录的日期定义为安装日
-- 查询每个安装日，安装的人数以及安装日的留存率
-- 安装日的留存率 = 安装日后的第一天登录的用户比例/安装日安装的用户数
SELECT a.install_dt, 
COUNT(a.player_id) AS installs,
ROUND(COUNT(b.player_id)/COUNT(a.player_id),2) AS Day1_retention 
FROM (
	SELECT DISTINCT player_id, 
	FIRST_VALUE(event_date) OVER(
		PARTITION BY player_id 
		ORDER BY event_date
		) AS install_dt 
	FROM Activity) AS a
LEFT JOIN Activity AS b
ON a.player_id = b.player_id AND DATEDIFF(b.event_date, a.install_dt) = 1
GROUP BY a.install_dt;


-- 两张表，Employee 和 Department
-- 查询每个部门中薪水最高的员工姓名和薪水
SELECT b.Name AS Department, a.Name AS Employee, a.Salary AS 'Salary' 
FROM Employee AS a
INNER JOIN Department AS b
ON a.DepartmentId = b.Id
WHERE a.Salary IN (
	SELECT MAX(Salary) 
	FROM Employee AS c 
	WHERE a.DepartmentId = c.DepartmentId 
	GROUP BY c.DepartmentId
	);


-- 任意两点组成的所有可能的矩形，结果的每一行包含三列（p1，p2，area）
-- p1和p2是矩形的两个对角的坐标，且p1 <p2
SELECT a.id AS p1, b.id AS p2, ABS(a.x_value - b.x_value) * ABS(a.y_value - b.y_value) AS area
FROM Points AS a
LEFT JOIN Points AS b
ON a.id < b.id
WHERE ABS(a.x_value - b.x_value) <> 0 AND ABS(a.y_value - b.y_value) <> 0
ORDER BY area DESC, p1, p2;


-- 找出连续座位的编号
-- 不太懂
SELECT DISTINCT a.seat_id
FROM cinema AS a 
JOIN cinema AS b
ON ABS(a.seat_id - b.seat_id) = 1 AND a.free = TRUE AND b.free = TRUE
ORDER BY a.seat_id;


-- 查询收入第二高的员工薪水，若无则null
-- shanshan解法，不太懂
SELECT (
 SELECT 
 DISTINCT a.Salary 
 FROM Employee AS a
 JOIN Employee AS b
 ON a.Salary < b.Salary
 GROUP BY  a.Id
 HAVING COUNT(a.Id) = 1) 
AS SecondHighestSalary;


-- 删除邮件重复的行，当有重复值时，保留Id最小的行
-- 不太懂
DELETE FROM Person
WHERE Id IN (
	SELECT a.Id 
	FROM (SELECT * FROM Person) AS a
	INNER JOIN (SELECT * FROM Person) AS b
	ON a.Id > b.Id AND a.Email = b.Email); 


-- 查询重复的邮箱
SELECT DISTINCT a.Email 
FROM Person AS a
JOIN Person AS b
ON a.Email = b.Email AND a.Id <> b.Id;


-- 查出薪水比其经理薪水高的员工姓名
-- 法一
SELECT a.Name AS 'Employee' 
FROM Employee AS a
JOIN Employee AS b
ON a.ManagerId = b.Id
WHERE a.Salary > b.Salary;
-- 法二
-- 不太懂
SELECT a.Name AS 'Employee'
FROM Employee AS a, Employee AS b
WHERE a.ManagerId = b.Id AND a.Salary > b.Salary;
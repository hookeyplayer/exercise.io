-- friend_request(sender_id, send_to_id, requester_id)
-- request_accepted(requester_id, accepter_id, accept_date)
-- 找出申请通过率，结果保留两位小数
SELECT ROUND(IFNULL((
	SELECT COUNT(*) FROM (SELECT DISTINCT requester_id, accepter_id FROM request_accepted) AS A) / (
	SELECT COUNT(*) FROM (SELECT DISTINCT sender_id, send_to_id FROM friend_request) AS B), 0), 2) AS accept_rate;


-- 2张表
-- actions(user_id, post_id, action_date, action, extra)
-- removals(post_id, remove_date)
-- 查询被举报为垃圾邮件后被删除的帖子每日平均百分比，四舍五入到小数点后两位
SELECT ROUND(AVG(percentage),2) AS average_daily_percent
FROM (
	SELECT 
		action_date, 
		(COUNT(DISTINCT b.post_id)/COUNT(DISTINCT a.post_id))*100 AS percentage 
	FROM Actions AS a
	LEFT JOIN Removals AS b
	ON a.post_id = b.post_id
	WHERE a.action = 'report' AND a.extra = 'spam'
	GROUP BY a.action_date
	) AS tmp;


-- 按照日期，查询每个用户累积玩的游戏数
-- 不懂
SELECT
	a.player_id,
	a.event_date,
	(SELECT SUM(games_played) 
	 FROM Activity AS b
	 WHERE a.player_id = b.player_id AND a.event_date >= b.event_date
	 ) AS games_played_so_far
FROM Activity AS a;


-- 找出连续出现三次及以上的数字
SELECT DISTINCT Num AS ConsecutiveNums 
FROM (
	SELECT Num, LEAD(Num,1) OVER(ORDER BY id) AS lead1, LEAD(Num,2) OVER(ORDER BY id) AS lead2 FROM Logs) AS lg
WHERE Num = lead1 AND Num = lead2;


-- 列出至少有5名学生的课程名称
-- 每个学生只算作一次
SELECT class 
FROM (
	SELECT class, COUNT(DISTINCT student) AS num
	FROM courses
	GROUP BY class) AS temp_table
WHERE num >= 5;


-- 两张表candidate和vote
-- 找到当选者的名字
-- 注意：本题目中不考虑平票的情况
SELECT Name 
FROM Candidate 
WHERE id=(
	SELECT CandidateId 
	FROM Vote 
	GROUP BY CandidateId 
	ORDER BY COUNT(*) DESC 
	LIMIT 1);


-- 查询出至少管理5个员工的经理的名称
-- 子查询
SELECT Name 
FROM Employee 
WHERE Id IN (
	SELECT ManagerId 
	FROM Employee 
	GROUP BY ManagerId 
	HAVING COUNT(*)>=5);


-- 根据每个数出现的频率找出中位数
-- 不太懂
SELECT AVG(Number) AS median
FROM (
	SELECT *, 
	SUM(Frequency) OVER (ORDER BY Number) AS cum_sum),
	(SUM(Frequency) OVER ())/2.0 AS median 
	FROM Numbers
	) AS temp
WHERE mid BETWEEN cum_sum - Frequency AND cum_sum;


-- 查询截至2020年5月27日（含）的30天期间的每日活动用户数
-- 如果某天至少进行了一项活动，则该用户在某天是活跃的
-- DATE_SUB возвращает дату, после которой вычитается определенный интервал даты/времени.
SELECT activity_date AS day, COUNT(DISTINCT user_id) AS active_users 
FROM (
	SELECT DISTINCT activity_date, user_id 
	FROM Activity
	WHERE activity_date > DATE_SUB("2020-05-27", INTERVAL 30 DAY)
	GROUP BY activity_date, user_id
	HAVING COUNT(DISTINCT activity_type) >= 1
) AS tmp
GROUP BY activity_date;


-- 两张表：顾客表和订单表
-- 找出没有下过订单的顾客姓名
SELECT name AS 'Customers' FROM Customers
WHERE Id NOT IN
 (SELECT CustomerId FROM Orders);

 -- 查询重复的邮箱
SELECT Email 
FROM (
	SELECT Email, COUNT(id) AS num 
	FROM Person 
	GROUP BY Email
	) AS tmp 
WHERE num > 1;


-- 查询收入第二高的员工薪水，若无则null
-- 必须加 DISTINCT, 否则当不止一个人有第二高薪水的时候会返回多个值
-- 法一
SELECT (
	SELECT DISTINCT Salary 
	FROM Employee 
	ORDER BY Salary DESC 
	LIMIT 1 
	OFFSET 1) 
As SecondHighestSalary;
-- 法二
SELECT MAX(Salary) AS SecondHighestSalary 
FROM Employee
WHERE Salary NOT IN (SELECT MAX(Salary) FROM Employee);
-- 或者
SELECT MAX(Salary) AS SecondHighestSalary 
FROM Employee
WHERE Salary < (SELECT MAX(Salary) FROM Employee);


-- 查询最高（子查询）
SELECT name, id 
FROM Employee 
WHERE Salary=(SELECT MAX(Salary) FROM Employee);
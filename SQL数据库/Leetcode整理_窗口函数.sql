-- 1. 分组排序
-- 1.1 ROW_NUMBER() 在排序相同时不重复，会根据顺序排序
SELECT 
	*,
	ROW_NUMBER() OVER (PARTITION BY department ORDER BY cost DESC) AS row_number_result
FROM table;

-- 找出各公司薪水的中位数 569 不懂
WITH t AS(
	SELECT 
		*, 
		ROW_NUMBER() OVER(PARTITION BY Company ORDER BY Salary) AS num
	FROM Employee
	),

t1 AS (
	SELECT 
		Company AS company_id, 
		MAX(num)/2 AS criteria_1, 
		MAX(num)/2+1 AS criteria_2, 
		ROUND(MAX(num)/2) AS criteria_3
	FROM t
	GROUP BY Company
	),

t2 AS (
	SELECT * FROM t 
	LEFT JOIN t1 
	ON t.Company = t1.company_id
	)

SELECT Id,Company,Salary
FROM t2
WHERE num = criteria_1 OR num = criteria_2 OR num = criteria_3;

-- 3个表
-- user(user_id, join_date, favorite_brand),
-- order(order_id, order_date, item_id, buyer_id, seller_id)
-- item(item_id, item_brand)
-- 查询每个用户出售的第二个商品的品牌（按日期）是否是他们最喜欢的品牌
-- 如果用户售出的商品少于两件，则将该用户的答案报告为否
-- 注意：没有卖家一天卖出一件以上的商品
-- 不懂
SELECT 
	a.user_id AS seller_id,
	COALESCE(CASE WHEN a.favorite_brand = c.item_brand THEN 'yes' ELSE 'no' END) AS 2nd_item_fav_brand 
FROM Users AS a
LEFT JOIN (
	SELECT 
		seller_id,
		item_id 
	FROM (
		SELECT 
			seller_id,
			item_id, 
			ROW_NUMBER() OVER(PARTITION BY seller_id ORDER BY order_date) AS rnk 
		FROM Orders
		) AS tmp
	WHERE rnk = 2
	) AS b
ON a.user_id = b.seller_id
LEFT JOIN Items AS c
ON b.item_id = c.item_id;

-- 联合主键(student_id, course_id)
-- 查询每个学生的最高成绩及其相应的课程
-- 如果最高成绩相同则，输出课程编号最小的课程
-- 查询结果按照 student_id 升序排列
SELECT 
	student_id, 
	course_id, 
	grade 
FROM (
	SELECT 
		*,
		ROW_NUMBER() OVER (PARTITION BY student_id ORDER BY grade DESC, course_id ASC) AS grade_rnk
	FROM Enrollments
	) AS tmp
WHERE grade_rnk = 1
ORDER BY student_id;

-- 已有的表是姓名和大洋洲
-- 旋转，以便每个学生名按字母顺序显示在其对应大洲下
-- 输出标题应分别为美洲，亚洲和欧洲
-- 已知来自美国的学生人数不少于亚洲或欧洲
-- 不懂
WITH continent_pivot AS (
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

-- 查询出每个员工三个月的累积工资，其中不包含最近一个月，且按照员工id升序排列，月份降序排列
WITH s AS (
	SELECT 
		Id AS id,
		Month AS month, 
		Salary, 
		Sum(Salary) OVER (PARTITION BY id ORDER BY Month) AS SumSal,
		ROW_NUMBER() OVER (PARTITION BY id ORDER BY id ASC, month DESC) AS rn
	FROM Employee
	)
SELECT 
	Id,
	Month,
	SumSal AS Salary
FROM s
WHERE rn > 1;

-- 1.2 RANK()排序相同时会重复，总数不会变 ，会出现1、1、3这样的排序结果
SELECT 
	*,
	RANK() OVER (PARTITION BY department ORDER BY cost DESC) AS rank_result
FROM table;


-- Customers(customer_id, name)
-- Orders(order_id, order_date, customer_id, product_id)
-- Products(product_id, product_name, price)
-- 查询每个产品的最新订单，查询结果按 product_name，product_id，以及 order_id 升序排列
WITH tmp AS (
	SELECT
		a.product_name,
		a.product_id,
		b.order_id,
		b.order_date,
		RANK() OVER(PARTITION BY a.product_name, a.product_id ORDER BY b.order_date DESC) AS rnk
	FROM Products a
	JOIN Orders b
	ON a.product_id = b.product_id
	)
SELECT
	product_name,
	product_id,
	order_id,
	order_date
FROM tmp
WHERE rnk = 1
ORDER BY product_name, product_id, order_id;

-- 2个表，项目和员工
-- 查询每个项目中所有最有经验的员工
WITH t AS (
	SELECT 
		a.project_id, 
		a.employee_id, 
		RANK() OVER(PARTITION BY a.project_id ORDER BY b.experience_years DESC) AS exp
	FROM Project AS a
	LEFT JOIN Employee AS b
	ON a.employee_id = b.employee_id
	)
SELECT 
	project_id,
	employee_id
FROM t
WHERE exp = 1;

-- 2个表，项目和员工
-- 查询员工最多的项目
SELECT project_id
FROM (
	SELECT 
		project_id,
		RANK() OVER (ORDER BY COUNT(employee_id) DESC) AS r
	FROM Project
	GROUP BY project_id 
	) AS a
WHERE r = 1;

-- 3个表
-- user(user_id, join_date, favorite_brand),
-- order(order_id, order_date, item_id, buyer_id, seller_id)
-- item(item_id, item_brand)
-- 查询每个用户出售的第二个商品的品牌（按日期）是否是他们最喜欢的品牌
-- 如果用户售出的商品少于两件，则将该用户的答案报告为否
-- 注意：没有卖家一天卖出一件以上的商品
WITH tmp AS (
	SELECT
		o.seller_id, 
		i.item_brand, 
		RANK() over (PARTITION BY o.seller_id ORDER BY o.order_date) AS 'rk'
    FROM Orders AS o
    JOIN Items AS i
    on o.item_id = i.item_id
    )

SELECT 
	u.user_id AS 'seller_id', 
	IF (t.item_brand IS null OR u.favorite_brand != t.item_brand, 'no', 'yes') AS '2nd_item_fav_brand'
FROM Users AS u
LEFT JOIN tmp AS t
ON u.user_id = t.seller_id AND t.rk = 2
ORDER BY u.user_id;


-- 查询每个用户首次登陆的日期所使用的设备
SELECT
	player_id, 
	device_id 
FROM (
	SELECT 
		player_id,
		device_id, 
		RANK() OVER (PARTITION BY player_id ORDER BY event_date) AS rnk
    FROM Activity
    ) AS tmp
WHERE rnk = 1;

-- 产品表和销售表
-- 查询全部总销售价格最高的销售员，返回其 seller_id
WITH tmp AS (
	SELECT 
		seller_id, 
		RANK() OVER(ORDER BY SUM(price) DESC) AS rnk 
	FROM Sales 
	GROUP BY seller_id
	)
SELECT seller_id 
FROM tmp
WHERE rnk = 1;


-- 1.3 DENSE_RANK() 排序相同时会重复，总数会减少，意思是会出现1、1、2这样的排序结果
SELECT 
	*,
	DENSE_RANK() OVER (PARTITION BY department ORDER BY cost DESC) AS dense_rank_result
FROM table;

-- 成绩由高到低排序，并列出排名
-- 当两个人获得相同分数时，取并列名次，且名次中无断档
SELECT 
	*, 
	DENSE_RANK() OVER(ORDER BY Score DESC) AS 'Rank'
FROM Scores; 

-- 查询每个客户订购最频繁的产品
-- Customers(customer_id, name)
-- Orders(order_id, order_date, customer_id, product_id)
-- Products(product_id, product_name, price)
-- 结果表应具有至少订购了一个订单的每个 customer_id 的 product_id 和 product_name
-- 不懂
WITH tmp AS (
	SELECT 
		a.customer_id,
		b.product_id,
		c.product_name,
		COUNT(b.order_id) OVER(PARTITION BY a.customer_id, b.product_id) AS freq
	FROM Customers AS a
	JOIN Orders AS b
	ON a.customer_id = b.customer_id
	JOIN Products AS c
	ON b.product_id = c.product_id
	),

tmp1 AS (
	SELECT 
		customer_id,
		product_id, 
		product_name,
		freq,
		DENSE_RANK() OVER(PARTITION BY customer_id ORDER BY freq DESC) AS rnk
	FROM tmp
	)

SELECT 
	DISTINCT customer_id, 
	product_id, 
	product_name 
FROM tmp1
WHERE rnk = 1;


-- Employee, Department两张表
-- 查询各部门薪水排名前三的员工姓名和薪水
-- 若有并列相同的薪水，则一样返回

SELECT 
	x.Department,
	x.Employee, 
	x.Salary
FROM (
	SELECT 
		b.Name AS Department, 
        a.Name AS Employee, 
        a.Salary AS Salary, 
        DENSE_RANK() OVER (PARTITION BY b.Name ORDER BY a.Salary DESC) AS dept_rank
    FROM Employee AS a
    INNER JOIN Department AS b
    ON a.DepartmentId = b.Id) AS x
WHERE x.dept_rank <= 3;


-- 2. 分组取最大最小
-- 2.1 FIRST_VALUE取的是分组内排序后，截止到当前行第一个值
-- 返回每个组里cost最多和最少的人的名字
SELECT 
	*,
	FIRST_VALUE(name) OVER(PARTITION BY department ORDER BY cost DESC) AS max_cost_user,
	FIRST_VALUE(name) OVER(PARTITION BY department ORDER BY cost) AS min_cost_user
FROM table;

-- 返回最高工资
SELECT DISTINCT FIRST_VALUE(salary) OVER(ORDER BY salary DESC RANGE BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) AS "HIGHEST"
FROM employees;


-- 按部门的最高工资
SELECT 
    DISTINCT department_id, 
    FIRST_VALUE(salary) OVER(PARTITION BY department_id ORDER BY salary DESC RANGE BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) AS "HIGHEST"
FROM employees
WHERE department_id in (10,20)
ORDER BY department_id;


-- traffic表没有主键，所以有重复行可能
-- traffic(user_id, activity, activity_date)
-- 假设今天是2019年6月30日，找出90天之内第一次登录 (login) 的日期的用户数
SELECT 
	login_date, 
	COUNT(user_id) AS user_count
FROM (
	SELECT 
		DISTINCT user_id, 
		FIRST_VALUE(activity_date) OVER (PARTITION BY user_id ORDER BY activity_date) AS login_date 
	FROM Traffic
	WHERE activity = 'login'
	) AS tmp
WHERE DATEDIFF("2019-06-30", login_date) <= 90
GROUP BY login_date;

-- 查询首次登录后第二天也登录的用户比例
-- 不懂
SELECT ROUND(COUNT(DISTINCT b.player_id)/COUNT(DISTINCT a.player_id), 2) AS fraction 
FROM Activity AS a
LEFT JOIN (
	SELECT
		player_id,
		FIRST_VALUE(event_date) OVER(PARTITION BY player_id ORDER BY event_date) AS first_login 
		FROM Activity) AS b
ON a.player_id = b.player_id AND DATEDIFF(a.event_date, b.first_login) = 1;


-- 2.2 LAST_VALUE取的是分组内排序后，截止到当前行最后一个值

-- 3. 累积百分比
-- 3.1 CUME_DIST() 返回的是小于等于当前值的行数/分组内总行数，倒序排的话，也就是大于等于了。
-- 3.2 SUM() OVER:累积值的占比。
返回A部门的cost由高到低排序，？%的人累积贡献了？%。
SELECT
	*,
	CUME_DIST() OVER (PARTITION BY department ORDER BY cost DESC) AS cum_dist,
	SUM(cost) OVER (PARTITION BY department ORDER BY cost DESC) / SUM(cost) OVER (PARTITION BY department) AS sum_over
FROM table
WHERE department='A';


-- 4. 错位
-- 4.1 LEAD用于统计窗口内往下第n行值
-- 和比他们花费排名更高一名的值
SELECT 
	*,
	LEAD(cost) OVER (PARTITION BY department ORDER BY cost) AS next_cost,
FROM table;

-- 获取用户在某个页面停留的起始\结束时间\时间间隔
SELECT
	user_id,
	visit_time AS stime,
	LEAD(visit_time) OVER(PARTITION BY user_id ORDER BY visit_time) AS etime,
	UNIX_TIMESTAMP(LEAD(visit_time) OVER(PARTITION BY user_id ORDER BY visit_time), 'yyyy-MM-dd HH:mm:ss')- UNIX_TIMESTAMP(visit_time, 'yyyy-MM-dd HH:mm:ss') AS period,
	url
FROM table;

-- 计算每个页面停留的总时间，某个用户访问某个页面的总时间
-- 不懂
SELECT 
	NVL(url, '-1') AS url_name,
	NVL(user_id, '-1') AS user_name,
	SUM(period) AS total_period 
FROM (
	SELECT 
		user_id,
		visit_time AS stime,
		LEAD(visit_time) OVER (PARTITION BY user_id ORDER BY visit_time) AS etime,
		UNIX_TIMESTAMP(LEAD(visit_time) OVER(PARTITION BY user_id ORDER BY visit_time), 'yyyy-MM-dd HH:mm:ss')- UNIX_TIMESTAMP(visit_time, 'yyyy-MM-dd HH:mm:ss') AS period,
		url 
	FROM table) AS a
GROUP BY url, user_id WITH ROLLUP;

-- 4.2 LAG(field, num, defaultvalue)，用于统计窗口内往上第n行值，在一次查询中取出当前行的同一字段（field参数）的前面第num行的数据，如果没有用defaultvalue代替
-- 返回前一天抄表值, pq是抄表值
SELECT 
	name,
	checkdate,
	pq,
	LAG(pq, 1, 0) OVER(PARTITION BY name ORDER BY checkdate DESC) AS pq1
FROM table;

-- 找出连续出现三次及以上的数字
SELECT DISTINCT Num AS ConsecutiveNums 
FROM (
	SELECT 
		Num, 
		LEAD(Num,1) OVER(ORDER BY id) AS lead1,
		LEAD(Num,2) OVER(ORDER BY id) AS lead2
	FROM Logs) AS lg
WHERE Num = lead1 AND Num = lead2;


-- 查询各公司员工的税后工资工资，四舍五入
-- 如果公司中员工的最高薪水少于1000 $，则税率为 0%。
-- 如果公司中员工的最高薪水在[1000，10000]范围内，则税率为 24%。
-- 如果公司中员工的最高薪水大于10000 $，则税率为 49%。
-- 以任何顺序返回结果表。将薪水四舍五入到最接近的整数。
WITH tmp AS (
	SELECT
		company_id,
		employee_id,
		employee_name,
		salary, 
		MAX(salary) OVER(PARTITION BY company_id) AS max_sal
	FROM Salaries   
	)

SELECT 
	company_id,
	employee_id,
	employee_name,
	CASE 
		WHEN max_sal < 1000  
		THEN ROUND(salary) 
		WHEN max_sal BETWEEN 1000 AND 10000 
		THEN ROUND(salary * (1-0.24))
		ELSE ROUND(salary * (1-0.49))
	END AS salary
FROM tmp;


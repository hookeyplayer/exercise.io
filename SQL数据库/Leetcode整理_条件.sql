-- 过滤分组：WHERE在数据分组之前过滤行，不是分组的概念。 HAVING在数据分组之后进行过滤。所有WHERE都可以用HAVING替代。

-- 查询在同一日期查看过不止一篇文章的所有用户，并按ID升序排列
-- Views(article_id, author_id, viewer_id, view_date)
SELECT DISTINCT viewer_id AS id
FROM (
	SELECT 
		viewer_id, 
		view_date 
	FROM Views
	GROUP BY viewer_id, view_date
	HAVING COUNT(DISTINCT article_id) > 1
	) AS tmp
ORDER BY id;


-- 列出每一个节点及其所属类型
-- Tree(id, p_id)节点和父节点
SELECT 
	id,
	CASE 
		WHEN p_id IS NULL THEN 'Root'
		WHEN id NOT IN (SELECT DISTINCT p_id FROM tree WHERE p_id IS NOT NULL) THEN 'Leaf'
		ELSE 'Inner' 
	END AS Type
FROM tree;


-- 2个表，客户和产品，通过product_id联结
-- 找出从“客户”表中购买了“产品”表中所有产品的客户ID
SELECT b.customer_id 
FROM Product AS a
LEFT JOIN Customer AS b
ON a.product_key = b.product_key
GROUP BY b.customer_id
HAVING COUNT(DISTINCT b.product_key) = (SELECT COUNT(*) FROM Product);

-- EXISTS
SELECT product_name, sale_price
FROM Product AS p
WHERE EXISTS (
	SELECT * FROM ShopProduct AS sp
	WHERE sp.shop_id='000C' ANd sp.product_id=p.product_id);

-- LIKE
-- IN

-- 查询买了 S8 但是没有买 iPhone 的顾客的 buyer_id
WITH tmp AS (
	SELECT 
		a.buyer_id, 
		b.product_name
	FROM Sales AS a
	JOIN Product AS b
	ON a.product_id = b.product_id
	)
SELECT DISTINCT buyer_id 
FROM tmp
WHERE buyer_id NOT IN (SELECT buyer_id FROM tmp WHERE product_name = 'iPhone')
AND buyer_id IN (SELECT buyer_id FROM tmp WHERE product_name = 'S8');


-- BETWEEN

-- 查询所有查看了至少一篇自己的文章的作者，并按ID升序排列
SELECT DISTINCT author_id id 
FROM Views
WHERE author_id = viewer_id
ORDER BY id;

-- 查询只在 2019 年春季销售的产品编号及产品名称
SELECT DISTINCT a.product_id, b.product_name 
FROM Sales AS a
JOIN Product AS b
ON a.product_id = b.product_id
WHERE a.product_id NOT IN (SELECT product_id FROM Sales WHERE sale_date < '2019-01-01')
AND a.product_id NOT IN (SELECT product_id FROM Sales WHERE sale_date > '2019-03-31');

-- 找出actor与director合作至少3次的情况，并返回（actor_id，director_id）值
SELECT 
	actor_id, 
	director_id 
FROM ActorDirector
GROUP BY actor_id, director_id
HAVING COUNT(timestamp) >= 3;

-- 找出下单数最多的顾客，列出customer_number。注意：结果只有一个值，不会存在多个值
-- 法一
SELECT customer_number 
FROM orders
GROUP BY customer_number
ORDER BY COUNT(*) DESC
LIMIT 1;

-- 法二
SELECT customer_number 
FROM orders 
GROUP BY customer_number
HAVING COUNT(customer_number) >= ALL(SELECT COUNT(customer_number) FROM orders GROUP BY customer_number);

-- 姗姗
SELECT DISTINCT a.customer_number 
FROM orders AS a
JOIN (
	SELECT 
		customer_number, 
		COUNT(order_number) AS num 
	FROM orders
	GROUP BY customer_number
	) AS b
ON a.customer_number = b.customer_number
WHERE b.num >= ALL(SELECT COUNT(*) FROM orders GROUP BY customer_number);

-- 找出不是被2号顾客推荐来的顾客姓名
-- or is null
-- SQL 的三值逻辑，如果条件只是 WHERE referee_id <> 2，则返回不出 referee_id 为 null 的顾客
SELECT name 
FROM customer 
WHERE referee_id <> 2 OR referee_id IS NULL;

-- 子查询
SELECT name 
FROM customer 
WHERE id NOT IN (SELECT id FROM customer WHERE referee_id = 2);

-- 法三
SELECT name 
FROM customer
WHERE IFNULL(referee_id, 0) <> 2;


-- 列出至少有5名学生的课程名称
-- 每个学生只算作一次
SELECT class 
FROM courses
GROUP BY class
HAVING COUNT(DISTINCT student) >= 5;


-- 查询重复的邮箱
SELECT Email FROM Person
GROUP BY Email
HAVING COUNT(Id) > 1;


-- 查找最大的数字，该数字只出现一次
-- 注意：如果没有这样的数字，则仅输出 null
SELECT MAX(num) AS num 
FROM (
	SELECT num FROM my_numbers
	GROUP BY num
	HAVING COUNT(*) = 1
	) AS x;

-- 找到国土面积大于300万平方公里或人口数超过2500万的国家，并显示人口数和国土面积
-- 法一
SELECT 
	name, 
	population, 
	area 
FROM World
WHERE area > 3000000 OR population > 25000000;

-- 法二
-- exists()判断查询子句中是否有记录
SELECT 
	name, 
	population, 
	area
FROM World
WHERE EXISTS (SELECT population, area WHERE (population > 25000000) OR (area > 3000000));

-- 找出中位数
-- 姗姗，不太懂
SELECT AVG(Number) AS median
FROM (
	SELECT
		*, 
		SUM(Frequency) OVER (ORDER BY Number) AS cum_sum,
        ROUND((SUM(Frequency) over ())/2.0)  AS mid1,
        (SUM(Frequency) OVER ())/2.0 AS mid2,
        (SUM(Frequency) OVER ())/2.0 + 1 AS mid3,
        SUM(Frequency) OVER () AS total
    FROM Numbers
    ) AS temp  
WHERE 
	CASE WHEN MOD(total,2) = 0 THEN (mid2 > cum_sum - frequency AND mid2 <= cum_sum)
	OR (mid3 > cum_sum - frequency AND mid3 <= cum_sum)
	ELSE mid1 > cum_sum - frequency AND mid1 <= cum_sum END;


-- 查找2016年的投资总额，其中需要满足如下两个条件：
-- 2015年投资额不是唯一值 (至少两个政策制定者在2015年的投资额是相等的)
-- 位置是唯一的 (即经度和纬度的组合没有重复值)
-- 不懂
-- 法一
SELECT SUM(TIV_2016) AS TIV_2016
FROM insurance
WHERE TIV_2015 IN (
	SELECT TIV_2015 
	FROM insurance 
	GROUP BY TIV_2015 
	HAVING COUNT(*) > 1) 
AND (lat, lon) IN (
	SELECT lat, lon 
	FROM insurance 
	GROUP BY lat, lon 
	HAVING COUNT(*)=1);

-- 法二
SELECT SUM(a.TIV_2016) AS TIV_2016 
FROM insurance AS a
JOIN (
	SELECT LAT, LON 
	FROM insurance
	GROUP BY LAT, LON
	HAVING COUNT(*) = 1) AS b
ON a.LAT = b.LAT AND a.LON = b.LON
WHERE a.TIV_2015 IN (
	SELECT DISTINCT TIV_2015 
	FROM insurance
	GROUP BY TIV_2015
	HAVING COUNT(*) > 1);

-- 2个表，项目和员工
-- 查询员工最多的项目
-- 姗姗
SELECT project_id 
FROM Project
GROUP BY project_id
HAVING COUNT(employee_id) >= ALL(SELECT COUNT(employee_id) OVER(PARTITION BY project_id) FROM Project);


-- 查询收入第二高的员工薪水，若无则null
SELECT MAX(CASE WHEN rnk = 2 THEN Salary ELSE null END) AS SecondHighestSalary
FROM (
	SELECT
		Salary,
		ROW_NUMBER() OVER(ORDER BY Salary DESC) AS rnk 
	FROM Employee) AS tmp;

-- 找出工资第 N 高的员工的薪水，100 此处举例
SELECT MAX(CASE WHEN rnk = 100 THEN Salary ELSE null END) AS SecondHighestSalary 
FROM (
	SELECT 
		Salary,
		ROW_NUMBER() OVER(ORDER BY Salary DESC) AS rnk 
	FROM Employee
	) AS tmp;

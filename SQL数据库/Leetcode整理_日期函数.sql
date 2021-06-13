-- 1. 日期操作
-- 1.1 TO_DATE
-- 得到 2020-03-21 
SELECT TO_DATE('2020-03-21 17:13:39') 
SELECT SUBSTR('2020-03-21 17:13:39',1,10)

-- 1.2 加减
-- DATE_SUB() 得到开始日期startdate减少days天后的日期
-- 得到 2012-11-28
SELECT DATE_SUB('2012-12-08', INTERVAL 10 DAY) 
SELECT SUBDATE('2012-12-08', 10)

-- DATE_ADD() 得到开始日期startdate增加days天后的日期
-- 得到 2012-12-18
SELECT DATE_ADD('2012-12-08', INTERVAL 10 DAY) 

-- 返回比前一天温度高的 id
-- 表信息：三列，id+日期+温度
-- 法一
SELECT a.id 
FROM Weather AS a
JOIN Weather AS b
ON a.recordDate = ADDDATE(b.recordDate, INTERVAL 1 DAY)
WHERE a.temperature > b.temperature;

-- 法二 （换了一个函数其他不变）
SELECT a.id 
FROM Weather AS a 
JOIN Weather AS b 
ON a.recordDate = DATE_ADD(b.recordDate, INTERVAL 1 DAY) 
WHERE a.temperature > b.temperature;

SELECT a.id 
FROM Weather AS a
JOIN Weather AS b
ON b.recordDate = SUBDATE(a.recordDate, INTERVAL 1 DAY)
WHERE a.temperature > b.temperature;

SELECT a.id 
FROM Weather AS a  
JOIN Weather AS b  
ON b.recordDate = DATE_SUB(a.recordDate, INTERVAL 1 DAY)  
WHERE a.temperature > b.temperature;

-- DATEDIFF(string enddate, string startdate)得到 结束日期减去开始日期的天数
-- 得到 213
SELECT DATEDIFF('2012-12-08','2012-05-09') 

-- 法四
SELECT a.id 
FROM Weather AS a
JOIN Weather AS b
ON DATEDIFF(a.recordDate, b.recordDate) = 1
WHERE a.temperature > b.temperature

-- 2张表
-- actions(user_id, post_id, action_date, action, extra)
-- action 列可能的值为 view, like, reaction, comment, report, 以及 share
-- extra 列不是必须的，包含有关操作的可选信息，例如报告原因或反应类型
-- removals(post_id, remove_date)
-- Write an SQL query that reports # of posts reported yesterday for each report reason
SELECT
	extra AS report_reason, 
	COUNT(DISTINCT post_id) AS report_count
FROM Actions
WHERE extra IS NOT NULL AND action = 'report' AND DATEDIFF("2019-07-05", action_date) = 1
GROUP BY extra;

-- 2. 时间和日期转换
-- 2.1 UNIT_TIMESTAMP 日期转化为时间戳
-- 得到 1584782019
SELECT UNIT_TIMESTAMP('2020-03-21', 'yyyy-MM-dd')
SELECT UNIT_TIMESTAMP('20200321 13:01:03','yyyyMMdd HH:mm:ss') 
SELECT UNIT_TIMESTAMP('20200321','yyyyMMdd')

-- 2.2 FROM_UNIXTIME 时间转化为日期
-- 得到 2020-03-21 17:16:15
SELECT FROM_UNIXTIME (1584782175) 
-- 得到 20200321
SELECT FROM_UNIXTIME (1584782175,'yyyyMMdd') 
-- 得到 2020-03-21
SELECT FROM_UNIXTIME (1584782175,'yyyy-MM-dd')

-- 2.3 日起和日期之间通过时间戳转化
-- 得到 2020-03-21
SELECT FROM_UNIXTIME(UNIT_TIMESTAMP('20200321','yyyymmdd'),'yyyy-mm-dd') 
-- 得到 20200321
SELECT FROM_UNIXTIME(UNIT_TIMESTAMP('2020-03-21','yyyy-mm-dd'),'yyyymmdd')

-- 3. 日期格式
DATE_FORMAT(pay_date, '%Y-%m') AS pay_month

-- transactions(id, country, state, amount, trans_date)
-- 查询每个月和每个国家/地区的交易次数及其总金额，批准的交易次数及其总金额
SELECT 
	DATE_FORMAT(a.trans_date, "%Y-%m") AS month,
	a.country,
	COUNT(a.id) AS trans_count,
	COUNT(b.id) AS approved_count,
	SUM(a.amount) AS trans_total_amount,
	SUM(COALESCE(b.amount,0)) AS approved_total_amount 
FROM Transactions AS a
LEFT JOIN (
	SELECT
		id,
		country,
		state,
		amount,
		DATE_FORMAT(trans_date, "%Y-%m") AS month 
	FROM Transactions
	WHERE state = 'approved'
	) AS b
ON a.id = b.id
GROUP BY DATE_FORMAT(a.trans_date, "%Y-%m"), a.country;

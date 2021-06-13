-- 1. 基础
-- 1.1 字符串提取 SUBSTR(string A, int start)返回字符串A从start位置到结尾的字符串
-- 返回 cde
SELECT SUBSTRING('abcde', 3)

-- SUBSTRING(string A, int start, int len)返回字符串A从start位置开始，长度为len的字符串
-- 得到 cd
SELECT SUBSTRING('abcde', 3, 2) 

-- 1.3 字符串拼接 CONCAT(A, B) 返回AB多个拼接的结果
-- 返回 abcdefgh
SELECT CONCAT('abc', 'def', 'gh')

-- CONCAT_WS(X, A, B) A和B由X拼接
-- 返回 abc, def, gh
SELECT CONCAT_WS(',', 'abc', 'def', 'gh')

-- GROUP_CONCAT()将group by产生的同一个分组中的值连接起来，返回一个字符串结果
SELECT 
    performance, 
    GROUP_CONCAT(employee_name) AS employees
FROM employees
GROUP BY performance;

SELECT GROUP_CONCAT(DISTINCT home_town ORDER BY home_town DESC SEPARATOR ';') AS '领导关怀地区'
FROM employees;

-- 查询每个日期的不同产品的销售数量及其名称，每个日期中的已售产品名称应按字典顺序排序
-- 查询结果按 sell_date 升序排序
SELECT
    sell_date,
    COUNT(DISTINCT product) AS num_sold, 
    GROUP_CONCAT(DISTINCT product ORDER BY product) AS products
FROM Activities
GROUP BY sell_date
ORDER BY sell_date;

-- 查找2016年的投资总额，其中需要满足如下两个条件：
-- 2015年投资额不是唯一值 (至少两个政策制定者在2015年的投资额是相等的)
-- 位置是唯一的 (即经度和纬度的组合没有重复值)
SELECT SUM(insurance.TIV_2016) AS TIV_2016
FROM insurance
WHERE insurance.TIV_2015 IN (
    SELECT TIV_2015 
    FROM insurance
    GROUP BY TIV_2015
    HAVING COUNT(*) > 1)
AND CONCAT(LAT, ",", LON) IN (
    SELECT CONCAT(LAT, ",", LON) 
    FROM insurance
    GROUP BY LAT , LON
    HAVING COUNT(*) = 1);


-- 1.4 字符串基本处理
SELECT LENGTH('abcdefg')
SELECT TRIM('  abc   ')
SELECT LOWER('abSEd')
SELECT UPPER('abSED')

-- 1.5 不同格式数据转化
SELECT CAST(A TO string) AS A

-- 1.6 字符串正则
-- REGEXP_EXTRACT(string subject, string pattern, int index)
-- 将字符串subject按照pattern正则表达式的规则拆分，返回index指定的字符
-- 返回 the
SELECT REGEXP_EXTRACT('foothebar', 'foo(.*?)(bar)', 1)

-- REGEXP_REPLACE(A, B, C) 将A中符合正则表达式B的部分替换为C
-- 返回 fb
SELECT REGEXP_REPLACE('foobar', 'oo|ar', '')

-- 查询拥有有效电子邮件的用户
-- 前缀名称是一个字符串，可能包含字母（大写或小写），数字，下划线，句点和/或破折号。
-- 前缀名称必须以字母开头。
-- 域为“ @ leetcode.com”
SELECT * FROM users
WHERE mail REGEXP '^[A-Z][A-Z0-9_.-]*@leetcode.com$';


-- 1.7 字符串解析
-- GET_JSON_OBJECT(string, path) 返回path指定内容
-- 得到 420
select GET_JSON_OBJECT(
                  	{"from_remain_count":420,"reason":"collect","to_remain_count":0},
                    '$.from_remain_count'
                ) 
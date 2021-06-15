-- 创建表
CREATE TABLE teachers (
	id bigserial,
	first_name varchar(25), 
	last_name varchar(50),
	school varchar(50),
	hire_date date,
	salary numeric
);

-- 增加6行（6位老师）
INSERT INTO teachers (first_name, last_name, school, hire_date, salary)
VALUES ('Janet', 'Smith', 'F.D. Roosevelt HS', '2011-10-30', 36200),
('Lee', 'Reynolds', 'F.D. Roosevelt HS', '1993-05-22', 65000),
('Samuel', 'Cole', 'Myers Middle School', '2005-08-01', 43500),
('Samantha', 'Bush', 'Myers Middle School', '2011-10-30', 36200),
('Betty', 'Diaz', 'Myers Middle School', '2005-08-30', 43500),
('Kathleen', 'Roush', 'F.D. Roosevelt HS', '2010-10-22', 38500);

-- 截取全部或是subset
SELECT * FROM teachers;
SELECT last_name, first_name, salary FROM teachers;
-- unique的值
SELECT DISTINCT school
FROM teachers;

-- 每个学校的unique工资
SELECT DISTINCT school, salary
FROM teachers;

-- 降序排列工资
-- 默认order by 升序
SELECT first_name, last_name, salary
FROM teachers
ORDER BY salary DESC;

-- 按学校分组的生序+受聘日期的降序
SELECT last_name, school, hire_date 
FROM teachers
ORDER BY school ASC, hire_date DESC;

-- 添加过滤条件
SELECT last_name, school, hire_date FROM teachers
WHERE school = 'Myers Middle School';
-- not equal
WHERE school <> 'Baker Middle'
--日期也可以比较，此处选取在之前
WHERE hire_date < '2000-01-01';
-- 区间内
WHERE salary BETWEEN 20000 AND 40000
-- 匹配一个子集（包含在一个集合里）
WHERE last_name IN ('Bush', 'Roush')
-- 符合某种形式
WHERE first_name LIKE '%am%'
-- 不区分大小写
WHERE first_name ILIKE 'sam%'
-- 否定
WHERE first_name NOT LIKE 'Sam%'
-- 复合
SELECT *
FROM teachers
WHERE school = 'F.D. Roosevelt HS'
    AND (salary < 38000 OR salary > 40000);
    

-- 删除表
DROP TABLE teache;

-- 拷贝表
-- 任何行都不能满足的布尔条件。由于没检索到行，所以仅拷贝了表的结构
CREATE TABLE s_worker
AS SELECT *
FROM s_emp
WHERE 1<>1;

-- 更新表
UPDATE  s_worker
SET COLUMN = (
    SELECT col_name
    FROM s_worker
    WHERE condition)
WHERE col_name = (
    SELECT col_name
    FROM s_worker
    WHERE condition);

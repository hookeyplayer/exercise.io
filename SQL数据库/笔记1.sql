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
SELECT first_name, last_name, salary
FROM teachers
ORDER BY salary DESC;
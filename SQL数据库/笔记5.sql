CREATE TABLE departments (
	dept_id bigserial,
	dept varchar(100),
	city varchar(100),
	CONSTRAINT dept_key PRIMARY KEY (dept_id),
	CONSTRAINT dept_city_unique UNIQUE (dept, city)
);
CREATE TABLE employees (
	emp_id bigserial,
	first_name varchar(100),
	last_name varchar(100),
	salary integer,
	dept_id integer REFERENCES departments (dept_id),
	CONSTRAINT emp_key PRIMARY KEY (emp_id),
	CONSTRAINT emp_dept_unique UNIQUE (emp_id, dept_id)
);

INSERT INTO departments (dept, city)
VALUES
    ('Tax', 'Atlanta'),
    ('IT', 'Boston');

INSERT INTO employees (first_name, last_name, salary, dept_id) 
VALUES
    ('Nancy', 'Jones', 62500, 1),
    ('Lee', 'Smith', 59300, 1),
    ('Soo', 'Nguyen', 83000, 2),
    ('Janet', 'King', 95000, 2);

-- 使用join query
SELECT *
FROM employees JOIN departments
ON employees.dept_id = departments.dept_id;

CREATE TABLE schools_left (
	id integer CONSTRAINT left_id_key PRIMARY KEY,
	left_school varchar(30)
);

CREATE TABLE schools_right (
	id integer CONSTRAINT right_id_key PRIMARY KEY,
	right_school varchar(30)
);

INSERT INTO schools_left (id, left_school) 
VALUES 
    (1, 'Oak Street School'),
    (2, 'Roosevelt High School'),
    (5, 'Washington Middle School'),
    (6, 'Jefferson High School');
INSERT INTO schools_right (id, right_school)
VALUES
    (1, 'Oak Street School'),
    (2, 'Roosevelt High School'),
    (3, 'Morrison Elementary'),
    (4, 'Chase Magnet Academy'),
    (6, 'Jefferson High School');

-- outerjoin
SELECT *
FROM schools_left FULL OUTER JOIN schools_right
ON schools_left.id = schools_right.id;

-- 借助NULL查找行内缺省值
SELECT *
FROM schools_left LEFT JOIN schools_right 
ON schools_left.id = schools_right.id 
WHERE schools_right.id IS NULL;

-- 查找一列（表的subset，而非全部）
-- 报错的写法：
-- SELECT id
-- FROM schools_left LEFT JOIN schools_right 
-- ON schools_left.id = schools_right.id;

-- 正确的写法：
SELECT schools_left.id,
       schools_left.left_school,
       schools_right.right_school
FROM schools_left LEFT JOIN schools_right
ON schools_left.id = schools_right.id;

CREATE TABLE schools_enrollment (
	id integer,
	enrollment integer
);
CREATE TABLE schools_grades (
	id integer,
    grades varchar(10)
  );
INSERT INTO schools_enrollment (id, enrollment) 
VALUES
    (1, 360),
    (2, 1001),
    (5, 450),
    (6, 927);
INSERT INTO schools_grades (id, grades)
VALUES
    (1, 'K-3'),
    (2, '9-12'),
    (5, '6-8'),
    (6, '9-12');

SELECT lt.id, lt.left_school, en.enrollment, gr.grades
-- 取精简的表名join
-- 整合3个表格
FROM schools_left AS lt LEFT JOIN schools_enrollment AS en 
ON lt.id = en.id
LEFT JOIN schools_grades AS gr 
ON lt.id = gr.id;

-- join时加入数学计算
CREATE TABLE us_counties_2000 (
	geo_name varchar(90),
	state_us_abbreviation varchar(2),
	state_fips varchar(2),
	county_fips varchar(3),
	p0010001 integer,
    p0010002 integer,
    p0010003 integer,
    p0010004 integer,
    p0010005 integer,
    p0010006 integer,
    p0010007 integer,
    p0010008 integer,
    p0010009 integer,
    p0010010 integer,
    p0020002 integer,
    p0020003 integer
);

COPY us_counties_2000
FROM '/Users/xiaofan/Downloads/practical-sql-master/Chapter_06/us_counties_2000.csv' 
WITH (FORMAT CSV, HEADER);

SELECT c2010.geo_name,
       c2010.state_us_abbreviation AS state,
       c2010.p0010001 AS pop_2010,
       c2000.p0010001 AS pop_2000,
       c2010.p0010001 - c2000.p0010001 AS raw_change,
       -- 一位小数
       round( (CAST(c2010.p0010001 AS numeric(8,1)) - c2000.p0010001)
       	/ c2000.p0010001 * 100, 1 ) AS pct_change
FROM us_counties_2010 c2010 INNER JOIN us_counties_2000 c2000
ON c2010.state_fips = c2000.state_fips
AND c2010.county_fips = c2000.county_fips
AND c2010.p0010001 <> c2000.p0010001
ORDER BY pct_change DESC;
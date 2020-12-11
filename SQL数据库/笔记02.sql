-- 创建三列，定义datatype=character
CREATE TABLE char_data_types (
	varchar_column varchar(10),
	char_column char(10),
	text_column text
);
-- 未定义列的名字
INSERT INTO char_data_types
VALUES
    ('abc', 'abc', 'abc'),
    ('defghi', 'defghi', 'defghi');
-- 创建了一个txt文件
-- copy是PostgreSQL的语言所以sql不标亮
COPY char_data_types TO '/Users/xiaofan/SQL数据库/type test.txt'
-- format the data with each column separated by a pipe character (|)
WITH (FORMAT CSV, HEADER, DELIMITER '|');

CREATE TABLE number_data_types (
	numeric_column numeric(20,5),
	real_column real,
	double_column double precision
);
INSERT INTO number_data_types 
VALUES
    (.7, .7, .7),
    (2.13579, 2.13579, 2.13579),
    (2.1357987654, 2.1357987654, 2.1357987654);
SELECT * FROM number_data_types;

-- 浮点的不精确
SELECT
    numeric_column * 10000000 AS "Fixed",
    real_column * 10000000 AS "Float"
FROM number_data_types
WHERE numeric_column = .7;

-- 2列4行
CREATE TABLE date_time_types (
	timestamp_column timestamp with time zone,
	interval_column interval
);
INSERT INTO date_time_types
VALUES
    ('2018-12-31 01:00 EST','2 days'),
    ('2018-12-31 01:00 -8','1 month'),
    ('2018-12-31 01:00 Australia/Melbourne','1 century'),
    (now(),'1 week');
SELECT * FROM date_time_types;

SELECT
    timestamp_column,
    interval_column,
    timestamp_column - interval_column AS new_date
FROM date_time_types;

-- 使用cast函数的第一种：variable-length character column=10
SELECT
    timestamp_column,
    CAST(timestamp_column AS varchar(10))
FROM date_time_types;

-- 第二种cast函数
SELECT 
    numeric_column,
    CAST(numeric_column AS integer),
    CAST(numeric_column AS varchar(6))
FROM number_data_types;

-- 只在PostgreSQL里存在快捷双引号的使用，在列名称和type之间截取
SELECT
    timestamp_column,
    CAST(timestamp_column AS varchar(10)) 
FROM date_time_types;

SELECT timestamp_column::varchar(10) 
FROM date_time_types;

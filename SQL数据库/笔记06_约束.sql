-- primary key 主键约束
CREATE TABLE natural_key_example ( 
	license_id varchar(10) PRIMARY KEY,
	first_name varchar(50),
	last_name varchar(50) 
	);

ALTER TABLE natural_key_example DROP PRIMARY KEY;



-- -- 如果忘记创建主键
-- mysql way
ALTER TABLE natural_key_example ADD PRIMARY KEY (license_id);
-- 弃键的约束
-- ALTER TABLE natural_key_example DROP CONSTRAINT license_id;
-- 弃 not null 的约束
ALTER TABLE natural_key_example ALTER COLUMN first_name DROP NOT NULL;


-- composite primary key 联合约束
CREATE TABLE natural_key_composite_example (
	student_id varchar(10),
	school_day date,
	present boolean,
	CONSTRAINT student_key PRIMARY KEY (student_id, school_day)
	-- PRIMARY KEY (student_id, school_day)
	);
-- 此时第1、2不会报错
INSERT INTO natural_key_composite_example (student_id, school_day, present) 
VALUES(775, '1/22/2017', 'Y');
INSERT INTO natural_key_composite_example (student_id, school_day, present) 
ALUES(775, '1/23/2017', 'Y');
INSERT INTO natural_key_composite_example (student_id, school_day, present) 
ALUES(775, '1/23/2017', 'N');


-- auto-incrementing surrogate key 自增约束
-- order_number列自动补全1、2、3
-- smallserial, serial, and bigserial对应smallint, integer, and bigint
CREATE TABLE surrogate_key_example (
	order_number bigserial PRIMARY KEY auto_increment
	product_name varchar(50), 
	order_date date
	);
INSERT INTO surrogate_key_example (product_name, order_date) 
VALUES ('Beachball Polish', '2015-03-17'), 
('Wrinkle De-Atomizer', '2017-05-22'),
('Flux Capacitor', '1985-10-26');
SELECT * FROM surrogate_key_example; 


-- foreign key 外键约束
CREATE TABLE licenses ( 
	license_id varchar(10),
	first_name varchar(50), 
	last_name varchar(50),
	CONSTRAINT licenses_key PRIMARY KEY (license_id)
	);
CREATE TABLE registrations ( 
	registration_id varchar(10),
	registration_date date,
	license_id varchar(10) REFERENCES licenses (license_id),
	CONSTRAINT registration_key PRIMARY KEY (registration_id, license_id)
	);
INSERT INTO licenses (license_id, first_name, last_name) 
VALUES ('T229901', 'Lynn', 'Malero');
-- 正常
INSERT INTO registrations (registration_id, registration_date, license_id) 
VALUES ('A203391', '3/17/2017', 'T229901');
-- 报错，因为license_id不存在于licenses表里
INSERT INTO registrations (registration_id, registration_date, license_id)
VALUES ('A75772', '3/17/2017', 'T000001');

-- 在registrations中创建表需要事先已在licenses存在license_id
-- 下面旨在删除licenses相关行时同时删除registrations相关行
-- registrations中不会遗留orphaned行
CREATE TABLE registrations (
	registration_id varchar(10),
	registration_date date,
	license_id varchar(10) REFERENCES licenses (license_id) ON DELETE CASCADE,
	CONSTRAINT registration_key PRIMARY KEY (registration_id, license_id)
	);


-- check约束
CREATE TABLE check_constraint_example (
	user_id bigserial,
	user_role varchar(50),
	salary integer,
	CONSTRAINT user_id_key PRIMARY KEY (user_id),
	CONSTRAINT check_role_in_list CHECK (user_role IN ('Admin', 'Staff')),
	CONSTRAINT check_salary_not_zero CHECK (salary > 0)
	);


-- unique 唯一约束:允许null存在
-- mysql method:
CREATE TABLE user1 (
id int,
name varchar(20),
unique(name)
);
					     
CREATE TABLE unique_constraint_example (
	contact_id bigserial CONSTRAINT contact_id_key PRIMARY KEY, 
	first_name varchar(50),
	last_name varchar(50),
	email varchar(200),
	CONSTRAINT email_unique UNIQUE (email)
	);
INSERT INTO unique_constraint_example (first_name, last_name, email) 
VALUES ('Samantha', 'Lee', 'slee@example.org');
INSERT INTO unique_constraint_example (first_name, last_name, email) 
VALUES ('Betty', 'Diaz', 'bdiaz@example.org');
					     
ALTER TABLE unique_constraint_example ADD UNIQUE (name);
ALTER TABLE unique_constraint_example DROP INDEX name;
ALTER TABLE not_null_example ADD PRIMARY KEY (student_id);				     
ALTER TABLE unique_constraint_example MODIFY name varchar(20) UNIQUE; 
ALTER TABLE natural_key_example MODIFY license_id varchar(10) PRIMARY KEY;					    

-- 非空约束
CREATE TABLE not_null_example (
	student_id bigserial PRIMARY KEY,
	first_name varchar(50) NOT NULL,
	last_name varchar(50) NOT NULL,
	);

ALTER TABLE not_null_example ALTER COLUMN first_name DROP NOT NULL; 
ALTER TABLE not_null_example ALTER COLUMN first_name SET NOT NULL;



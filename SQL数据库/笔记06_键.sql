-- primary key
CREATE TABLE natural_key_example ( 
	license_id varchar(10) CONSTRAINT license_key PRIMARY KEY,
	first_name varchar(50),
	last_name varchar(50) 
	);
-- 会报错，因为primary key应该唯一
-- ERROR:  duplicate key value violates unique constraint "license_key"
INSERT INTO natural_key_example(license_id, first_name, last_name)
VALUES ('T229901', 'Lynn', 'Malero');
INSERT INTO natural_key_example (license_id, first_name, last_name) 
VALUES ('T229901', 'Sam', 'Tracy'); 

-- composite primary key
CREATE TABLE natural_key_composite_example (
	student_id varchar(10),
	school_day date,
	present boolean,
	CONSTRAINT student_key PRIMARY KEY (student_id, school_day)
	);
-- 此时第1、2不会报错
INSERT INTO natural_key_composite_example (student_id, school_day, present) 
VALUES(775, '1/22/2017', 'Y');
INSERT INTO natural_key_composite_example (student_id, school_day, present) 
ALUES(775, '1/23/2017', 'Y');
INSERT INTO natural_key_composite_example (student_id, school_day, present) 
ALUES(775, '1/23/2017', 'N');
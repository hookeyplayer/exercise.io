CREATE TABLE meat_poultry_egg_inspect (
    est_number varchar(50) CONSTRAINT est_number_key PRIMARY KEY,
    company varchar(100),
    street varchar(100),
    city varchar(30),
    st varchar(2),
    zip varchar(5),
    phone varchar(14),
    grant_date date,
    activities text,
    dbas text
);

COPY meat_poultry_egg_inspect
FROM '/Users/xiaofan/Downloads/practical-sql-master/Chapter_09/MPI_Directory_by_Establishment_Name.csv'
WITH (FORMAT CSV, HEADER, DELIMITER ',');
CREATE INDEX company_idx ON meat_poultry_egg_inspect (company);

-- 计数
SELECT count(*) 
FROM meat_poultry_egg_inspect;

-- 查看是否有多个公司写着同一个地址，结果有23个（但不一定是entry error）
SELECT company,
       street,
       city,
       st,
       count(*) AS address_count -- alias
FROM meat_poultry_egg_inspect
GROUP BY company, street, city, st -- unique combination
HAVING count(*) > 1
ORDER BY company, street, city, st;

-- 任务一
-- 有3行其st列名为null
SELECT st, 
       count(*) AS st_count
FROM meat_poultry_egg_inspect
GROUP BY st
ORDER BY st;

-- 用IS NULL 查找st列为null的行
SELECT est_number,
       company,
       city,
       st,
       zip
FROM meat_poultry_egg_inspect
WHERE st IS NULL;

-- 更新
UPDATE meat_poultry_egg_inspect
SET st = 'MN'
WHERE est_number = 'V18677A';

UPDATE meat_poultry_egg_inspect
SET st = 'AL'
WHERE est_number = 'M45319+P45319';

UPDATE meat_poultry_egg_inspect
SET st = 'WI'
WHERE est_number = 'M263A+P263A+V263A';

-- 手误的挽救
UPDATE meat_poultry_egg_inspect 
SET st = st_copy;

UPDATE meat_poultry_egg_inspect original
SET st = backup.st
FROM meat_poultry_egg_inspect_backup backup
WHERE original.est_number = backup.est_number

-- 任务二
-- 用GROUP BY和count()查找inconsistent company names
-- 同一个公司有不规范多种写法Inc., LLC.
SELECT company,
       count(*) AS company_count
FROM meat_poultry_egg_inspect
GROUP BY company
ORDER BY company ASC;

ALTER TABLE meat_poultry_egg_inspect ADD COLUMN company_standard varchar(100);

UPDATE meat_poultry_egg_inspect
SET company_standard = company;

UPDATE meat_poultry_egg_inspect
SET company_standard = 'Armour-Eckrich Meats'
WHERE company LIKE 'Armour%';

SELECT company, company_standard
FROM meat_poultry_egg_inspect
WHERE company LIKE 'Armour%';


-- 任务三
-- 用length()和count()查找malformed值
-- concatenation的使用，修复zip
SELECT length(zip),
       count(*) AS length_count
FROM meat_poultry_egg_inspect
GROUP BY length(zip)
ORDER BY length(zip) ASC;

-- 定位
SELECT st,
       count(*) AS st_count
FROM meat_poultry_egg_inspect
WHERE length(zip) < 5
GROUP BY st
ORDER BY st ASC;

ALTER TABLE meat_poultry_egg_inspect ADD COLUMN zip_copy varchar(5);

UPDATE meat_poultry_egg_inspect
SET zip_copy = zip;

UPDATE meat_poultry_egg_inspect
SET zip = '00' || zip -- concatenation operator
WHERE st IN('PR','VI') AND length(zip) = 3;

-- Listing 9-17: Modify codes in the zip column missing one leading zero

UPDATE meat_poultry_egg_inspect
SET zip = '0' || zip
WHERE st IN('CT','MA','ME','NH','NJ','RI','VT') AND length(zip) = 4;


-- 备份一（整张表）
CREATE TABLE meat_poultry_egg_inspect_backup AS
SELECT * FROM meat_poultry_egg_inspect;

-- 检查一致性
SELECT 
    (SELECT count(*) FROM meat_poultry_egg_inspect) AS original,
    (SELECT count(*) FROM meat_poultry_egg_inspect_backup) AS backup;

-- 备份二（整张列）
ALTER TABLE meat_poultry_egg_inspect ADD COLUMN st_copy varchar(2);

UPDATE meat_poultry_egg_inspect
SET st_copy = st;

-- 检查一致性
-- SELECT st,
--        st_copy
-- FROM meat_poultry_egg_inspect
-- ORDER BY st;
SELECT st,
       st_copy
FROM meat_poultry_egg_inspect
GROUP BY st, st_copy
ORDER BY st;

-- 备份三（通过事先复制的列复原）
UPDATE meat_poultry_egg_inspect
SET st = st_copy;

-- 备份四（通过事先复制的整张表复原）
UPDATE meat_poultry_egg_inspect original
SET st = backup.st
FROM meat_poultry_egg_inspect_backup backup
WHERE original.est_number = backup.est_number; 




COPY state_regions
FROM '/Users/xiaofan/Downloads/practical-sql-master/Chapter_09/state_regions.csv'
WITH (FORMAT CSV, HEADER, DELIMITER ',');

CREATE TABLE state_regions (
    st varchar(2) CONSTRAINT st_key PRIMARY KEY,
    region varchar(20) NOT NULL
);

ALTER TABLE meat_poultry_egg_inspect ADD COLUMN inspection_date date;

UPDATE meat_poultry_egg_inspect inspect
SET inspection_date = '2019-12-01'
WHERE EXISTS (SELECT state_regions.region
              FROM state_regions
              WHERE inspect.st = state_regions.st AND state_regions.region = 'New England');

SELECT st, inspection_date
FROM meat_poultry_egg_inspect
GROUP BY st, inspection_date
ORDER BY st;

-- 删除行
DELETE FROM meat_poultry_egg_inspect
WHERE st IN('PR','VI');

-- 从表中移除列
ALTER TABLE meat_poultry_egg_inspect DROP COLUMN zip_copy;

-- 从数据库中移除表
DROP TABLE meat_poultry_egg_inspect_backup;

-- Listing 9-24: Demonstrating a transaction block

-- Start transaction and perform update
START TRANSACTION;

UPDATE meat_poultry_egg_inspect
SET company = 'AGRO Merchantss Oakland LLC'
WHERE company = 'AGRO Merchants Oakland, LLC';

-- view changes
SELECT company
FROM meat_poultry_egg_inspect
WHERE company LIKE 'AGRO%'
ORDER BY company;

-- Revert changes
ROLLBACK;

-- See restored state
SELECT company
FROM meat_poultry_egg_inspect
WHERE company LIKE 'AGRO%'
ORDER BY company;

-- Alternately, commit changes at the end:
START TRANSACTION;

UPDATE meat_poultry_egg_inspect
SET company = 'AGRO Merchants Oakland LLC'
WHERE company = 'AGRO Merchants Oakland, LLC';

COMMIT;

-- Listing 9-25: Backing up a table while adding and filling a new column

CREATE TABLE meat_poultry_egg_inspect_backup AS
SELECT *,
       '2018-02-07'::date AS reviewed_date
FROM meat_poultry_egg_inspect;

-- Listing 9-26: Swapping table names using ALTER TABLE

ALTER TABLE meat_poultry_egg_inspect RENAME TO meat_poultry_egg_inspect_temp;
ALTER TABLE meat_poultry_egg_inspect_backup RENAME TO meat_poultry_egg_inspect;
ALTER TABLE meat_poultry_egg_inspect_temp RENAME TO meat_poultry_egg_inspect_backup;


-- 公式：
-- 新增/删除
ALTER TABLE table ADD COLUMN column data_type;
ALTER TABLE table DROP COLUMN column;
-- 更改约束：列的数据类型、not null
ALTER TABLE table ALTER COLUMN column SET DATA TYPE data_type;
ALTER TABLE table ALTER COLUMN column SET NOT NULL;
ALTER TABLE table ALTER COLUMN column DROP NOT NULL;
-- 更新
UPDATE table
SET column = value;
WHERE criteria;

UPDATE table
SET column_a = value,
column_b = value;

-- 使用另一张表
UPDATE table
SET column = (SELECT column
              FROM table_b
              WHERE table.column = table_b.column) 
WHERE EXISTS (SELECT column 
              FROM table_b
              WHERE table.column = table_b.column);

UPDATE table
SET column = table_b.column
FROM table_b
WHERE table.column = table_b.column;



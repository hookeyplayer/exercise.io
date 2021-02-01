-- 找出不是被2号顾客推荐来的顾客姓名
-- or is null
-- SQL 的三值逻辑，如果条件只是 WHERE referee_id <> 2，则返回不出 referee_id 为 null 的顾客
SELECT name FROM customer 
WHERE referee_id <> 2 OR referee_id IS NULL;

-- 子查询
SELECT name FROM customer WHERE
id NOT IN
(SELECT id FROM customer WHERE referee_id = 2);

-- 法三
SELECT name FROM customer
WHERE IFNULL(referee_id, 0) <> 2;


-- 法四
SELECT name FROM customer
WHERE COALESCE(referee_id, 0) <> 2;
-- 男女性别交换
UPDATE salary
SET sex = (CASE WHEN sex = 'm' THEN 'f' ELSE 'm' END);
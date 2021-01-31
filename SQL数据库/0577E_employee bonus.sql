-- 两张表Employee和Bonus
-- 选出奖金小于1000元的员工姓名及其获得的奖金数
-- 法一
SELECT a.name, 
b.bonus
FROM Employee AS a
LEFT JOIN Bonus AS b
ON a.empId = b.empId
WHERE b.bonus < 1000 OR b.bonus IS NULL;


-- 法二
SELECT a.name, b.bonus
FROM Employee AS a
LEFT JOIN Bonus AS b
ON a.empId = b.empId
WHERE a.empId NOT IN
(SELECT empId FROM Bonus WHERE bonus >= 1000);
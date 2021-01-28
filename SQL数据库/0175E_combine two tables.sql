-- 查询每个人的姓名，以及住址
-- 注意：即使有人没有地址，也要将其罗列
SELECT a.FirstName, a.LastName, b.City, b.State FROM Person As a 
LEFT JOIN AddressId As b
ON a.PersonID = b.PersonID;

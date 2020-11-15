-- 表一：人，列有PersonId, FirstName, LastName
-- 表二：地址，列有AddressId, PersonId, City, State
-- 题目：查询每个人的名、姓、城市、州，即使有人没有AddressId，也要列出来
SELECT a.FirstName, a.LastName, b.City, b.State
FROM Person
AS a LEFT JOIN Address AS b
ON a.PersonId = b.PersonId

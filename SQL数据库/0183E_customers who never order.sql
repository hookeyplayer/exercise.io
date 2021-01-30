# 两张表：顾客表和订单表
# 找出没有下过订单的顾客姓名

# 法一：外联结
SELECT a.Name AS 'Customers' FROM Customers AS a
LEFT JOIN Orders AS b
ON a.Id = b.CustomerId
WHERE b.Id IS NULL;


# 法二：子查询
SELECT name AS 'Customers' FROM Customers
WHERE Id NOT IN
 (SELECT CustomerId FROM Orders);
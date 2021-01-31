-- 找出某时间期间里 每一天 未被禁止的 (unbanned) 用户的订单取消率

SELECT a.Request_at AS Day,
1-ROUND(SUM(CASE WHEN a.Status = 'completed' THEN 1 ELSE 0 END)/COUNT(*),2) AS 'Cancellation Rate' FROM Trips AS a
INNER JOIN 
(SELECT * FROM Users
 WHERE Role = 'client') AS b
ON a.Client_Id = b.Users_Id
INNER JOIN 
(SELECT * FROM Users
 WHERE Role = 'driver') AS c
ON a.Driver_Id = c.Users_Id
WHERE b.Banned = 'No'
AND c.Banned = 'No'
AND a.Request_at BETWEEN '2013-10-01' AND '2013-10-03'
GROUP BY a.Request_at
ORDER BY a.Request_at
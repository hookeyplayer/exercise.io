-- 查询每个月和每个国家/地区的交易次数及其总金额，批准的交易次数及其总金额
SELECT 
	DATE_FORMAT(a.trans_date, "%Y-%m") AS month,
	a.country,
	COUNT(a.id) AS trans_count,
	COUNT(b.id) AS approved_count,
	SUM(a.amount) AS trans_total_amount,
	SUM(COALESCE(b.amount,0)) AS approved_total_amount 
FROM Transactions a
LEFT JOIN (SELECT
				id,
				country,
				state,
				amount,
				DATE_FORMAT(trans_date, "%Y-%m") AS month 
		   FROM Transactions
		   WHERE state = 'approved') b
	ON a.id = b.id
GROUP BY DATE_FORMAT(a.trans_date, "%Y-%m"), a.country;
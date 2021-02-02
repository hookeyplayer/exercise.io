-- 交易和退款2张表
-- 查询每个月和每个国家/地区的已批准交易的数量及其总金额，拒付金额及其总金额
-- 姗姗
WITH
tmp AS (
	SELECT 
		a.trans_id AS id,
		b.country,
		'checkback' AS state,
		b.amount,
		a.trans_date
	FROM Chargebacks a
	LEFT JOIN Transactions b
		ON a.trans_id = b.id

	UNION ALL
	    
	SELECT * FROM Transactions
	WHERE state = 'approved'
)

SELECT
	DATE_FORMAT(trans_date, "%Y-%m") AS month,
	country,
	SUM(CASE WHEN state = 'approved' THEN 1 ELSE 0 END) AS approved_count,
	SUM(CASE WHEN state = 'approved' THEN amount ELSE 0 END) AS approved_amount,
	SUM(CASE WHEN state = 'checkback' THEN 1 ELSE 0 END) AS chargeback_count,
	SUM(CASE WHEN state = 'checkback' THEN amount ELSE 0 END) AS chargeback_amount
FROM tmp
GROUP BY DATE_FORMAT(trans_date, "%Y-%m"), country;


-- 法二
select 
	month,country,
	count(case when state='approved' and tag=0 then 1 else null end) as approved_count,
	sum(case when state='approved' and tag=0 then amount else 0 end) as approved_amount,
	count(case when tag=1 then 1 else null end) as chargeback_count,
	sum(case when tag=1 then amount else 0 end) as chargeback_amount
from
	(select
		country,
		state,
		amount,
		date_format(c.trans_date,'%Y-%m') as month,
		1 as tag
	 from transactions t
right join chargebacks c
	on t.id=c.trans_id

union all 

select
	country,
	state,
	amount,
	date_format(t.trans_date,'%Y-%m') as month,
	0 as tag 
from transactions t 
where state = 'approved'
) a
group by month,country
order by month,country
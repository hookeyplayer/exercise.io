 -- Products 表记录着各商品价格变化的情况
 --  (product_id, change_date) 组合为主键
 -- 查询所有产品在2019-08-16的价格。假设所有产品的价格在变化之前均为10
 -- 法一
 with product_list as (
    select distinct product_id
    from Products
),
recent_price as (
    select product_id, new_price
    from (
        select product_id, new_price, 
            rank() over (partition by product_id order by change_date desc) as 'rk'
        from Products
        where change_date <= '2019-08-16'
    ) tmp
    where rk = 1
)

select p1.product_id, ifnull(p2.new_price, 10) as 'price'
from product_list p1
left join recent_price p2
on p1.product_id = p2.product_id


-- 姗姗
WITH

tmp1 AS (
SELECT a.product_id, a.new_price AS price FROM Products AS a
JOIN (
	SELECT product_id, MAX(change_date) change_date
	FROM Products
	WHERE change_date <= '2019-08-16'
	GROUP BY product_id
) AS b
ON a.product_id = b.product_id
AND a.change_date = b.change_date
),

-- 赋值null以10
tmp2 AS (
SELECT product_id, 10 AS price 
FROM Products 
WHERE change_date > '2019-08-16'
AND product_id NOT IN (SELECT product_id FROM tmp1)
)

SELECT * FROM tmp1
UNION 
SELECT * FROM tmp2
ORDER BY price DESC, product_id ASC;


-- 法二
select a.product_id,ifnull(b.new_price,10) price
from
(select distinct product_id from Products) a left join
(select product_id,new_price from Products where (product_id,change_date) in (select product_id,max(change_date) as change_date from Products where change_date<='2019-08-16' group by product_id)) b
on a.product_id=b.product_id
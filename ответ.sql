-- 1.1
SELECT ROUND(100*COUNT(promocode_id)/SELECT COUNT(*), 2) 
AS "Долю заказов с промокодами"
FROM orders;

-- 1.2
WITH tmp AS(
    SELECT 
        p.name,
        p.promocode_id
        RANK() OVER(PARTITION BY p.name ORDER BY(COUNT(promocode_id) DESC)) AS rnk
    FROM promocode AS p 
    LEFT JOIN orders AS o
    ON o.promocode_id=p.promocode_id
    )
SELECT 
    name,
    COUNT(order_id)
FROM tmp
WHERE rnk=1;

-- 1.3
SELECT 
    b.office_id,
    b.office_name
FROM buildings AS b
WHERE b.coffee_point_id IN (
    SELECT c.coffee_point_id 
    FROM consumption AS c
    WHERE c.cookies <= 1000
    ) AS tmp
ORDER BY c.cookies DESC
LIMIT 10;
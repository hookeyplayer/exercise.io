-- if
select *, 
    IF(x + y > z AND x + z > y AND y + z > x, 'Yes', 'No') as triangle 
    FROM triangle;

-- case when
SELECT *, CASE WHEN (x + y > z) AND (x + z > y) AND (y + z > x) THEN 'Yes'
               ELSE 'No' 
               END AS triangle
FROM triangle

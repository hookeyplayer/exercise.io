SELECT MIN(ABS(a.x - b.x)) AS shortest
FROM point AS a
JOIN point AS b
ON a.x <> b.x;


SELECT MIN(dis) AS shortest
FROM (
	SELECT @dis := if(@last_p IS NULL, NULL, x - @last_p) AS dis
		, @last_p := x
	FROM point, (
			SELECT @dis := NULL, @last_p := NULL
		) temp
	ORDER BY x ASC
) a
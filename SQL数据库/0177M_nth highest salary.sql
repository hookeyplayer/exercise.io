-- 找出工资第 N 高的员工的薪水
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
 DECLARE p INT;
 SET p = N - 1;
 RETURN (
    SELECT * FROM
     (SELECT DISTINCT Salary FROM Employee
      ORDER BY Salary DESC
      LIMIT 1 OFFSET p
     ) AS getNthHighestSalary);
END;

CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (     
  SELECT  IF(count<N,NULL,min) 
  FROM
    (SELECT MIN(Salary) AS min, COUNT(1) AS count
    FROM
      (SELECT DISTINCT Salary
      FROM Employee ORDER BY Salary DESC LIMIT N) AS a
    ) as b
  );
END

-- 2窗口函数
SELECT MAX(CASE WHEN rnk = 2 THEN Salary ELSE null END) AS SecondHighestSalary 
FROM (
SELECT Salary, ROW_NUMBER() OVER(ORDER BY Salary DESC) AS rnk FROM Employee 
) AS tmp 

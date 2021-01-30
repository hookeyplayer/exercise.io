-- 成绩由高到低排序，并列出排名
-- 当两个人获得相同分数时，取并列名次，且名次中无断档
SELECT *, DENSE_RANK() OVER(ORDER BY Score DESC) AS 'Rank'
FROM Scores; 

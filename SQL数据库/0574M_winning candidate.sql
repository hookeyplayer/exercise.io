-- 两张表candidate和vote
-- 找到当选者的名字
-- 注意：本题目中不考虑平票的情况

-- 子查询
SELECT Name FROM Candidate 
WHERE id =
(SELECT CandidateId FROM Vote
 GROUP BY CandidateId
 ORDER BY COUNT(*) DESC
 LIMIT 1
) ;


-- 联结
SELECT Name FROM Candidate AS a
JOIN
(SELECT CandidateId FROM Vote
 GROUP BY CandidateId
 ORDER BY COUNT(*) DESC
 LIMIT 1
) AS b
ON a.id = b.CandidateId;
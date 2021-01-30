-- 成绩由高到低排序，并列出排名
-- 当两个人获得相同分数时，取并列名次，且名次中无断档
SELECT *, DENSE_RANK() OVER(ORDER BY Score DESC) AS 'Rank'
FROM Scores;


-- 拓展
-- 2
-- 找到score表中最高分学生的学号与课程号
select sno, cno from score where degree=(select max(degree) from score);

-- 排序并取出最高分，存在缺陷，万一有两个最高分
-- limit 第一个参数表示位置，第二个参数表示查询多少条
select sno, cno from score order by degree desc limit 0, 1;
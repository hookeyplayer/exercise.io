-- 联合主键(student_id, course_id)
-- 查询每个学生的最高成绩及其相应的课程
-- 如果最高成绩相同则，输出课程编号最小的课程
-- 查询结果按照 student_id 升序排列
SELECT student_id, course_id, grade FROM (
SELECT *, ROW_NUMBER() OVER(PARTITION BY student_id ORDER BY grade DESC, course_id ASC) AS grade_rnk
FROM Enrollments
) AS tmp
WHERE grade_rnk = 1
ORDER BY student_id;
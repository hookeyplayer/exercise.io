-- 查询每个部门下的学生数，要列出所有部门，即使该部门没有学生
-- 结果按学生数降序、部门名称升序排列
SELECT a.dept_name, COUNT(b.student_id) AS student_number FROM department AS a
LEFT JOIN student AS b
ON a.dept_id = b.dept_id
GROUP BY a.dept_name
ORDER BY student_number DESC, a.dept_name;
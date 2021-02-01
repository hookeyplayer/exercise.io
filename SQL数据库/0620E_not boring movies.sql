-- 查询以输出带有奇数编号ID和非“无聊”描述的电影
-- 按等级排序结果
SELECT * FROM cinema
WHERE MOD(id, 2) = 1 AND description <> 'boring'
ORDER BY rating DESC;
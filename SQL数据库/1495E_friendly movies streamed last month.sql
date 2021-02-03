-- 查询2020年6月播放的儿童电影的标题，以任何顺序返回结果表
-- content_id是电视上某个频道中节目的 ID
-- Kids_content是一个枚举（'Y'，'N'）
 -- “ Y”表示内容适合小孩，“ N”表示内容不适合小孩

SELECT DISTINCT a.title
FROM Content a
JOIN TVProgram b
	ON a.content_id = b.content_id
WHERE a.content_type = 'Movies'
AND a.Kids_content = 'Y'
AND LEFT(b.program_date,7) ='2020-06';
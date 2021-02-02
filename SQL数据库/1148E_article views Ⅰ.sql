-- 查询所有查看了至少一篇自己的文章的作者，并按ID升序排列
SELECT DISTINCT author_id id 
FROM Views
WHERE author_id = viewer_id
ORDER BY id;
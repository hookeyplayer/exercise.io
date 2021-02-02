-- 查询在同一日期查看过不止一篇文章的所有用户，并按ID升序排列
SELECT DISTINCT viewer_id id
FROM (
	SELECT viewer_id, view_date FROM Views
	GROUP BY viewer_id, view_date
	HAVING COUNT(DISTINCT article_id) > 1
) tmp
ORDER BY id;
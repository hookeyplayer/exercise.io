-- 列出每一个节点及其所属类型
SELECT Id,
CASE WHEN p_id IS NULL THEN 'Root'
     WHEN id NOT IN (SELECT DISTINCT p_id FROM tree
                     WHERE p_id IS NOT NULL) THEN 'Leaf'
     ELSE 'Inner' END AS Type
FROM tree;
-- 找出actor与director合作至少3次的情况，并返回（actor_id，director_id）值
SELECT actor_id, director_id FROM ActorDirector
GROUP BY actor_id, director_id
HAVING COUNT(timestamp) >= 3;
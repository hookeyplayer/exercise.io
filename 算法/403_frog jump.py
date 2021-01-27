# 如果青蛙上一步跳跃了 k 个单位，那么接下来跳跃距离只能选择为 k - 1、k 或 k + 1个单位
from typing import List
class Solution:
    def canCross(self, stones: List[int]) -> bool:
    	# stones是stages的键
    	stages = {x: set() for x in stones}
    	stages[0] = {0}
    	end = stones[-1]

    	for key in stones:
    		steps = stages[key]
    		if not steps:
    			return False
    		# 遍历steps中的每一个走法
    		# 如果三种走法任意一种走到了结尾，退出循环
    		if any(map(lambda step: self._jump(stages, step, key, end), steps)):
    			return True

    	return False
    def _jump(self, stages, step, start, end):
    	steps = (step-1, step, step+1)
    	for s in filter(lambda x: x > 0 and start + x in stages, steps):
    		stages[start + s].add(s)
    		if start + s == end:
    			return True

    	return False

stones = [0, 1, 2, 3, 4, 8, 9]
test = Solution()
print(test.canCross(stones)) # F
stones = [0, 1, 3, 5, 6, 8, 12, 17]
print(test.canCross(stones)) # T 
from typing import List
from collections import deque
class Solution:
# BFS：用队列保存每个遍历的有效字符串，再对队列中的每个字符串再次遍历
# 初始字符串是第1层，与初始字符串相差1个char的为下1层
	def _valid_next(self, current: str, next_: str):
		return sum(1 for c, n in zip(current, next_) if c != n) == 1

	def minMutation(self, start: str, end: str, bank: List[str]) -> int:
		deck = deque()
		deck.append([start, '', 0])

		while deck:
			current, previous, steps = deck.popleft()

			if current == end:
				return steps

			for item in bank:
				if item != previous and self._valid_next(current, item):
					deck.append([item, current, steps+1])

		return -1

test = Solution()
start = "AACCGGTT"
end = "AAACGGTA"
bank = ["AACCGGTA", "AACCGCTA", "AAACGGTA"]
print(test.minMutation(start, end, bank)) # 2
# 拆分数字各位，平方加总，直到和为1，则是快乐数字；若无限循环，则不是快乐数字

class Solution(object):
	def is_happy(self, n):
		"""
		:type n: int
		:rtype: bool
		"""
		seen_numbers = []
		while n not in seen_numbers:
			seen_numbers.append(n)
			# n = sum([int(x) **2 for x in str(n)])
			n = sum(map(lambda x: int(x)**2, list(str(n))))
		return 'happy' if n == 1 else 'unhappy'

s = Solution()	
print(s.is_happy(19))	

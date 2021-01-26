# 考虑大小写
# 对字符串里的char排列组合
from collections import Counter
class Solution:
	def longestPalindrome(self, s: str) -> int:
		cnt_dict = Counter(s)
		a = sum(cnt_dict.values()) # 各个char出现次数加总
		print(a)
		b = sum(1 for x in cnt_dict.values() if x & 1) # 出现了奇数次的char
		print(b)
		return a if b == 0 else a-b+1

s = 'abbc'
test = Solution()
print(test.longestPalindrome(s))     
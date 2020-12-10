# 在大字符串里找小字符串，不考虑顺序
# O(N)
class Solution(object):
	def minWindow(self, s, t):
		"""
		:type s: str
		:type t: str
		:type: str
		"""
		# 指向sliding window的左右边界
		l, r = 0, 0
		min_len = len(s) + 1 # 初始值设最大，继而更新
		m = {} # 记录目标字符串
		count = 0 # count means the same chars of s[l, r] with t
		# 遍历t，将对应的字符及出现的次数存到hashmap里
		for i in t:
			m[i] = m.get(i, 0) + 1 
		# 遍历s,将遍历到的字母对应的hashmap中的值-1
		while r < len(s): 
			if s[r] in m: 
				m[s[r]] -= 1
				# 若-1后仍>=0，count+1
				if m[s[r]] >= 0: 
					count += 1
				while (count == len(t)): 
					if (r - l + 1 < min_len):
						min_len = r - l + 1
						res = s[l:r+1]
					if s[l] in m:
						m[s[l]] += 1
						if m[s[l]] > 0:
							count -= 1
					l += 1
			r += 1
		return res

s = Solution()
print(s.minWindow("ADOBECODEBANC", "ABC")) #BANC
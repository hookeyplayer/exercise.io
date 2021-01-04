# 一个字符串修改k个字符后，最长的相同字符组成的连续子序列
# input: "ABAB", k = 2
# output: 4
# input:"AABABBA", k = 1
# output: 4
class Solution(object):
	def characterReplacement(self, s, k):
		start = end = res = maxcur = 0
		count = [0] * 26
		while end < len(s):
			count[ord(s[end]) -65] += 1
			maxcur = max(maxcur, max(count))
			while (end - start + 1 - maxcur) > k:
				count[ord(s[start]) -65] -= 1
				start += 1
			res = max(res, end - start + 1)
			end += 1
		return res

# given "abcabc", 给出子串的长度3
# 双指针法+sliding window
class Solution(object):
# 1
	def lengthOfLongestSubstring(self, s):
		char_map = {}
		for i in range(256):
			char_map[i] = -1
		length = len(s)
		i = max_len = 0
		for j in range(length): 
			if char_map[ord(s[j])] >= i:
				i = char_map[ord(s[j])] + 1
			char_map[ord(s[j])] = j
			max_len = max(max_len, j - i + 1)
		return max_len
# 2
	def lengthOfLongestSubstring(self, s):
		char_map = {}
		res, start = 0, 0
		# 用end遍历每个数组
		for end in range(len(s)):
			if s[end] in char_map:
				# 更新每个字母最后一次出现的下标
				start = max(start, char_map[s[end]] + 1)
			char_map[s[end]] = end
			res = max(res, end - start + 1) # update res
		return res
# 3
	def lengthOfLongestSubstring(self, s):
		exist = [False] * 256
		length = len(s)
		max_len = i = 0
		for j in range(length):
			while(exist[ord(s[j])]):
				exist[ord(s[i])] = False
				i += 1
			exist[ord(s[j])] = True
			max_len = max(max_len, j - i + 1)
		return max_len
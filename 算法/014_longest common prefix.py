# Input: strs = ["flower","flow","flight"]
# Output: "fl"
class Solution(object):
# 1
# 最长的前缀不会超过最短的字符串
	def longestCommonPrefix(self, strs):
		if len(strs) == 0:
			return ''
		# 找出最短字符串的长度
		minLen = min([len(x) for x in strs])
		end = 0

		while end < minLen:
			for i in range(1, len(strs)):
				if strs[i][end] != strs[i-1][end]:
					return strs[0][:end]
			end += 1
		return strs[0][:end]
# 2
	def longestCommonPrefix(self, strs):
		ls = len(strs)
		if ls == 1:
			return strs[0]
		prefix = ''
		pos = 0
		while True:
			try:
				curr = strs[0][pos]
			except IndexError:
				break
			index = 1
			while index < ls:
				try:
					if strs[index][pos] != curr:
						break
				except IndexError:
					break
				index += 1
			if index == ls:
				prefix = prefix + curr
			else:
				break
			pos += 1
		return prefix

if __name__ == '__main__':
    s = Solution()
    print(s.longestCommonPrefix(["flower","flow","flight"]))
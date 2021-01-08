# 反转每个单词中的字符顺序，保持空格和单词的初始顺序
class Solution(object):
	def reverseWords(self, s):
		temp = s.split(' ')
		for i in range(len(temp)):
			temp[i] = temp[i][::-1]
		result = ' '.join(temp)
		return result

if __name__ == "__main__":
	test = Solution()
	print(test.reverseWords('I like Jerry'))
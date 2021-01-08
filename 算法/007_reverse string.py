class Solution(object):
# 1. slice
	def reverseString(self, s):
		return s[::-1]

# 2. recuce()
reduce(lambda x, y:x+y, [1, 2, 3, 4, 5]) calculates ((((1+2)+3)+4)+5)
	def reverseString(self, s):
		from functools import reduce
		return reduce(lambda x, y:y+x, s)

# 3. reversed() 对可迭代对象（list，set）反转
	def reverseString(self, s):
		s = list(s)
		return ''.join(reversed(s))

# 4. 遍历
	def reverseString(self, s):
		result = list(s)
		for i in range(len(result) // 2):
			temp = result[len(result)-i-1]
			result[len(result)-i-1] = result[i]
			result[i] = temp
		return ''.join(result)

if __name__ == "__main__":
	test = Solution()
	print(test.reverseString('Jerry'))
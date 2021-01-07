class Solution(object):
# hash
	# def singleNumbers(self, nums):
	# 	dict = {}
	# 	for i in nums:
	# 		try:
	# 			dict.pop(i)
	# 		except:
	# 			dict[i] = 1
	# 	return dict.popitem()[0]

# array
	# def singleNumbers(self, nums):
	# 	a = []
	# 	for i in nums:
	# 		if i in a:
	# 			a.remove(i)
	# 		else:
	# 			a.append(i)
	# 	return a.pop()

# 外部包
	# def singleNumber(self, nums):
	# 	from collections import Counter
	# 	cnt = Counter(nums)
	# 	for k, v in cnt.items():
	# 		if v == 1:
	# 			return k

# 异或：两个相同的数异或为0；0和任意数异或都为那个数；异或满足交换律
	def singleNumbers(self, nums):
		result = 0
		for i in range(len(nums)):
			result ^= nums[i]
		return result



test = Solution()
nums = [2, 2, 5, 3, 3]
print(test.singleNumbers(nums))

# 返回两个索引，使得其对应的值之和等于目标值，且唯一解

# 法一：brutal force
class Solution():
# 法零：
	def twoSum(self, nums, target):
		length = len(nums)
		for i in range(length):
			for j in range(i+1, length):
				if nums[i] + nums[j] == target:
					return [i, j]
# 法一
	def twoSum(self, nums, target):
		if len(nums) == 0:
			return []
		for index, num in enumerate(nums):
			for count in range(index+1, len(nums)):
				if num + nums[count] == target:
					return [index, count]

# 法二
	def twoSum(self, nums, target):
		hashmap = {}
		for index, num in enumerate(nums):
			temp = target - num
			try:
				hashmap[temp]
				return [hashmap[temp], index]
			except KeyError:
				hashmap[num] = index

# 法三：不会
	def twoSum(self, nums, target):
		nums_index = [(item, index) for index, item in enumerate(nums)]
		nums_index.sort()
		begin, end = 0, len(nums)-1
		while begin < end:
			curr = nums_index[begin][0] + nums_index[end][0]
			if curr == target:
				return [nums_index[begin][1], nums_index[end][1]]
			elif curr < target:
				begin += 1
			else:
				end -= 1
				
s = Solution()
nums = [2, 5, 8, 9]
print(s.twoSum(nums, 14))

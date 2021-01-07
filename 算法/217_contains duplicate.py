class Solution(object):
	# def containsDuplicate(self, nums):
	# 	return len(nums) != len(set(nums))
	def containsDuplicate(self, nums):
		if nums == []:
			return False
		for i in nums:
			nums.remove(i)
			if i in nums:
				return True
		return False

	# def containsDuplicate(self, nums):
	# 	if nums == []:
	# 		return False
	# 	from collections import Counter
	# 	# Counter的返回为字典，即列表元素：出现次数
	# 	con = Counter(nums)
	# 	if max(con.values()) > 1:
	# 		return True
	# 	return False

test = Solution()
nums = [1, 2, 3, 3]
print(test.containsDuplicate(nums))
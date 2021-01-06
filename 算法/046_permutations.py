from typing import List

class Solution:
#  1.库函数
    def permute(self, nums: List[int]) -> List[List[int]]:
    	# 为高效循环而创建迭代器的函数 itertools
        from itertools import permutations
    	# result = permutations(nums)
    	# result = [list(t) for t in result]
    	# return result
    	return list(permutations(nums))

# 2.DPS with swapping
    def permute(self, nums: List[int]) -> List[List[int]]:
    	res = []
    	if len(nums) == 0:
    		return res
    	self.get_permute(res, nums, 0)
    	return res
    def get_permute(self, res, nums, index):
    	if index == len(nums):
    		res.append(list(nums))
    		return
    	for i in range(index, len(nums)):
    		self.get_permute(res, nums, index+1)
    		nums[i], nums[index] = nums[index], nums[i]

# 3.回溯。数组path保存走过的路，若走完了全部的解，则弹出path最后的元素
    def permute(self, nums: List[int]) -> List[List[int]]:
    	visited = [0] * len(nums)
    	res = []
    	def dfs(path):
    		if len(path) == len(nums):
    			res.append(path)
    		else:
    			for i in range(len(nums)):
    				if not visited[i]:
    					visited[i] = 1
    					dfs(path + [nums[i]])
    					visited[i] = 0
    	dfs([])
    	return res

# 4.递归：每个数字为起始位置，剩余的全排列
    def permute(self, nums: List[int]) -> List[List[int]]:
    	res = []
    	self.dfs(nums, res, [])
    	return res
    # 对nums进行全排列，已有的结果放到path中，path放入res中
    def dfs(self, nums, res, path):
    	if not nums:
    		res.append(path)
    	else:
    		for i in range(len(nums)):
    			self.dfs(nums[:i] + nums[i+1:], res, path+[nums[i]])



nums = [1, 2, 3]
test = Solution()
print(test.permute(nums))
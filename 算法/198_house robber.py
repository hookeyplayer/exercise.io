# 不可以连着两户人家打劫
from typing import List
class Solution:
# dp[i] = max(dp[i-1], dp[i-2]+nums[i])
# 自底向上
    def rob(self, nums: List[int]) -> int:
    	if nums == None:
    		return 0
    	if len(nums) == 1:
    		return nums[0]

    	nums[1] = max(nums[0], nums[1])
    	for i in range(2, len(nums)):
    		nums[i] = max(nums[i] + nums[i-2], nums[i-1])

    	return nums[-1]

# 自顶向下
    def rob(self, nums: List[int]) -> int:
    	prev_max, curr_max = 0, 0
    	for num in nums:
    		temp = curr_max
    		curr_max = max(prev_max + num, curr_max)
    		prev_max = temp
    	return curr_max


    def rob(self, nums: List[int]) -> int:
    	if nums == None:
    		return 0
    	dp = [0] * len(nums)
    	dp[0] = nums[0]
    	for i in range(1, len(nums)):
    		if i < 2:
    			dp[i] = max(nums[i], dp[i-1])
    		else:
    			dp[i] = max(dp[i-2] + nums[i], dp[i-1])
    	return dp[len(nums)-1]



nums = [1,2,3,1] 
test = Solution()
print(test.rob(nums)) # 4
nums = [2,7,9,3,1]
print(test.rob(nums)) # 12
        
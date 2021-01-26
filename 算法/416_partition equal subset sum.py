# 分割等和子集
from typing import List
class Solution:
# DP 
    def canPartition(self, nums: List[int]) -> bool:
    	whole = sum(nums)
    	half = whole >> 1
    	# whole为奇数、数组最大值大于whole的一半 均不可能达到题意
    	if whole & 1 or max(nums) > half:
    		return False
    	nums.sort(reverse=True) # 从大到小
    	dp = [[False] * (half+1) for _ in range(2)]
    	dp[0][0] = True

    	for i in range(1, len(nums)):
    		index = i % 2
    		for j in range(nums[i]):
    			dp[index][j] = dp[index-1][j]
    		for j in range(nums[i], half+1):
    			dp[index][j] = dp[index-1][j] if dp[index-1][j] else dp[index-1][j-nums[i]]
    		if dp[index][-1]:
    			return True

    	return dp[-1][-1]

test = Solution()
nums = [1,5,11,5]
print(test.canPartition(nums))
nums = [1,2,3,5]
print(test.canPartition(nums))
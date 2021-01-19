from typing import List
class Solution:
# DP1
# 贪心
    def maxSubArray(self, nums: List[int]) -> int:
    	thisSum = 0
    	maxSum = -2**31
    	for i in range(len(nums)):
    		if thisSum < 0:
    			thisSum = 0
    		thisSum += nums[i]
    		maxSum = max(maxSum, thisSum)
    	return maxSum

# DP2
    def maxSubArray(self, nums: List[int]) -> int:
# 构造子序列时保证以第n个元素结尾
# 原先是正增益的作用，则包含到新的子序列中；否则抛弃前面的子序列
    	dp = [0] * len(nums)
    	dp[0] = nums[0]
    	ans = nums[0]
    	for i in range(1, len(nums)):
    		dp[i] = max(dp[i-1], 0) + nums[i]
    		ans = max(ans, dp[i])
    	return ans

# DP3
    def maxSubArray(self, nums: List[int]) -> int:
    	maxEndingHere = ans = nums[0]
    	for i in range(1, len(nums)):
    		maxEndingHere = max(maxEndingHere+nums[i], nums[i])
    		ans = max(maxEndingHere, ans)
    	return ans

if __name__ == '__main__':
	test = Solution()
	print(test.maxSubArray([-2, 3, -1, -8]))

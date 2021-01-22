# DP的核心：最优子结构、边界、状态转移公式
class Solution(object):
# O(n+2n) = O(n)
# 备忘录+DP
	def climbStairs(self, n: int) -> int:
		if n <= 2:
			return n
		dp = [0] * (n+1)
		dp[1] = 1
		dp[2] = 2
		for i in range(3, n+1):
			dp[i] = dp[i-1] + dp[i-2]
		return dp[n]

# basic DP
	def climbStairs(self, n: int) -> int:
		if n <= 2:
			return n
		if n == 1:
			return 1
		if n == 2:
			return 2
		a, b = 1, 2
		temp = 0
		for i in range(3, n+1):
			temp = a + b
			a = b
			b = temp
		return temp


test = Solution()
print(test.climbStairs(6))

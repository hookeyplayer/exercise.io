# 每次爬1或2阶，则一共有多少种方法攀顶？
# 1 <= n <= 45
# 爬到第n层要么是从第 n-1 层一步上来的，要不就是从 n-2 层2步上来的

class Solution(object):
# O(n+2n) = O(n)
	def climbStairs(self, n: int) -> int:
		if n <= 2:
			return n
		dp = [0] * (n+1)
		dp[1] = 1
		dp[2] = 2
		for i in range(3, n+1):
			dp[i] = dp[i-1] + dp[i-2]
		return dp[n]

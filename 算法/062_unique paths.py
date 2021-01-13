# only move right or down
# goal: bottom-right
# pattern: sum up left cell and up cell
# O(m + n + m*n) = O(n^2)
def uniquePaths(self, m: int, n: int) -> int:
	dp = [[0]*n for _ in range(m)] # m x n
	for i in range(m):
		dp[i][0] = 1
	for j in range(n):
		dp[0][j] = 1
	for i in range(1, m):
		for j in range(1, n):
			dp[i][j] = dp[i-1][j] + dp[i][j-1]
	return dp[m-1][n-1]
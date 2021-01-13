# 路障出现后，不能reach那一行/列的结尾了
# Input:
# [
#   [0,0,0],
#   [0,1,0],
#   [0,0,0]
# ]
# Output: 2
# Explanation:
# There is one obstacle in the middle of the 3x3 grid above.
# There are two ways to reach the bottom-right corner
from typing import List
def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
	m = len(obstacleGrid)
	n = len(obstacleGrid[0])
	if obstacleGrid[0][0] == 1:
		return 0
	if m == 1 or n == 1:
		if obstacleGrid[m-1][n-1] == 1:
			return 0
		else:
			return 1
	dp = [[0]*n for _ in range(m)]
	for i in range(m):
		if obstacleGrid[i][0] == 1:
			dp[i][0] = 0
			break
		dp[i][0] = 1
	for j in range(n):
		if obstacleGrid[0][j] == 1:
			dp[0][j] == 0
			break
		dp[0][j] = 1
	for i in range(1, m):
		for j in range(1, n):
			if obstacleGrid[i][j] == 1:
				dp[i][j] = 0
			else:
				dp[i][j] = dp[i-1][j] + dp[i][j-1]
	return dp[m-1][n-1]


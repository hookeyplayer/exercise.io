# 空间复杂度O(N) & 线性时间O(N)
# 计算其二进制数中1的数目并作为数组返回
# 法一
class Solution(object):
	def countBits(self, num):
		res = []
		for i in range(num+1):
			res.append(self.hammingWeight(i))

	def hammingWeight(self, n):
		count = 0
		while n:
			n &= n-1
			count += 1
		return count

# 法2.1：动态规划
	def countBits(self, num):
		res = [0] * (num + 1)
		for i in range(1, num+1):
			res[i] = res[i >> 1]


# 法2.2：动态规划
	def countBits(self, num):
		dp = [0 for i in range(num+1)]
		for i in range(1, num+1):
			dp[i] = dp[i & (i-1)] + 1
		return dp


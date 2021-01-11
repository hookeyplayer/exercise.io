# 数列是第i天的股价, 单次单笔交易
class Solution(object):
# 法0.1: 线性扫描，brutal force
# n选2pairs，O(n^2)

	def maxProfit(self, prices):
		profit = 0
		for index in range(len(prices)-1):
			diff = max(prices[index+1:]) - prices[index]
			if diff > profit:
				profit = diff
		return profit
# 法0.2
	def maxProfit(self, prices):
		length = len(prices)
		if length == 0:
			return 0
		maxProfit, low = 0, prices[0]
		for i in range(1, length):
			if low > prices[i]:
				low = prices[i]
			else:
				diff = prices[i] - low
				if diff > maxProfit:
					maxProfit = diff
		return maxProfit

# 法一：动态规划
# 法1.1:无额外空间

	def maxProfit(self, prices):
		if not prices:
			return 0
		profit = 0
		min_element = prices[0]
		dp = [0]
		for i in range(1, len(prices)):
			min_element = min(min_element, prices[i])
			dp.append(max(dp[i-1], prices[i] - min_element))
			if dp[-1] > profit:
				profit = dp[-1]
		return profit 

# 法1.2:额外空间跟踪

	def maxProfit(self, prices):
		if not prices:
			return 0
		profit = 0
		min_element = prices[0]

		for i in range(len(prices)):
			min_element = min(min_element, prices[i])
			profit = max(profit, prices[i] - min_element)
		return profit


s = Solution()
prices = [10, 3, 4, 8]
print(s.maxProfit(prices))

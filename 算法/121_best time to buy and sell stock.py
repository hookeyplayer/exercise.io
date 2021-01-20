# 数列是第i天的股价, 单次单笔交易
from typing import List
class Solution(object):
# 法一：DP
# 第i天卖，使利润最大的答案是前i-1天中的最低价格
    def maxProfit(self, prices: List[int]) -> int:
    	if len(prices) < 2:
    		return 0
    	# 记录两个变量 利润 和 最小（买入）价
    	profit = 0
    	minPrice = prices[0] # 前i-1天的最小价为buy
    	for i in prices:
    		minPrice = min(i, minPrice)
    		profit = max(i-minPrice, profit)
    	return profit

# need额外空间
    def maxProfit(self, prices: List[int]) -> int:
		if not prices:
			return 0
		profit = 0
		minPrice = prices[0]
		dp = [0]
		for i in range(1, len(prices)):
			minPrice = min(minPrice, prices[i])
			dp.append(max(dp[i-1], prices[i] - minPrice))
			if dp[-1] > profit:
				profit = dp[-1]
		return profit 

# 法二：线性扫描，brutal force
	def maxProfit(self, prices):
		profit = 0
		for index in range(len(prices)-1):
			diff = max(prices[index+1:]) - prices[index]
			if diff > profit:
				profit = diff
		return profit


if __name__ == "__main__":
    test = Solution()
    print(test.maxProfit([10, 3, 4, 8]))
        

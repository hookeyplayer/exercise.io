# 多次买卖
class Solution(object):
	def maxProfit(self, prices):
		return sum([y-x for x, y in zip(prices[0:-1], prices[1:]) if x < y])

prices = [7,1,5,3,6,4]
s = Solution()
print(s.maxProfit(prices))
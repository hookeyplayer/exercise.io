# 《剑指Offer》结论:i和i-1做与运算,i的二进制中的最右边1会变成0 
# goal: get one

# class Solution(object):
# 法一
# 	def hammingWeight(self, n):
# 		return bin(n)[2:].count("1")
# 法二：位运算
	def hammingWeight(self, n):
		count = 0
		while n:
			n &= n-1
			count += 1
		return count

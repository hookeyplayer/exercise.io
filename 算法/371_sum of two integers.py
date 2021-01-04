# 不能使用运算符，计算两数之和
class Solution(object):
# 法一
	def getSum(self, a, b):
		return sum([a, b])
# 法二
	# def getSum(self, a, b):
	# 	import ctypes
	# 	sum = 0
 #        carry = ctypes.c_int32(b)
 #        while carry.value != 0:
 #        	sum = a ^ carry.value
 #            carry = ctypes.c_int32(a & carry.value)
 #            carry.value <<= 1
 #            a = sum
 #        return sum

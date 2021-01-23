# 不能使用运算符，计算两数之和
class Solution(object):
# 法一
	def getSum(self, a, b):
		return sum([a, b])
# 法二:位运算
# 1+0=1, 0+1=1, 0+0 =0,1+1=0
	def getSum(self, a, b):
		import ctypes
		sum = 0
        carry = ctypes.c_int32(b)
        while carry.value != 0:
        	sum = a ^ carry.value
            carry = ctypes.c_int32(a & carry.value)
            carry.value <<= 1
            a = sum
        return sum

# 法三（不会）
    def getSum(a,b):
     while b!=0:
         ta = a
         a = a^b
         b = ((ta&b)<<1)&0xffffffff
     hibit = (a&0x80000000)>>31
     if hibit==1:
         return -(((~a)+1)&0xffffffff)
     else:
	return a&0xffffffff
		         

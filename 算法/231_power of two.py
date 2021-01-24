class Solution:
# 1
# 计算1的个数
    def isPowerOfTwo(self, n: int) -> bool:
    	if n < 0:
    		return False
    	binNum = bin(n)
    	return sum(map(lambda x:int(x), list(binNum[2:]))) == 1

# 2
# （2的整数幂）-1，二进制全部变成1，且位数降一位
# （2的整数幂）和（2的整数幂）-1 进行按位与运算结果是：0
    def isPowerOfTwo(self, n: int) -> bool:
    	return n & (n-1) == 0
    	
test = Solution()
print(test.isPowerOfTwo(3))

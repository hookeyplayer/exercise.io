# ax + by = Z 的解为：Z = gcd(x, y)
# 看Z是不是x,y最大公约数的倍数
class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
    	return z == 0 or (x+y >= z and z % self.gcd(x, y) == 0)

    # 1.移位（不会）
    def gcd(self, x, y):
    	if x == y:
    		return x
    	# 皆为偶数
    	if x&1 == 0 and y&1 == 0:
    		return self.gcd(x>>1, y>>1)<<1
    	elif x&1 == 0 and y&1 != 0:
    		return self.gcd(x>>1, y)
    	elif x&1 != 0 and y&1 == 0:
    		return self.gcd(x, y>>1)
    	# 皆为奇数
    	else:
    		bigger = max(x, y)
    		smaller = min(x, y)
    		# 应用更相减损术一次，差为偶数
    		return self.gcd(bigger-smaller, smaller)

    # # 2.九章算术：更相减损术
    # # 若两个整数相差悬殊，性能不佳
    # def gcd(self, x, y):
    # 	if x == y:
    # 		return x
    # 	if x < y:
    # 		return self.gcd(y-x, x)
    # 	return self.gcd(x-y, y)
    
    # # 3.辗转相除法：Euclidean algo
    # # 若两个整数较大，取模的性能不佳
    # def gcd(self, x, y):
    # 	return x if y == 0 else self.gcd(y, x%y)

    # # 4.定义法
    # def gcd(self, x, y):
    # 	smaller = min(x, y)
    # 	while smaller:
    # 		if x % smaller == 0 and y % smaller == 0:
    # 			return smaller
    # 		smaller -= 1

test = Solution()
print(test.canMeasureWater(3, 5, 4))
        
# ax + by = Z 的解为：Z = gcd(x, y)
# 看Z是不是x,y最大公约数的倍数
class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
    	return z == 0 or (x+y >= z and z % self.gcd(x, y) == 0)

    # 九章算术：更相减损术
    def gcd(self, x, y):
    	if x == y:
    		return x
    	if x < y:
    		return self.gcd(y-x, x)
    	return self.gcd(x-y, y)
    
    # 辗转相除法
    def gcd(self, x, y):
    	return x if y == 0 else self.gcd(y, x%y)

    # 定义法
    def gcd(self, x, y):
    	smaller = min(x, y)
    	while smaller:
    		if x % smaller == 0 and y % smaller == 0:
    			return smaller
    		smaller -= 1

test = Solution()
print(test.canMeasureWater(3, 5, 4))
        
class Solution:
# 1枚举
    def mySqrt(self, x: int) -> int:
    	if x == 0:
    		return 0
    	elif x < 0:
    		return 'error'
    	else:
    		i = 1
    		while True:
    			if (i+1)**2 > x >= i**2:
    				return i
    			i += 1

# 2    			
    def mySqrt(self, x: int) -> int:
    	y = int(x**0.5)
    	return y

# 不会
    def mySqrt(self, x: int) -> int:
    	# sqrt(x) = 2 * sqrt(x / 4) for n % 4 == 0
        # sqrt(x) = 1 + 2 * sqrt(x / 4) for n % 4 != 0
    	if x == 0:
    		return 0
    	if x < 4:
    		return 1
    	ans = 2 * self.mySqrt(x/4)
    	if (ans+1) * (ans+1) <= x and (ans+1) * (ans+1) >= 0:
    		return ans+1
    	return ans

if __name__ == '__main__':
	s = Solution()
	print(s.mySqrt(5))
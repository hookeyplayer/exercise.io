# 每次爬1或2阶，则一共有多少种方法攀顶？
# 1 <= n <= 45

# 题外话：Fibonacci
known = {0: 0, 1: 1}
def fib(n):
    if n in known:
        return known[n]
    else:
    	addup = fib(n-1) + fib(n-2)
    	known[n] = addup
    return addup

class Solution(object):
# 1.1: 由Fibonacci得来
	# C = {1: 1, 2: 2}
#    def climbStairs(self, n):
#        if n in Solution.C:
#            return Solution.C[n]
#        else:
#            result = Solution.C.get(n - 1, self.climbStairs(n - 1)) + \
#                     Solution.C.get(n - 2, self.climbStairs(n - 2))
#            Solution.C[n] = result
#            return result
# 1.2
	# def climbStairs(self, n):
	# 	if n <= 2:
    # 		return [1, 2][n-1]
    # 	first = 1
    # 	second = 2
    # 	count = 2
    # 	while count < n:
    # 		count += 1
    # 		current = first + second
    # 		if count == n:
    # 			return current
    # 		first = second
    # 		second = current

# 2 
    def climbStairs(self, n):
    	if n <= 1:
    		return 1
    	dp = [1] * 2
    	for i in range(2, n+1):
    		dp[1], dp[0] = dp[1] + dp[0], dp[1]
    	return dp[1]

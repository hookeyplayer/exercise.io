# .代表任何char
# *代表0或者更多之前的元素
# ".*" means "zero or more (*) of anyssss character (.)"
# s = "aab", p = "c*a*b"
# Output: true
# c can be repeated 0 times, a can be repeated 1 time
class Solution(object):
# recursion
    def isMatch(self, s: str, p: str) -> bool:
        if len(p) == 0:
            return len(s) == 0
        flag = len(s) != 0 and p[0] in {s[0], '.'}
        if len(p) >= 2 and p[1] == '*':
            return (flag and self.isMatch(s[1:], p) or (self.isMatch(s, p[2:])))
        else:
            return flag and self.isMatch(s[1:], p[1:])
if __name__ == '__main__':
    test = Solution()
    print(test.isMatch('like', 'l.k**e'))

# DP
    # def isMatch(self, s: str, p: str) -> bool:
    # 	# 初始化全False的二维数组
    # 	dp = [[False for i in range(len(p)+1)] for j in range(len(s)+1)]
    # 	# dp[i][j]的含义：s[0->i] 与 p[0->j]是否匹配
    # 	dp[0][0] = True
    # 	for i in range(1, len(p)+1):
    # 		dp[0][i] = p[i-1] == '*' and dp[0][i-2] and i > 1
    # 	for i in range(1, len(s)+1):
    # 		for j in range(1, len(p)+1):
    # 			if p[j-1] == '*':
    # 				dp[i][j] = dp[i][j-2] or (dp[i-1][j] and (s[i-1] == p[j-2] or p[j-2] == '.'))
    # 			else: # 否则求与
    # 				dp[i][j] = dp[i-1][j-1] and (p[j-1] == '.' or p[j-1] == s[i-1])
    # 	return dp[len(s)][len(p)]


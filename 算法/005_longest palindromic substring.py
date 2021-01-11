class Solution(object):
# DP
    def longestPalindrome(self, s: str) -> str:
    	n = len(s)
    	start, maxl = 0, 0
    	for i in range(n):
    		if i - maxl >= 1 and s[i-maxl-1 : i+1] == s[i-maxl-1 : i+1][::-1]:
    			start = i-maxl-1
    			maxl += 2
    			continue
    		if i - maxl >= 0 and s[i-maxl : i+1] == s[i-maxl : i+1][::-1]:
    			start = i-maxl
    			maxl += 1
    	return s[start : start+maxl]

# Manacher Algo, 时间复杂度线性O(n)
# 字符串长度永远是奇数
# 到了边界就可以出循环
    # def longestPalindrome(self, s: str) -> str:
    # 	T = '#'.join('^{}$'.format(s))
    # 	g = len(T)
    # 	G = [0] * g
    # 	C = R = 0
    # 	for i in range(1, g-1):
    # 		G[i] = (R > i) and min(R-i, G[2*C - i])

if __name__ == '__main__':
	test = Solution()
	print(test.longestPalindrome('abcacbe'))

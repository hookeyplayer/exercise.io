class Solution:
# 1.以单词的形式拆分列表
    def lengthOfLastWord(self, s: str) -> int:
    	if len(s) == 0:
    		return 0
    	temp = s.split(' ')
    	temp = [t for t in temp if len(t) > 0]
    	if len(temp) == 0:
    		return 0
    	else:
    		return len(temp[-1])
    		
# 2.直接遍历字符串
    def lengthOfLastWord(self, s: str) -> int:
        ans = 0
        n = len(s) - 1
        while n >= 0 and s[n] == ' ':
        	n -= 1
        从末尾开始遍历，碰到‘’就结束，否则ans++
        while n >= 0 and s[n] != ' ':
        	ans += 1
        	n -= 1
        return ans

if __name__ == '__main__':
	test = Solution()
	print(test.lengthOfLastWord('Good morning'))

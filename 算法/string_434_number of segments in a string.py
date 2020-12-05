# given string, return number of segments(non-space characters)
class Solution(object):

	# 法一：内置函数
    
    def count_segments(self, s):
        return len(s.split())

    # 法二：空值和非空值配对计数

    def count_segments(self, s):
    	segment_count = 0
    	for i in range(len(s)):
    		if (i == 0 or s[i-1] == ' ') and s[i] != ' ':
    			segment_count += 1
    	return segment_count

a = Solution()
print(a.count_segments("Hi this is me ok'ay ！")) # 6

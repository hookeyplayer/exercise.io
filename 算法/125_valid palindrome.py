# 只考虑字母和数字
class Solution:
# 1
# filter函数的两个参数：函数、序列；返回boolean为True的相应元素放到一个列表里
# isalnum方法检测字符串是否由字母和数字组成
    def isPalindrome(self, s: str) -> bool:
    	s = list(filter(str.isalnum, s.lower()))
    	return True if s == s[::-1] else False
    
# 2
    def isPalindrome(self, s: str) -> bool:
    	alnumsS = [t.lower() for t in s if t.isalnum()]
    	length = len(alnumsS)
    	if length <= 1:
    		return True
    	mid = length // 2
    	for i in range(mid+1):
    		if alnumsS[i] != alnumsS[length-i-1]:
    			return False
    	return True

if __name__ == "__main__":
    test = Solution()
    print(test.isPalindrome("race a car")) # false
    print(test.isPalindrome("A man, a plan, a canal: Panama")) # true

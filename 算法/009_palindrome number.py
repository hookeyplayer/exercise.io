# 1. 倒序切片，跟原来的数直接比较
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x >= 0:
        	if x == int(str(x)[::-1]):
        		return True
        	else:
        		return False
        return False

# 2. half compare
class Solution:
    def isPalindrome(self, x: int) -> bool:
    	if x < 0:
    		return False
    	n = len(str(x))
    	temp = str(x)
    	for i in range(n // 2):
    		if temp[i] != temp[n-1-i]:
    			return False
    	return True
    	

if __name__ == '__main__':
	test = Solution()
	print(test.isPalindrome(1431))
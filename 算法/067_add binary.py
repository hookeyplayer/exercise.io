# Input: a = "1010", b = "1011"
# Output: "10101"
class Solution:
    def addBinary(self, a: str, b: str) -> str:
    	num = int(a, 2) + int(b, 2)
    	ans = bin(num)
    	return ans[2:] # 否则是0b11
    	
if __name__ == '__main__':
	s = Solution()
	print(s.addBinary('1', '10'))
        
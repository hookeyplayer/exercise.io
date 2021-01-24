class Solution:

    def addStrings(self, num1: str, num2: str) -> str:
        i, j = len(num1)-1, len(num2)-1
        # carry记录进位
        carry = 0
        res = ''
        while i >= 0 or j >= 0:
        	d1 = int(num1[i]) if i >= 0 else 0
        	d2 = int(num2[j]) if j >= 0 else 0
        	t = d1 + d2 + carry
        	res = str(t % 10) + res
        	carry = t // 10
        	i, j = i-1, j-1
        return res if carry == 0 else str(carry) + res

test = Solution()
print(test.addStrings('389187', '222220101010101'))
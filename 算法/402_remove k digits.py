# 返回移除k个数字后的最小值

class Solution:
# 1. stack
# O(N)
    def removeKdigits(self, num: str, k: int) -> str:
    	lens = len(num) 	    	
    	if lens == k:
    		return '0'
    	stack = []
    	for a in num:
    		while k and stack and stack[-1] > a:
    			stack.pop()
    			k -= 1
    		stack.append(a)
    	# 栈中元素就是最终结果
    	return str(int(''.join(stack)))

test = Solution()
print(test.removeKdigits('41270936', 3))

# 2. greedy，依次局部最优解

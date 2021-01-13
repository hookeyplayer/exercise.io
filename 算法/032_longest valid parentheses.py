# string只有(或)
class Solution:
# 栈方法
    def longestValidParentheses(self, s: str) -> int:
    	stack = [-1] # 栈顶元素，即离当前合法子串左边最近的字符
    	ans = 0
    	for i, e in enumerate(s):
    		# 遇到前括号就进栈，遇到后括号就出栈（出栈分情况）
    		if e == '(':
    			stack.append(i)
    		elif e == ')':
    			stack.pop()
    			if not stack:
    				stack.append(i)
    			else:
    				ans = max(ans, i-stack[-1])
    	return ans

if __name__ == '__main__':
	a = Solution()
	test = ')()())'
	print(a.longestValidParentheses(test))
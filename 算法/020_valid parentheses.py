class Solution:
# try/except语句用来检测try语句块中的错误，从而让except语句捕获异常信息并处理
    def isValid(self, s: str) -> bool:
    	stack = [None]
    	dic = {')':'(', '}':{}, ']':'['}
    	for t in s:
    		if t in dic and dic[t] == stack[len(stack)-1]:
    			stack.pop()
    		else:
    			stack.append(t)
    	return len(stack) == 1

if __name__ == '__main__':
    # begin
    s = Solution()
    print(s.isValid(["{[))}"]))
        
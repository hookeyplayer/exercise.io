class MinStack:
    def __init__(self):
    	self.stack = [] # 主栈A
    	self.min_stack = [] # 备胎B辅助栈A

    # 入栈
    def push(self, x: int) -> None:
    	self.stack.append(x)
    	if len(self.min_stack) == 0 or x <= self.min_stack[-1]:
    		self.min_stack.append(x)

    # 出栈需判断是否是最小元素
    def pop(self) -> None:
    	if len(self.stack) > 0:
    		last = self.stack[-1]
    		if len(self.min_stack) > 0 and last == self.min_stack[-1]:
    			self.min_stack.pop()
    		self.stack.pop()

    # 返回栈顶元素
    def top(self) -> int:
    	if len(self.stack) > 0:
    		return self.stack[-1]
    	return None

    def getMin(self) -> int:
    	if len(self.min_stack) > 0:
    		return self.min_stack[-1]
    	return None

obj = MinStack()
obj.push(3)
obj.push(1)
obj.push(-3)
obj.push(-1)
obj.push(-5)
obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()
print(param_4)
print(param_3)
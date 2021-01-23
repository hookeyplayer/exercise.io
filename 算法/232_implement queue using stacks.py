# 栈是一个进出口
# 队列一个进口一个出口
class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    
    # enqueue,push元素进栈1
    def push(self, x: int) -> None:
        self.stack1.append(x)
        
    # 移除队首并返回
    # 栈1中的元素按顺序出栈，再按照出栈顺序入栈2，则两个栈顺序相反
    def pop(self) -> int:
        if len(self.stack2) == 0:
            while len(self.stack1):
                curr = self.stack1.pop()
                self.stack2.append(curr)
        self.stack2.pop()

    # 获取队首（不pop）
    def peek(self) -> int:
        # 当栈2空了，只要栈1中还有元素，就继续把它弹出栈1，并且入栈2
        if len(self.stack2) == 0:
            while len(stack1):
                curr = self.stack1.pop()
                self.stack2.append(curr)
        return self.stack2[-1]
        
    # 判断队列是否为空
    def empty(self) -> bool:
       return len(self.stack2) + len(self.stack1) == 0

obj = MyQueue()
obj.push(3)
obj.push(1)
obj.push(0)
obj.push(-4)
param_2 = obj.pop()
param_3 = obj.peek()
param_4 = obj.empty()
print(param_2, param_3, param_4)
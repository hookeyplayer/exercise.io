class Solution(object):
# 1 栈
# 遇到#，字符串不为空，就删除最后一个字符
# 如果不是#号，就拼接到字符串的最后。把两个字符串都求出来
    def backspaceCompare(self, S, T):
        if S == T:
            return true
        s_stack = []
        t_stack = []

        for c in S:
            if c != '#':
                s_stack.append(c)
            elif len(s_stack) != 0:
                s_stack.pop()

        for c in T:
            if c != '#':
                t_stack.append(c)
            elif len(t_stack) != 0:
                t_stack.pop()
                
        return s_stack == t_stack


test = Solution()
S = "ab#c"
T = "ad#c"
print(test.backspaceCompare(S, T))

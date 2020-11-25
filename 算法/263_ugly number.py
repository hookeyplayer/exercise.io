# 正数，且构成只能是2\3\5
# 迭代1
class Solution(object):
    def isUgly(self, num):
        if num <= 0:
            return False

        divisors = [2, 3, 5]
        for d in divisors:
            while num % d == 0:
                num /= d
        return num == 1

if __name__ == '__main__':
    s = Solution()
    print(s.isUgly(14))

# 迭代2
class Solution(object):
    def isUgly(self, num):
        if num <= 0:
            return False

        for i in [2, 3, 5]:
            while num % i == 0:
                num = num / i
        return True if num == 1 else False

# 递归
class Solution(object):
    def isUgly(self, num):
        if num <= 0:
            return False
        if num == 1:
            return True
        if num % 2 == 0:
            return self.isUgly(num / 2)
        elif num % 3 == 0:
            return self.isUgly(num / 3)
        elif num % 5 == 0:
            return self.isUgly(num / 5)
        else:
            return False

# https://blog.csdn.net/coder_orz/article/details/51317748
# class Solution(object):
#     def isUgly(self, num):
#         """
#         :type num: int
#         :rtype: bool
#         """
#         return num > 0 == 30**30 % num
# 给定n枚硬币排阶梯，k行有k个，返回k值

# 法一：二分查找
class Solution(object):
    def arrange_coins(self, n):
        
        # 1 +2 + 3 + ... + k = (k + 1) * k / 2 < n
        
        low, high = 0, n
        while low <= high:
            mid = (low + high) // 2
            total = (mid + 1) * mid // 2

            if total > n:
                high = mid - 1
            elif total < n:
                low = mid + 1
            else:
                return mid
            
        return low - 1

# 法二：求根公式
class Solution(object):
    def arrange_coins(self, n):

        # 1 +2 + 3 + ... + k = (k + 1) * k / 2 < n
        
        import math
        return (-1 + int(math.sqrt(1 + 8 * n))) // 2

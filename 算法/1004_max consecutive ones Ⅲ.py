from typing import List
class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        maxLength = 0
        l, r = 0, 0
        for r in range(len(A)):
            if A[r] == 0: # 分情况讨论：0的数量是否<=K
                if K == 0: # 此时窗口里包含了K个0，分情况讨论左指针
                    while A[l] == 1: # 需要移动至下1个0，再右移，才能减少1个0
                        l += 1
                    l += 1
                else:
                    K -= 1
            maxLength = max(maxLength, r-l+1) # 每次向右移动都维护变量maxLength
        return maxLength

test = Solution()
A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
K = 3
print(test.longestOnes(A, K))
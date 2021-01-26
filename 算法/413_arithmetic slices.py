# 等差数列
# 至少3个元素，相邻元素之差相同
# A slice (P, Q) of A is called arithmetic if:
# A[P], A[P + 1], ..., A[Q - 1], A[Q] is arithmetic,this means that P + 1 < Q
from typing import List
class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
    	if len(A) < 3:
    		return 0

    	dp = [0 for _ in range(len(A))]
    	d = A[1] - A[0]
    	start = 2

    	next_ = self._count(A, d, dp, start)
    	while next_ < len(A):
    		d = A[next_] - A[next_ - 1]
    		start = next_ + 1
    		next_ = self._count(A, d, dp, start)
    		
    	return sum(dp)

    def _count(self, A: List[int], d: int, dp: List[int], start: int) -> int: 
    	for i in range(start, len(A)):
    		if A[i] - A[i-1] == d:
    			dp[i] = dp[i-1] + 1
    		else:
    			return i
    	return len(A)


test = Solution()
A = [1, 2, 3, 4]
print(test.numberOfArithmeticSlices(A))
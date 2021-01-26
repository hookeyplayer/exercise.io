# 返回第三大数字，若无则返回最大的数字
from typing import List
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
    	bucket = [float("-inf"), float("-inf"), float("-inf")]
    	for num in nums:

    		for i in range(3):

    			if num > bucket[i]:
    				self._update(i, num, bucket)
    				break
    			if num == bucket[i]:
    				break

    	return bucket[-1] if bucket[-1] != float("-inf") else bucket[0]

    # bucket从大到小排序
    def _update(self, i, num, bucket):
    	if i == 0:
    		bucket[1], bucket[2] = bucket[0], bucket[1]
    		bucket[0] = num
    	elif i == 1:
    		bucket[2] = bucket[1]
    		bucket[1] = num
    	elif i == 2:
    		bucket[2] = num
        
        
nums = [2, 2, 3, 1]
test = Solution()
print(test.thirdMax(nums))
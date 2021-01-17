# 返回无重复的数列其长度
from typing import List
class Solution:
# 从总长度做减法
    def removeDuplicates(self, nums: List[int]) -> int:
    	if not nums:
    		return 0
    	length, index, a = len(nums), 1, nums[0]
    	for num in nums[1:]:
    		if num != a:
    			nums[index] = num
    			index += 1
    			a = num
    		else:
    			length -= 1
    	return length


# 从零做加法
    def removeDuplicates(self, nums: List[int]) -> int:
    	if len(nums) == 0:
    		return 0
    	ls = 0
    	for i in range(1, len(nums)):
    		if nums[ls] == nums[i]:
    			continue
    		else:
    			ls += 1
    			nums[ls] = nums[i]
    	return ls+1
        

if __name__ == '__main__':
    s = Solution()
    print(s.removeDuplicates([1, 2, 2, 3, 4, 4]))
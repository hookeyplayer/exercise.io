# input：sorted array of非重复整数，和target
# output：index或是应该插入的位置
from typing import List
class Solution:
# 二分查找
    def searchInsert(self, nums: List[int], target: int) -> int:
    	right = len(nums)-1
    	left = 0
    	while left < right:
    		mid = (left + right) // 2
    		if nums[mid] == target:
    			return mid
    		elif nums[mid] > target:
    			right = mid - 1
    		else:
    			left = mid + 1
    	# 到这里说明target不在nums里
    	if target > nums[left]:
    		return left + 1
    	else:
    		return left
        

if __name__ == '__main__':
    # begin
    s = Solution()
    print(s.searchInsert([1, 3, 5, 8], 9))
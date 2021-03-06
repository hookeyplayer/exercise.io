# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
from typing import List
class Solution:
# 二分
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left <= right:
        	mid = left + (right-left) // 2
        	if nums[mid] == target: return mid
        	if nums[mid] < nums[right]:
        		if nums[mid] < target and nums[right] >= target:
        			left = mid + 1
        		else:
        			right = mid - 1
        	else:
        		if nums[left] <= target and nums[mid] > target:
        			right = mid - 1
        		else:
        			left = mid + 1
        return -1
if __name__ == '__main__':
	test = Solution()
	nums = [3, 4, 5, 7, 9, 0, 1]
	print(test.search(nums, 9))

# 返回一个由每个区间 i 的 右侧区间 的最小起始位置组成的数组
from typing import List
class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
    	starts = []
    	# 构造字典，键为区间开始端点值，值为区间在原数组中的索引
    	index_dict = {}
    	for index, interval in enumerate(intervals):
    		starts.append(interval[0])
    		index_dict[interval[0]] = index
    	starts.sort()
    	return list(self.binary_find(starts, interval[1], index_dict) for interval in intervals)

    def binary_find(self, nums, target, index_dict):
    	if target in index_dict:
    		return index_dict[target]
    	l, r = 0, len(nums)-1
    	mid = l + (r-l) // 2
    	while l <= r:
    		if nums[mid] >= target and (mid == 0 or nums[mid-1] < target):
    			return index_dict[nums[mid]]
    		elif nums[mid] < target:
    			l = mid + 1
    		elif nums[mid] >= target and (mid == 0 or nums[mid-1] >= target):
    			r = mid - 1
    		mid = l + (r-l) // 2

    	return -1

test = Solution()
intervals = [[3,4],[2,3],[1,2]]
print(test.findRightInterval(intervals))
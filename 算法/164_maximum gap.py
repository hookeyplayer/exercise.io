from typing import List
import math
import sys
# Given an unsorted array
# find maximum difference between successive elements in sorted form
# 桶排序:O(N)
class Solution:

    def maximumGap(self, nums: List[int]) -> int:
    	m, n = min(nums), max(nums)
    	d = n - m
    	# 向上取整
    	bucketSize = math.ceil(d / (len(nums)-1))
    	# bucketSize = d // len(nums) + 1
    	bucketCount = int(d/bucketSize) + 1
    	# 二维桶
    	# +∞,−∞ for plain int values
    	# 记录每一个桶的最大和最小值
    	bucketMin, bucketMax = [sys.maxsize] * bucketCount, [-sys.maxsize] * bucketCount
    	buckets = []
    	for i in range(bucketCount):
    		# 当前值放到哪个桶里
    		# 第一个桶从min开始
    		index = (nums[i]-m) // bucketSize
    		bucketMin[index] = min(bucketMin[index], nums[i])
    		bucketMax[index] = max(bucketMax[index], nums[i])
    	premax, maxgap = bucketMax[0], 0
    	# 统计每个桶的最大值，和该桶右侧非空桶的最小值的差
    	for i in range(1, bucketSize+1):
    		if bucketMin[i] != sys.maxsize:
    			maxgap = max(maxgap, bucketMin[i]-premax)
    			premax = bucketMax[i]
    	return maxgap

test = Solution()
print(test.maximumGap([3, 6, 9, 1]))
# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# 时间复杂度：O(log(m+n))
from typing import List
class Solution:
# sort
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    	whole = nums1 + nums2
    	whole.sort()
    	l = len(whole)
    	mid = l // 2
    	if l%2 == 1:
    		return whole[mid]
    	else:
    		return (whole[mid-1] + whole[mid]) / 2.0

# merge sort
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    	m, n = len(nums1), len(nums2)
    	p1 = p2 = 0
    	whole = []
    	mid = 0.0
    	while p1 < m and p2 < n:
    		if nums1[p1] < nums2[p2]:
    			whole.append(nums1[p1])
    			p1 += 1
    		else:
    			whole.append(nums2[p2])
    			p2 += 1
    	mid = len(whole) // 2
    	if (m+n) % 2 == 1:
    		mid = whole[(m+n) // 2]
    	else:
    		mid = (whole[mid-1] + whole[mid]) / 2.0
    	return mid

if __name__ == '__main__':
	test = Solution()
	nums1 = [3, 4, 5, 6] 
	nums2 = [7, 9, 0, 1]
	print(test.findMedianSortedArrays(nums1, nums2))

        
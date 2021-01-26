# 无重复
from typing import List
class Solution:

    # def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
    # 	return list(set(nums1) & set(nums2))

    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
    	nums2.sort()
    	nums1.sort()
    	ans = set()
    	pos1, pos2 = 0, 0
    	while pos1 < len(nums1) and pos2 < len(nums2):

    		if nums1[pos1] == nums2[pos2]:
    			ans.add(nums1[pos1])
    			pos1 += 1
    			pos2 += 1
    		elif nums1[pos1] < nums2[pos2]:
    			pos1 += 1
    		else:
    			pos2 += 1
    			
    	return list(ans)
        

test = Solution()
nums1 = [1,2,2,1]
nums2 = [2,2]
print(test.intersection(nums1, nums2)) # [2]
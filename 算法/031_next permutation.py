# lexicographically next greater permutation
# 找出这个正整数所有数字全排列的下一个（大于且仅大于原数的新整数）
# 变换顺序的范围大小取决于当前整数的逆序区域
from typing import List
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
    	if not nums or len(nums) < 1:
    		return nums
    	index1, index2 = None, None
    	lens = len(nums)
    	# 这段循环找到逆序区域前一位的索引
    	for i in range(lens-1, 0, -1):
    		if nums[i-1] < nums[i]:
    			index1 = i - 1
    			break
    	# 否则说明列表降序，题目要求返回升序结果
    	else:
    		nums[:] = nums[::-1]
    		return
    	# 让逆序区域的前一位和逆序区域中（从右向左）刚刚大于它的最小数进行置换
    	for j in range(lens-1, 0, -1):
    		if nums[j] > nums[index1]:
    			index2 = j
    			break
    	nums[index2], nums[index1] = nums[index1], nums[index2]
    	nums[index1+1:lens] = nums[-1:index1:-1]

# nums = [0, 2, 3, 5, 4, 8, 6]
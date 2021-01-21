# 0, 1, 2 -> 红，白，蓝
 # E.W.Dijlstra 荷兰国旗问题（三向切分）
from typing import List
class Solution:
# # 双指针,快排+三向切分
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero = 0 # 第一个1的位置
        two = len(nums) - 1
        i = 0
        while i <= two:
            if nums[i] == 0: # i遇到0就换到左边去
                nums[zero] = nums[i]
                # nums[zero], nums[i] = nums[i], nums[zero]
                i += 1
                zero += 1
            elif nums[i] == 1: # 遇到1跳过
                i += 1
            elif nums[i] == 2: # i遇到2就换到右边去
                nums[two] = nums[i] # two记录第一个非2的位置
                nums[two], nums[i] = nums[i], nums[two]
                two -= 1

# countSort
    def sortColors(self, nums: List[int]) -> None:
        count = [0] * 3
        for num in nums:
            count[num] += 1
        pos = 0
        for i in range(3):
            while count[i] > 0:
                nums[pos] = i
                pos += 1
                count[i] -= 1
        return

# counter
    def sortColors(self, nums: List[int]) -> None:
    	from collection import Counter
    	count = Counter(nums)
    	for i in range(len(nums)):
    		if i < count[0]:
    			nums[i] = 0
    		elif i < count[1] + count[0]:
    			nums[i] = 1
    		else:
    			nums[i] = 2
    			
# Input: [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]    

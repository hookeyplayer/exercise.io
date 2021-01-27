# 求众数
# 定义不是寻常数学意义的众数，而是appears more than ⌊n / 2⌋ times
from typing import List
class Solution:
# 1 Boyer-Moore Majority Vote Algo
    def majorityElement(self, nums: List[int]) -> int:
    	cnt = 1
    	group = nums[0]

    	for i in range(len(nums)):
    		if cnt == 0:
    			cnt = 1
    			group = nums[i]
    			continue

    		if nums[i] == group:
    			cnt += 1
    		else:
    			cnt -= 1

    	return group


# 2.bit manipulation, 0-31位(int32)
# 每一位出现最多的0或1就是大量元素在该位的值
# 32次迭代, 每一次计算所有n个数的第i位的1的个数



# 3:因为肯定超过半数，所以排序找中间数
    # def majorityElement(self, nums: List[int]) -> int:
    # 	nums.sort()
    # 	return nums[len(nums) // 2]


# 4 hash
    # def majorityElement(self, nums: List[int]) -> int:
    # 	dic = {}
    # 	for num in nums:
    # 		dic[num] = dic.get(num, 0) + 1
    # 		if dic[num] > len(nums)/2:
    # 			return num



test = Solution()
nums = [3,2,3]
print(test.majorityElement(nums)) # 3
nums = [2, 2, 1, 1, 1, 2, 2]
print(test.majorityElement(nums)) # 2
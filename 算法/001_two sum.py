# 返回两个索引，使得其对应的值之和等于目标值，且唯一解
from typing import List
class Solution():

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {num: pos for pos, num in enumerate(nums)}
        for pos, num in enumerate(nums):
            other = target - num
            other_pos = dict.get(other, -1)

            if other in dict and other_pos != pos:
                return [pos, other_pos]

        return [-1, -1]


    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for index, num in enumerate(nums):
            temp = target - num
            try:
                hashmap[temp]
                return [hashmap[temp], index]
            except KeyError:
                hashmap[num] = index
                
# brutal force O(n^2)
# 双指针
    def twoSum(self, nums, target):
        nums_index = [(item, index) for index, item in enumerate(nums)]
        nums_index.sort()
        begin, end = 0, len(nums)-1
        while begin < end:
            curr = nums_index[begin][0] + nums_index[end][0]
            if curr == target:
                return [nums_index[begin][1], nums_index[end][1]]
            elif curr < target:
                begin += 1
            else:
                end -= 1

#   def twoSum(self, nums, target):
#       length = len(nums)
#       for i in range(length):
#           for j in range(i+1, length):
#               if nums[i] + nums[j] == target:
#                   return [i, j]

#   def twoSum(self, nums, target):
#       if len(nums) == 0:
#           return []
#       for index, num in enumerate(nums):
#           for count in range(index+1, len(nums)):
#               if num + nums[count] == target:
#                   return [index, count]              
s = Solution()
nums = [2, 5, 8, 9]
print(s.twoSum(nums, 14))


# # 统计文件行数1
# count = len(open(filepath, 'r').readlines())
# # 统计文件行数2
# count = 0
# for index, line in enumerate(open(filepath, 'r')):
#     count += 1

# 给定一行数列、一个值；需要移走数列里所有等于该值的instance,返回新的长度
# in-palce算法：算法输出结果覆盖算法的输入
from typing import List
class Solution:
# 1.two pointers
    # def removeElement(self, nums: List[int], val: int) -> int:
    # 	i, j = 0, 0
    # 	while j < len(nums):
    # 		if nums[j] == val:
    # 			j += 1
    # 		else:
    # 			if i != 1:
    # 				nums[i] = nums[j]
    # 			i += 1
    # 			j += 1
    # 	del nums[i : len(nums)]
    # 	return len(nums)

    # def removeElement(self, nums, val):
    # 	N = len(nums)
    #     l, r = 0, N - 1
    #     while l <= r:
    #         if nums[l] == val:
    #             nums[l] = nums[r]
    #             r -= 1
    #         else:
    #             l += 1
    #     return l

# 2. 覆盖
    def removeElement(self, nums, val):
        count =0
        for i in range(0,len(nums)):
            if nums[i] != val:
                nums[count] = nums[i]
                count +=1
        return count

    # def removeElement(self, nums: List[int], val: int) -> int:
    #     ls = len(nums)
    #     count = 0
    #     i = 0
    #     while i < ls - count:
    #         if nums[i] == val:
    #             nums[i] = nums[ls - 1 - count]
    #             count += 1
    #         else:
    #             i += 1
    #     return ls - count
    

if __name__ == '__main__':
    # begin
    s = Solution()
    print(s.removeElement([1, 3], 1))

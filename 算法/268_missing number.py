# 已知数列range[0,n]，找出遗漏的数
class Solution(object):
# 数学求法
    # def missingNumber(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: int
    #     """
    #     n = len(nums)
    #     num_sum = sum(nums)
    #     return (n ** 2 + n) / 2 - num_sum

# 法二：异或
    def missingNumber(self, nums):
        res = len(nums)
        for i, v in enumerate(nums):
            res ^= i
            res ^= v
        return res

 # ^为异或运算：将两数字相同位置但数值不同的值变为1
    
    # def missingNumber(self, nums):
    #     nums.sort()
    #     left, right = 0, len(nums) - 1
    #     while left <= right:
    #         mid = (left + right) / 2
    #         if nums[mid] <= mid:
    #             left = mid + 1
    #         else:
    #             right = mid - 1
    #     return left
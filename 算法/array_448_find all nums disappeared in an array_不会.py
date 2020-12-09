# 给定一组n个数，找到其中没在[1,n]出现的数
# 不使用额外空间且时间复杂度为O(n)

class Solution(object):
    def findDisappearedNumbers(self, nums):
        res = []
        for i, x in enumerate(nums):
            p = abs(x)
            if nums[p - 1] > 0:
                nums[p - 1] *= -1
        # print nums
        return [i + 1 for i, x in enumerate(nums) if x > 0]

class Solution(object):
    def findDisappearedNumbers(self, nums):
        res = []
        if nums:
            n = len(nums)
            for i in range(n):
                val = abs(nums[i]) - 1
                if nums[val] > 0:
                    nums[val] = -nums[val]
            for i in range(n):
                if nums[i] > 0:
                    res.append(i + 1)
        return res

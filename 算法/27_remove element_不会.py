# 给定一行数列、一个值；需要移走数列里所有等于该值的instance；返回新的长度

# class Solution(object):
# 	def removeElement(self, nums, val):
#         ls = len(nums)
#         if ls == 0:
#             return ls
#         count = 0
#         index = 0
#         while index < ls - count:
#             if nums[index] == val:
#                 nums[index] = nums[ls - 1 - count]
#                 count += 1
#             else:
#                 index += 1
#         return ls - count

# if __name__ == '__main__':
#     # begin
#     s = Solution()
#     print s.removeElement([1], 1)

# 一个指向前面等于val的数字，一个指向后面不等于val的数字，交换后移动的方式就是交换之后把末尾的指针前移；如果不进行交换操作则把前指针后移
# 时间复杂度是O(N)，空间复杂度是O(1)
class Solution(object):
    def removeElement(self, nums, val):
        N = len(nums)
        l, r = 0, N - 1
        while l <= r:
            if nums[l] == val:
                nums[l] = nums[r]
                r -= 1
            else:
                l += 1
        return l

# 使用了begin指针保存的是已经确定了没有val的数组范围，使用for循环来向后遍历查找不等于val的数字放入begin位置
# 做了很多无用功，即对出去了等于val的每个数字都做了一次赋值操作。
# 时间复杂度是O(N)，空间复杂度是O(1)
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        N = len(nums)
        begin = 0
        for i in range(N):
            if nums[i] != val:
                nums[begin] = nums[i]
                begin += 1
        return begin

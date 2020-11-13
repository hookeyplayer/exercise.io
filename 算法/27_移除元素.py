class Solution(object):
	'''
	给定一行数列、一个值；需要移走数列里所有等于该值的instance；返回新的长度
	'''
	def removeElement(self, nums, val):
        ls = len(nums)
        if ls == 0:
            return ls
        count = 0
        index = 0
        while index < ls - count:
            if nums[index] == val:
                nums[index] = nums[ls - 1 - count]
                count += 1
            else:
                index += 1
        return ls - count

if __name__ == '__main__':
    # begin
    s = Solution()
    print s.removeElement([1], 1)

    
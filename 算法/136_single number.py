# 一个非空数列，每个元素都出现了两次，除了一个元素。找出这个元素。
# 法一：异或
class Solution(object):
	def single_number(self, nums):
		r = 0
		for i in nums:
			r ^= i
		return r

if __name__ == '__main__':
	s = Solution()
	print(s.single_number([0, 2, 2, 3]))

# 法二：异或的不同写法
class Solution(object):
    # def singleNumber(self, nums):
    #     dic = {}
    #     for num in nums:
    #         try:
    #             dic[num] += 1
    #         except KeyError:
    #             dic[num] = 1
    #     for num in nums:
    #         if dic[num] == 1:
    #             return num

    # def singleNumber(self, nums):
    #     # set
    #     s = set()
    #     for num in nums:
    #         if num in s:
    #             s.remove(num)
    #         else:
    #             s.add(num)
    #     return s.pop()

    def singleNumber(self, nums):
        res = 0
        for num in nums:
            res ^= num
        return res

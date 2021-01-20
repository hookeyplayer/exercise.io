from typing import List
class Solution:
# 异或：两个相同的数异或为0；0和任意数异或都为那个数；异或满足交换律
	def singleNumbers(self, nums):
		result = 0
		for i in range(len(nums)):
			result ^= nums[i]
		return result

# 1
# O(N^2)
    def singleNumber(self, nums: List[int]) -> int:
    	for i in nums:
    		if nums.count(i) == 1:
    			return i

# 外部包，类似于1的方法
	def singleNumber(self, nums):
		from collections import Counter
		cnt = Counter(nums)
		for k, v in cnt.items():
			if v == 1:
				return k

# 2. hash O(1)
    def singleNumber(self, nums: List[int]) -> int:
    	dict = {}
    	for num in nums:
    		if num in dict:
    			dict[num] += 1
    		else:
    			dict[num] = 1
    	for key in dict.keys():
    		if dict[key] == 1:
    			return key

# 3. hash O(1)
    def singleNumber(self, nums: List[int]) -> int:
    	dict = {}
    	for i in nums:
    		try:
    			dict.pop(i)
    		except:
    			dict[i] = 1
    	return dict.popitem()[0]

# 4. array
	def singleNumbers(self, nums):
		a = []
		for num in nums:
			if num in a:
				a.remove(num) # 只移走一个
			else:
				a.append(num)
		return a.pop()

if __name__ == "__main__":
    test = Solution()
    print(test.singleNumber([2, 2, 5, 3, 3]))

# array是有序的
from typing import List
class Solution:
# 双指针
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
    	begin, end = 0, len(numbers)-1
    	while begin < end:
    		curr = numbers[begin] + numbers[end]
    		if curr == target:
    			return [begin+1, end+1]
    		elif curr < target:
    			begin += 1
    		else:
    			end -= 1


test = Solution()
numbers = [2,7,11,15]
target = 9
print(test.twoSum(numbers, target)) # [1, 2]
numbers = [2,3,4]
target = 6
print(test.twoSum(numbers, target)) # [1, 3]

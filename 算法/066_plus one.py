# 把一整个array看作一个整数，加一
from typing import List
class Solution:
# 1. 将数组转换成数字，加1， 再转换回去
    def plusOne(self, digits: List[int]) -> List[int]:
    	trans = 0
    	for i in range(len(digits)):
    		trans = trans*10 + digits[i]
    	# 加1
    	trans += 1
    	transback = str(trans)
    	res = []
    	for i in range(len(transback)):
    		res.append(int(transback[i]))
    	return res

# 1. 从各位开始，小学算术实操
    def plusOne(self, digits: List[int]) -> List[int]:
    	l = len(digits)
    	for index in reversed(range(l)):
    		if digits[index] < 9:
    			digits[index] += 1
    			return digits
    		else:
    			digits[index] = 0
    	digits.insert(0, 1)
    	return digits

        
if __name__ == '__main__':
	test = Solution()
	print(test.plusOne([1, 3, 9, 0]))

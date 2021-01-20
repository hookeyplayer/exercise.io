# Input: 5
# Output:
# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]
from typing import List
class Solution:
# 1.函数map(func, parameters)
    def generate(self, numRows: int) -> List[List[int]]:
    	if numRows == 0:
    		return []
    	ans = [[1]]
    	for i in range(1, numRows):
    		# print([0]+[1]) # [0, 1]
    		ans.append(list(map(lambda x,y:x+y, ans[-1]+[0], [0]+ans[-1])))
    	return ans

# 2. Sudoku Solver 数独
    def generate(self, numRows: int) -> List[List[int]]:
    	ans = []
    	for i in range(numRows):
    		ans.append([0] * (i+1))
    	for i in range(numRows):
    		for j in range(i+1):
    			if j == 0 or j == i:
    				ans[i][j] = 1
    			else:
    				# 递归
    				ans[i][j] = ans[i-1][j-1] + ans[i-1][j]
    	return ans

if __name__ == "__main__":
    test = Solution()
    print(test.generate(4))

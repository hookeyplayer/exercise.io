# every!对角线元素相等
class Solution(object):
# 1 切片相等
    def isToeplitzMatrix(self, matrix):
    	return all(matrix[row+1][1:] == matrix[row][:-1] for row in range(len(matrix)-1))

    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        for r in range(len(matrix) - 1):
        	for c in range(len(matrix[0]) - 1):
        		if matrix[r][c] != matrix[r+1][c+1]:
        			return False
        return True

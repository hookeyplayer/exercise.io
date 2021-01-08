# 按螺旋返回matrix里的元素
from typing import List
class Solution:
# 1. pop()
	def spiralOrder(self, matrix):
		res = []
		while matrix:
			# 取出上面一行
			res += matrix.pop(0)
			if matrix and matrix[0]:
				for m in matrix:
					# 取出每一行的最后一个元素
					res += [m.pop()]
			if matrix:
				# reversed取出底下一行
				res += matrix.pop()[::-1]
				t = []
				if matrix and matrix[0]:
					for m in matrix:
						# 取出每一行第一个元素
						t += [m.pop(0)]
					res += t[::-1]
		return res

# 2.维护4个边界，起始为matrix边界
	def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
		if matrix == []: return []
		up, left, down, right = 0, 0, len(matrix)-1, len(matrix[0])-1
		direct = 0 # direct, 0往右，1往下，2往左，3往上
		res = []
		while True:
			if direct == 0:
				for i in range(left, right+1):
					res.append(matrix[up][i])
				up += 1
			if direct == 1:
				for i in range(up, down+1):
					res.append(matrix[i][right])
				right -= 1
			if direct == 2:
				for i in range(right, left-1, -1):
					res.append(matrix[down][i])
				down -= 1
			if direct == 3:
				for i in range(down, up-1, -1):
					res.append(matrix[i][left])
				left += 1
			if up > down or left > right: return res
			direct = (direct+1) % 4

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
    	if not matrix or not matrix[0]: return []
    	m, n = len(matrix), len(matrix[0])
    	l, r, u, d = 0, n-1, 0, m-1
    	res = []
    	x, y = 0, 0
    	dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    	cur_d = 0 
    	while len(res) != n*m:
    		res.append(matrix[x][y])
    		if cur_d == 0 and y == r:
    			cur_d += 1
    			u += 1
    		elif cur_d == 1 and x == d:
    			cur_d += 1
    			r -= 1
    		elif cur_d == 2 and y == l:
    			cur_d += 1
    			d -= 1
    		elif cur_d == 3 and x == u:
    			cur_d += 1
    			l += 1
    		cur_d %= 4
    		x += dirs[cur_d][0]
    		y += dirs[cur_d][1]
    	return res


    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
    	if matrix is None or len(matrix) == 0:
    		 return matrix
    	m, n = len(matrix), len(matrix[0])
    	return self.get_spiralOrder(matrix, 0, m-1, 0, n-1)

    def get_spiralOrder(self, matrix, r_start, r_end, c_start, c_end):
    	if r_start > r_end or c_start > c_end:
    		return []
    	elif r_start == r_end:
    		return matrix[r_start][c_start : c_end+1]
    	elif c_start == c_end:
    		return [matrix[j][c_end] for j in range(r_start, r_end+1)]

    	curr = matrix[r_start][c_start:c_end+1] + \
    	[matrix[j][c_end] for j in range(r_start+1, r_end)] + \
    	matrix[r_end][c_start : c_end+1][::-1] +\
    	[matrix[j][c_start] for j in reversed(range(r_start+1, r_end))]

    	res = curr + self.get_spiralOrder(matrix, r_start+1, r_end-1, c_start+1, c_end-1)
    	return res

if __name__ == '__main__':
	test = Solution()
	matrix = [
	[1, 3, 5],
	[7, 9, 11],
	[13, 15, 17]
	]
	print(test.spiralOrder(matrix))

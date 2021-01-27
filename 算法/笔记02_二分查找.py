# 一维数组
# 列表需要已经sorted
def binary_search(list, item):
	low = 0
	high = len(list) - 1
	while low <= high:
		mid = (low + high) // 2
		guess = list[mid]
		if guess == item:
			return mid
		elif guess > item:
			high = mid - 1
		else:
			low = mid + 1
	return -1

my_list = [1, 3, 5, 7, 9]
print(binary_search(my_list, 3))

# 二维数组
class Solution():
	def find(self, target, array):
		rows = len(array) - 1
		cols = len(array[0]) - 1
		i = rows
		j = 0
		# 左下角出发
		while j < cols and i >= 0:
			if target < array[i][j]:
				i -= 1
			elif target > array[i][j]:
				j += 1
			else:
				return True
		return False

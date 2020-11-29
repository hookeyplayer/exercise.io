# 移除：n-1次
# 比较：1+2+3+...+(n-1)=n(n-1)/2,约为N^2/2
# 平移：=比较的次数
# 插入：n-1次
# 共计(N^2 + 2N -2), 记作O(N^2)

def insertion_sort(array):

	# 从索引1开始的循环，遍历数组
	# 变量index保存的是当前索引

	for index in range(1, len(array)):
		position = index
		temp = array[index]

		# 内部循环，检查position左侧的值是否大于temp
		# 若左侧大于temp，则将其右移一格
		# 继续往左检查

		while position > 0 and array[position - 1] > temp:
			array[position] = array[position - 1]
			position = position - 1

		# 最后将temp放回空隙

		array[position] = temp



array = [4, 2, 7, 1, 3]
print(insertion_sort(array))
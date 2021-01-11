# insert A[i] into sorted array A[0:i-1]
# pariwise swaps down to correct position of A[i]
# 移除：n-1次
# 比较：1+2+3+...+(n-1)=n(n-1)/2,约为N^2/2
# 平移：=比较的次数
# 插入：n-1次
# 共计(N^2 + 2N -2), 记作O(N^2)
def insertion_sort(array):
	# 变量index保存当前索引
	for i in range(1, len(array)):
		temp = array[i]
		while i > 0 and array[i - 1] > temp:
			array[i] = array[i - 1]
			i = i - 1
		# 最后将temp放回空隙
		array[i] = temp
	return array
	
array = [4, 2, 7, 1, 3]
print(insertion_sort(array))

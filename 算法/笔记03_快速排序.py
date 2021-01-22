# 冒泡排序基础上的递归分治
# 处理大数据最快的排序算法之一
# 最差:O(N^2)
# 平均:O(NlogN)，内循环短小，且常数因子小于一般的该时间复杂度的算法
# 对于顺序性差的随机数列，快速排序优于归并排序

# 1: 双边循环，O(logN)
def quickSort(arr, left, right):
	# 分区
	def partition(arr, left, right):
		pivot = arr[left]
		while left < right:
			# 从右指针开始作比较
			while left < right and arr[right] >= pivot:
				right -= 1
			# 否则，右指针停止，切换到左指针
			# arr[left] = arr[right] 
			arr[left], arr[right] = arr[right], arr[left]

			while left < right and arr[left] <= pivot:
				left += 1
			# 否则，左指针停止移动，将比基准大的交换到后面
			# arr[right] = arr[left] 
			arr[right], arr[left] = arr[left], arr[right]
		arr[left] = pivot
		return left
	if left < right:
		pivotIndex = partition(arr, left, right)
		quickSort(arr, left, pivotIndex-1)
		quickSort(arr, pivotIndex+1, right)
	return arr

# 2: 单边循环
def quickSort(arr, start, end):

	def partition(arr, start, end):
		# 每一轮当后面的数跟mark比较时，pivot所指的数不变
		# 右移mark指针，把比pivot小的元素和mark指针所指的元素交换
		pivot = arr[start]
		mark = start
		for i in range(start+1, len(arr)):
			if arr[i] < pivot:
				mark += 1
				arr[mark], arr[i] = arr[i], arr[mark]
		arr[start] = arr[mark]
		arr[mark] = pivot
		return mark

	if start < end:
		pivotIndex = partition(arr, start, end)
		quickSort(arr, start, pivotIndex-1)
		quickSort(arr, pivotIndex+1, end)
	return arr
	

array = [4, 8, 3, 5, 1, 2, 9]
print(quickSort(array, 0, len(array)-1))

# # 3: O(NlogN)
def quickSort(array):
	if len(array) <= 1:
		return array
	else:
		pivot = array[0] # 设置基准元素
		smaller = [i for i in array[1:] if i < pivot]
		bigger = [i for i in array[1:] if i > pivot] # 分成一小一大左右两组
		return quickSort(smaller) + [pivot] + quickSort(bigger)
	
array = [4, 8, 3, 5, 1, 2, 9]
print(quickSort(array))

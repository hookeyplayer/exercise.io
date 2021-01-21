# 冒泡排序基础上的递归分治
# 处理大数据最快的排序算法之一
# 最差:O(N^2)
# 平均:O(NlogN)，内循环短小，且常数因子小于一般的该时间复杂度的算法
# 对于顺序性差的随机数列，快速排序优于归并排序

# 1: O(NlogN)
def quickSort(array):
	if len(array) <= 1:
		return array
	else:
		pivot = array[0] # 设置基准元素
		smaller = [i for i in array[1:] if i < pivot]
		bigger = [i for i in array[1:] if i > pivot] # 分成一小一大左右两组
		return quickSort(smaller) + [pivot] + quickSort(bigger)
	
array = [8, 3, 5, 1, 2, 9]
print(quickSort(array))

# 2: O(logN)
def quickSort(arr, left, right):
	# 分区
	def partition(arr, left, right):
		pivot = arr[left]
		while left < right:
			while left < right and arr[right] >= pivot:
				right -= 1
			# 否则，比基准小的交换到前面
			# arr[left] = arr[right] 
			arr[left], arr[right] = arr[right], arr[left]
			while left < right and arr[left] <= pivot:
				left += 1
			# 否则，比基准大的交换到后面
			# arr[right] = arr[left] 
			arr[right], arr[left] = arr[left], arr[right]
		arr[left] = pivot
		return left
	# 递归
	if left < right:
		pivotIndex = partition(arr, left, right)
		quickSort(arr, left, pivotIndex-1)
		quickSort(arr, pivotIndex+1, right)
	return arr
 
array = [8, 3, 5, 1, 2, 9]
print(quickSort(array, 0, 5))

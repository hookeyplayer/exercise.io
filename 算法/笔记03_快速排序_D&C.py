def quicksort(array):
	if len(array) <= 1:
		return array
	else:
		pivot = array[0] # 设置基准元素
		smaller = [i for i in array[1:] if i < pivot]
		bigger = [i for i in array[1:] if i > pivot] # 分成一小一大左右两组
		return quicksort(smaller) + [pivot] + quicksort(bigger)
print(quicksort([8, 3, 5, 1, 2, 9]))

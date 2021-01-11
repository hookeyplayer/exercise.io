# def merge_sort(A):
# 	if len(A) <= 1:
# 		return A
# 	mid = len(A) // 2
# 	n1 = merge_sort(A[:mid])
# 	n2 = merge_sort(A[mid:])
# 	lpointer = 0
# 	rpointer = 0
# 	result = []
# 	while lpointer < len(n1) and rpointer < len(n2):
# 		if n1[lpointer] <= n2[rpointer]:
# 			result.append(n1[lpointer])
# 			lpointer += 1
# 		else:
# 			result.append(n2[rpointer])
# 			rpointer += 1
# 	result += n1[lpointer:]
# 	result += n2[rpointer:]
# 	return result

def quicksort(array):
	if len(array) <= 1:
		return array
	else:
		pivot = array[0] # 设置基准元素
		smaller = [i for i in array[1:] if i < pivot]
		bigger = [i for i in array[1:] if i > pivot] # 分成一小一大左右两组
		return quicksort(smaller) + [pivot] + quicksort(bigger)
print(quicksort([8, 3, 5, 1, 2, 9]))

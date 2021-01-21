def mergeSort(arr):
	# 归并
	def merge(left, right):
		result = []
		i = j = 0
		while i < len(left) and j < len(right):
			if left[i] <= right[j]:
				result.append(left[i])
				i += 1
			else:
				result.append(right[j])
				j += 1
		result = result + left[i:] + right[j:] # 剩余的元素直接添加至末尾
		return result
	# 递归
	if len(arr) <= 1:
		return arr
	mid = len(arr) // 2
	left = mergeSort(arr[:mid])
	right = mergeSort(arr[mid:])
	return merge(left, right)


# # 算法导论，可以运行，但未测试
def merge(A, p, q, r):
	N1 = A[p : q+1]
	N2 = A[q+1 : r+1]
	pointer = p
	while N1 and N2:
		if N1[0] <= N2[0]:
			A[pointer] = N1.pop(0)
		else:
			A[pointer] = N2.pop(0)
		pointer += 1
	tail = N1 if N1 else N2 # 落单的那个
	for last in tail:
		A[k] = last
		pointer += 1

def mergesort(A, p, r):
	if p < r:
		mid = (p+r-1) // 2
		mergesort(A, p, mid)
		mergesort(A, mid+1, r)
		merge(A, p, q, r)

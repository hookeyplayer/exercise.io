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

# 算法导论，可以运行，但未测试
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

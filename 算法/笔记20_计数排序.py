def countingSort(arr):
    # 输入的数据值转化为键，储存在开辟的数组空间里
	bucket = [0] * (max(arr) + 1) # list of zero's
	for a in arr:
		bucket[a] += 1
	i = 0
	for j in range(len(bucket)):
		while bucket[j] > 0: # 对array里出现的数遍历
			arr[i] = j
			bucket[j] -= 1
			i += 1
	return arr

array = [3, 1, 5, 4, 9, 18, 10]
print(countingSort(array))

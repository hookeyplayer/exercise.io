# 希尔是插入排序的高效率实现
# 《算法（第4版》的 Robert Sedgewick 提出
# 核心：间隔序列的设定
def shellSort(arr):
	lens = len(arr)
	gap = 1
	while gap < lens // 3:
		gap = gap*3 + 1
	while gap > 0:
		for i in range(gap, lens):
			curNum, preIndex = arr[i], i-gap
			# 将比curNum大的后移
			while preIndex >= 0 and curNum < arr[preIndex]:
				arr[preIndex+gap] = arr[preIndex]
				preIndex -= gap
			arr[preIndex+gap] = curNum
		# 下一个动态间隔
		gap //= 3
	return arr

array = [8, 3, 5, 1, 2, 9]
print(shellSort(array))


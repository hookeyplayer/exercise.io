# 不受输入数据的影响，任何情况的时间复杂度不变
# 每轮遍历都选出最小元素
# 1
def selectionSort(arr):
	for i in range(len(arr)-1): # 遍历n-1次
		minIndex = i
		for j in range(i+1, len(arr)):
			if arr[j] < arr[minIndex]:
				minIndex = j
		arr[i], arr[minIndex] = arr[minIndex], arr[i]
	return arr
# 2
def selectionSort(arr):
	newArr = []
	for i in range(len(arr)):
		a = findMinNumber(arr)
		newArr.append(arr.pop(a))
	return newArr

def findMinNumber(arr):
	pivot = arr[0]
	minIndex = 0
	for i in range(1, len(arr)):
		if arr[i] < pivot:
			pivot = arr[i]
			minIndex = i
	return minIndex

print(selectionSort([3, 5, 8, 1, 9, 0]))

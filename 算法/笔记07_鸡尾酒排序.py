# shakerSort/biDirectionalBubbleSort/rippleSort
# happyHourSort/shuffleSort/shuttleSort
def cocktailSort(arr):
	for i in range(len(arr)//2):
		isSorted = True
		# 从左至右
		for j in range(i, len(arr)-i-1):
			if arr[j] > arr[j+1]:
				arr[j], arr[j+1] = arr[j+1], arr[j]
				isSorted = False
		if isSorted:
			break
		isSorted = True
		for j in range(len(arr)-i-1, i, -1):
			if arr[j] < arr[j-1]:
				arr[j], arr[j-1] = arr[j-1], arr[j]
				isSorted = False
		if isSorted:
			break
		return arr

array = [2, 3, 5, 1, 9, 8, 10]
print(cocktailSort(array))

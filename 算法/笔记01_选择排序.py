# # 给列表排序
# def selectionSort(arr):
# 	newArr = []
# 	for i in range(len(arr)):
# 		a = findMinNumber(arr)
# 		newArr.append(arr.pop(a))
# 	return newArr

# print(selectionSort([3, 5, 8, 1, 9, 0]))

# # 查找列表里最小值和它的索引键
# def findMinNumber(arr):
# 	a = arr[0]
# 	a_index = 0
# 	for i in range(1, len(arr)):
# 		if arr[i] < a:
# 			a = arr[i]
# 			a_index = i
# 	return a_index

def selectionSort2(arr):
    m = len(arr)
    for i in range(m - 1):
        for j in range(i + 1, m):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

if __name__ == '__main__':
    array = [4, 2, 5, 6, 7, 9, 1, 8, 3, 10]
    print(selectionSort2(array))

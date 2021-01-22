# 对列表n-1次遍历，每次找一个最大元素
# 4+3+...+1 = 10
# (1+k)*k/2
# O(N^2)

# 优化1:设置无序数列的边界
def bubble_sort(arr):
    m = len(arr)	
    for i in range(m-1):
    	# 第一轮后有序区长度=1， 第二轮后有序区长度=2
    	for j in range(m - i - 1): # 已排序好的不用再遍历
    		if arr[j] > arr[j+1]:
    			arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# 优化2:布尔做标记，如果本轮元素有交换，则数列无序；否则说明已然有序，跳出大循环
def bubble_sort(list):
	unsorted_until_index = len(list) - 1
	sorted = False
	#除非排好了，否则不停
	while not sorted:
		sorted = True
		for i in range(unsorted_until_index):
			if list[i] > list[i+1]:
				sorted = False
				list[i], list[i+1] = list[i+1], list[i] # 同时赋值
		unsorted_until_index = unsorted_until_index - 1
# 经典
def bubble_sort(arr):
    m = len(arr)
    for i in range(m - 1):
        for j in range(i + 1, m):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr
if __name__ == '__main__':
    array = [4, 2, 5, 6, 7, 9, 1, 8, 3, 10]
    print(bubble_sort(array))

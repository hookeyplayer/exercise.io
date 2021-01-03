# 对列表多次重复遍历
# 两个指针不停地一直把较大的元素换到右边
# 每次轮回后，未排序的值中最大的会冒到正确位置上
def bubble_sort(list):

	# 该索引之前的数据都没排过序，一开始整个都没有排序，所以赋值给最后一个索引
	unsorted_until_index = len(list) - 1
	sorted = False

	#除非排好了，否则不停
	while not sorted:
		sorted = True

		# for循环会迭代未排序元素的索引值
		for i in range(unsorted_until_index):
			if list[i] > list[i+1]:
				sorted = False
				list[i], list[i+1] = list[i+1], list[i] # 同时赋值
		unsorted_until_index = unsorted_until_index - 1

list = [65, 44, 35, 14, 10]
bubble_sort(list)
print(list)
# 4+3+...+1 = 10
# (1+k)*k/2
# O(N^2)

def bubble_sort2(arr):
    m = len(arr)
    for i in range(m - 1):
        for j in range(i + 1, m):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

if __name__ == '__main__':
    array = [4, 2, 5, 6, 7, 9, 1, 8, 3, 10]
    print(bubble_sort2(array))

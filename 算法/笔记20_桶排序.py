# 桶排序是技术排序的升级
# 核心：在于映射函数的确定
# 任务：尽量增大桶的数量；使用的映射函数能够将输入的N个数据均匀分配到K个桶里
def bucketSort(arr, defaultBucketSize=5):
	maxVal, minVal = max(arr), min(arr)
	bucketSize = defaultBucketSize
	# 数据分组
	bucketCount = (maxVal - minVal) // bucketSize + 1
	# 二维桶
	buckets = []
	for i in range(bucketCount):
		buckets.append([])
	# 利用函数映射，将各个数据放入对应桶中
	for a in arr:
		buckets[(a - minVal) // bucketSize].append(a)
	# 清空arr
	arr.clear()
	for bucket in buckets:
		insertionSort(bucket)
		# 排序好的桶依次放入arr中
		arr.extend(bucket)
	return arr

def insertionSort(array):
	for i in range(len(array) - 1):
		# curNum是当前待插入的数
		curNum, preIndex = array[i+1], i
		while preIndex >= 0 and curNum < array[preIndex]:
			array[preIndex+1] = array[preIndex]
			preIndex -= 1
		array[preIndex+1] = curNum
	return array

	
array = [4, 2, 7, 1, 3]
print(bucketSort(array))
# LSD次位优先，从低位开始排序
# MSD主位优先，从高位开始
def radixSort(arr):
	mod = 10
	div = 1
	# 最大数的位数决定外循环的次数
	mostBit = len(str(max(arr)))
	# mod个空桶
	buckets = [[] for row in range(mod)]
	while mostBit:
		for a in arr:
			buckets[a // div % mod].append(a)
		# a的索引
		i = 0
		for bucket in buckets:
			while bucket:
				arr[i] = bucket.pop(0)
				i += 1
		div *= 10
		mostBit -= 1
	return arr


array = [4, 2, 7, 1, 3]
print(radixSort(array))
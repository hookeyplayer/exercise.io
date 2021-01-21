# 打扑克，将后面的牌（抽出来）插入前面已经排好的牌中
# 插入排序有一种优化：折半插入
# 但是折半不改变元素移动次数，只是减少了比较次数
# 移除：n-1次
# 比较：1+2+3+...+(n-1)=n(n-1)/2,约为N^2/2
# 平移：=比较的次数
# 插入：n-1次
# 共计(N^2 + 2N -2), 记作O(N^2)
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
print(insertionSort(array))

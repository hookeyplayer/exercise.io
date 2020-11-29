# 法一：迭代每个元素，检查索引是否偶数
def every_other(array)
	new_array = []

	# 读取n步：用数组的each_with_index方法做便利
	# 插入1/2步：如果元素索引值是偶数，则将该元素插入新数组
	# 共计记作：O(N)

	array.each_with_index do |element, index|
		new_array << element if index.even?
	end

	return new_array
end

# 法二：只读取数组中间隔的元素
def every_other(array)
	new_array = []
	idnex = 0

	# 读取1/2步：while循环跳过间隔的元素
	# 插入1/2步
	# 共计记作：O(N)


	while index < array.length
		new_array << array[index]
		index += 2
	end

	return new_array
end

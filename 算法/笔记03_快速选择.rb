# 无序数组，无须排序，只要找出百分位的值
# 快速排序和二分查找的结合
def quickselect!(kth_lowest_value, left_index, right_index)
	if right_index - left_index <= 0
		return @array[left_index]
	end

	# 返回分隔所用的轴的索引

	pivot_position = partition!(left_index, right_index)
	if kth_lowest_value < pivot_position
		quickselect!(kth_lowest_value, left_index, pivot_position - 1)
	elsif kth_lowest_value > pivot_position
		quickselect!(kth_lowest_value, pivot_position + 1, right_index)
	else
		return @array[pivot_position]
	end
end
class SortableArray
	attr_reader :array 

	def initialize(array)
		@array = array 
	end

	# partition方法：接受两个参数作为左右指针的起始位置

	def partition!(left_pointer, right_pointer)

		# 总是取最右的值为轴

		pivot_position = right_pointer
		pivot = @array[pivot_position]

		right_pointer -= 1

		while true do 

			# 两个指针块的判断（各自）若非，则停
			# 左指针可以越过右指针，指着轴，此时所指的值不再小于轴，便启动右指针

			while @array[left_pointer] < pivot do 
				left_pointer += 1
			end

			while @array[right_pointer] > pivot do
				right_pointer -= 1
			end

			# 如果此时两个指针还没有交叉或触碰
			# 则交换两指针所指的值
			# 重复步骤，直到两指针重合

			if left_pointer >= right_pointer
				break
			else
				swap(left_pointer, right_pointer)
			end

		end

		# 左指针的值和pivot交换，并返回左指针

		swap(left_pointer, pivot_position)
		return left_pointer
	end

	def swap(pointer_1, pointer_2)
		temp_value = @array[pointer_1]
		@array[pointer_1] = @array[pointer_2]
		@array[pointer_2] = temp_value
	end

end


# 快速排序依赖于分区

def quicksort!(left_index, right_index)
	if right_index - left_index <= 0
		return
	end

	# 使轴到正确的位置上
	# 通过：数组分为两部分，再返回轴的索引

	pivot_position = partition!(left_index, right_index)

	# 对左右各自递归调用

	quicksort!(left_index, pivot_position - 1)

	quicksort!(pivot_position + 1, right_index)
end


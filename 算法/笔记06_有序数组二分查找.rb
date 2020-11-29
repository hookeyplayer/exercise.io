def binary_search(array, value)
	lower_bound = 0
	upper_bound = array.lenth - 1 	# 开始时，数组第一个为下界，最后为上界

	# 循环检查中间元素

	while lower_bound <= upper_bound do
		midpoint = (upper_bound + lower_bound) / 2

		# 获取该中间格子的值

		value_at_midpoint = array[midpoint]

		# 不断调整界限

		if value < value_at_midpoint
			upper_bound = midpoint - 1
		elsif value > value_at_midpoint
			lower_bound = midpoint + 1
		elsif value == value_at_midpoint
			return midpoint
		end
	end

	# 若下界超越上界，则空值

	return nil
end

def linear_search(array, value)
	array.each do |element| #遍历数组的每一个元素

		if element == value
			return value

		elsif element > value
			break
		end
	end

	return nil #返回空值
end

linear_search([17, 3, 75, 202], 22)

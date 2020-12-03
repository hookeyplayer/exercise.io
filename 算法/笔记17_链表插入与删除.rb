class Node
	# Node有两个属性
	attr_accessor :data, :next_node

	def initialize(data)
		@data = data
	end
end

class Linkedlist 
	attr_accessor :first_node

	def insert_at_index(index, value)
		# 创建一个类
		new_node = Node.new(value)
		# 在开头插入
		if index == 0
			new_node.next_node = first_node
			return @first_node = new_node
		end
		current_node = first_node
		current_index = 0
		# 找出前一结点
		# 使前一结点的键指向新结点
		prev_index = index - 1
		while current_index < prev_index do 
			current_node = current_node.next_node
			current_index += 1
		end
		# 赋值
		new_node.next_node = current_node.next_node

		current_node.next_node = new_node
	end

	def delete_at_index(index)
		# 若删除的是第一个结点，则将当前的第二个结点设置成first_node
		if index == 0
			deleted_node = first_node
			@first_node = first_node.next_node
			return deleted_node
		end
		current_node = first_node
		current_index = 0
		# 若删除最后一个，则令倒数第二的结点的链指向null
		# 找出前一结点
		# 使前一结点的成为current
		while current_index < index - 1 do 
			current_node = current_node.next_node
			current_index += 1
		end
		deleted_node = current_node.next_node
		node_after_deleted_node = deleted_node.next_node
		current_node.next_node = node_after_deleted_node
	end
end


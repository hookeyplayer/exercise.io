# 组成链表的格子不连续
# 不相邻的格子叫结点，每个结点保存了数据和下一结点的内存地址


class Node
	# Node有两个属性
	attr_accessor :data, :next_node

	def initialize(data)
		@data = data
	end
end

# 赋值

node_1 = Node.new("once") 
node_2 = Node.new("upon") 
node_1.next_node = node_2
node_3 = Node.new("a") 
node_2.next_node = node_3
node_4 = Node.new("time") 
node_3.next_node = node_4

# LinkedList作用是指针，指向第一个结点

class LinkedList
	attr_accessor :first_node

	# 查找

	def index_of(value)
		current_node = first_node
		current_index = 0
		begin

			# 如果找到就返回

			if current_node.data == value
				return current_index
			end

			# 否则继续下一个结点
			
			current_node = current_node.next_node
			current_index += 1
		end while current_node

		# 如果遍历都没有找到则返回nil

		return nil
	end

	def initialize(first_node)
		@first_node = first_node
	end

	def read(index)
		current_node = first_node
		current_index = 0

		while current_index < index do

			# 顺着链往下找

			current_node = current_node.next_node
			current_index += 1

			# 若读到最后一个结点之后，则所找的索引不在链表中

			return nil unless current_node
		end
		return current_node.data
	end
end

# 设定链表的起始位置
list = LinkedList.new(node_1)
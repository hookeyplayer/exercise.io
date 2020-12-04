# O(V+E):V个顶点，V次出队；E条边，2E步访问邻结点
class Person
	attr_accessor :name, :friends, :visited

	def initialize(name)
		@name = name
		@friends = []
		@visited = false
	end

	def add_friend()
		@friends << friend
	end

	def display_network
		# 记下每个访问过的人，以便算法完结后能重置他们的visited属性为false
		to_reset = [self]
		# 创建一个开始就有根顶点(vertex)的队列，队列只能开头弹出一个
		queue = [self]
		self.visited = true

		while queue.any?
			# 设出队的顶点为当前顶点
			current_vertex = queue.shift
			puts current_vertex.name
			# 将当前顶点的所有未访问的邻接点加入队列
			# 即访问该结点的所有，包括访问过的
			current_vertex.friends.each do |friend|
				if !friend.visited
					to_reset << friend
					queue << friend
					friend.visited = true
				end
			end
		end
		# 算法完结时，将访问过的结点的 visited 属性重置为 false
		to_reset.each do |node|
			node.visited = false
		end
	end
end

# 创建人物
mary = Person.new("Mary")
peter = Person.new("Peter")
mary.add_friend(peter)

# 散列表
friends = {
	"Alice" => ["Bob", "Diana", "Fred"],
	"Bob" => ["Alice", "Cynthia", "Diana"], 
	"Cynthia" => ["Bob"],
	"Diana" => ["Alice", "Bob", "Fred"], 
	"Elise" => ["Fred"],
	"Fred" => ["Alice", "Diana", "Elise"]
}
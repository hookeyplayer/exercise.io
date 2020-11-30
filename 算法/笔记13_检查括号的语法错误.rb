# 栈类似数组，但有插入、读取、移除的约束：LIFO
class Linter

	attr_reader :error

	def initialize

		@stack = []

		def lint(text)
			# 循环读取文本每个字符
			text.each_char.with_index do |char, index|

				if opening_brace?(char)
					# 若遇到左括号，则压入栈中
					@stack.push(char)
				elsif closing_brace?(char)
					if closes_most_recent_opening_brace?(char)
						# 若读到右括号，且和栈顶匹配，则栈顶弹出
						@stack.pop
					else
						@error = "Incorrect closing brace: #{char} at index #{index}"
						return
					end
				end
			end
			# 若读完后栈不空，则缺相应右括号
			if @stack.any?
				@error = "#{stack.last} does not have a closing brace"
			end
		end

		private

		def opening_brace?(char)
			["(", "[", "{"].include?(char)
		end

		def closing_brace?(char)
			[")", "]", "}"].include?(char)
		end

		def opening_brace_of(char)
			{")" => "(", "]" => "[", "}" => "{"}[char]
		end

		def most_recent_opening_brace
			@stack.last
		end

		def closes_most_recent_opening_brace?(char)
			opening_brace_of(char) == most_recent_opening_brace
		end
	end

# test
linter = Linter.new
linter.lint("( var x = { y: [1, 2, 3] ) }")
puts linter.error # Incorrect closing brace: ) at index 25


linter.lint("( var x = { y: [1, 2, 3] }")
puts linter.error #  ( does not have a closing brace



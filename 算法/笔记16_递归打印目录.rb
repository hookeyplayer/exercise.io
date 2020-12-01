# 法一：循环
# 遍历文件系统，包括子目录的文件以及子目录里的子目录的文件
def find_directories(directory)
	Dir.foreach(directory) do |filename|

		# 遇到某个文件类型为子目录
		# 但不是代表当前目录或上级目录的句号和双句号那些文件，便打印名字
		# 只打印当前目录的直属子目录
		# 未打印子目录的子目录的

		if File.directory?("#{directory}/#{filename}") &&
			filename != "." && filename != ".." 
			puts "#{directory}/#{filename}"

			# 发起循环，遍历子目录的孙子目录

			Dir.foreach("#{directory}/#{filename}") do |inner_filename|
				if File.directory?("#{directory}/#{filename}/#{inner_filename}") &&
					inner_filename != "." && inner_filename != ".."
					puts "#{directory}/#{filename}/#{inner_filename}"
				end
			end
		end
	end
end

# 以当前目录为参数，调用find_directories 
find_directories(".")

# 法二：递归
# 适用于无法估算深度的问题
def find_directories2(directory)
	Dir.foreach(directory) do |filename|
		if File.directory?("#{directory}/#{filename}") &&
			filename != "." && filename != ".."
			puts "#{directory}/#{filename}"
			find_directories2("#{directory}/#{filename}")
		end
	end
end
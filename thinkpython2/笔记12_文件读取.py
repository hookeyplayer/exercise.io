# read()到达文件末尾时返回一个空字符串，所以删除字符串末尾空白
with open('pi_digits.txt') as file_object:
	contents = file_object.read()
	print(contents.rstrip())
	
# 经由路径读取
with open('text_files/filename.txt') as file_object:

# 逐行读取
filename = 'pi_digits.txt'
with open(filename) as file_object:
	for line in file_object:
		print(line.rstrip())

# 创建包含各行的列表
# readlines()从文件中读取每一行，并将其存储在一个列表中
# 列表lines的每个元素都对应于文件中的一行
filename = 'pi_digits.txt'
with open(filename) as file_object:
	lines = file_object.readlines()
for line in lines:
	print(line.rstrip())
	
# 三行连起来显示pi
with open('/Users/xiaofan/python练习/pi_digits.txt') as file_object:
		lines = file_object.readlines()
pi_string = ''
for line in lines:
	# pi_string += line.rstrip()
	pi_string += line.strip()
print(pi_string) 
print(len(pi_string))

# 生日是否在圆周率里
birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
	print("Your birthday appears in the first million digits of pi!")
else:
	print("Your birthday does not appear in the first million digits of pi.")


# 写入文件
filename = 'programming.txt'
with open(filename, 'w') as file_object:
	file_object.write("I love programming.\n")
	file_object.write("I also love programming.\n")

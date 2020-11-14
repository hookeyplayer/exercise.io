# 如果读取的是数字，就必须使用函数int()将其转换为整数
# 或使用函数float()将其转换为浮点数

# with open('/Users/xiaofan/python练习/pi_digits.txt') as file_object:
# 	contents = file_object.read() 
# 	print(contents.rstrip())
# 	lines = file_object.readlines()
#	逐行读取
#	for line in lines:
#		print(line.strip())

# 打印
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
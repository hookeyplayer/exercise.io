import json

# numbers = [2, 3, 5, 7, 11, 13]
# filename = 'numbers.json'

# with open(filename, 'w') as f_obj:
# 函数json.dump()接受两个实参:要存储的数据以及可用于存储数据的文件对象
# 	json.dump(numbers, f_obj) #存储到文件number里

# with open(filename) as f_obj:
# 	numbers = json.load(f_obj) #加载信息
# 	print(numbers)

username = input("What is your name? ")
# 存储用户名字
filename = 'username.json'
# with open(filename, 'w') as f_obj:
# 	json.dump(username, f_obj)
# 	print("We'll remember you when you come back, " + username + "!")
# # 向名字被储存的用户问候
# filename = 'username.json'
# with open(filename) as f_obj:
# 	username = json.load(f_obj)
# 	print("Welcome back, " + username + "!")
try:
	with open(filename) as f_obj:
		username = json.load(f_obj)
	except FileNotFoundError:
		username = input("What is your name? ")
		with open(filename, 'w') as f_obj:
			json.dump(username, f_obj)
			print("We'll remember you when you come back, " + username + "!")
	else:
		print("Welcome back, " + username + "!")

# 打印完整姓名
def get_formatted_name(first_name, last_name, middle_name = ''):
	if middle_name:
		full_name = first_name + ' ' + middle_name + ' ' + last_name	
	else:
		full_name = first_name + ' ' + last_name
	return full_name.title()
musician = get_formatted_name('jimi', 'hendrix', 'lee') 
print(musician)

# 用户互动输入信息，再问候
while True:
	print("\nPlease tell me your name:") 
	print("(enter 'q' at any time to quit)")

	f_name = input("First name: ")
	if f_name == 'q':
		break
	l_name = input("Last name: ")
	if l_name == 'q':
		break

		formatted_name = get_formatted_name(f_name, l_name) 
		print("\nHello, " + formatted_name + "!")

# 向函数传递列表，问候列表里的每一个人
# def greetings_all(list):
# 	for participant in list:
# 		print('hello to: ' + participant.title())
	
# participants = ['Alian', 'Bob', 'Clark']
# greetings_all(participants)

def greet_users(names):
	for name in names:
		msg = "Hello, " + name.title() + "!"
		print(msg)

usernames = ['hannah', 'ty', 'margot'] 
greet_users(usernames)

# 函数中对列表的修改是永久性的


# 用函数返回字典：某个人的信息
# 注释是错误的，因为返回值的age是个空值
# def built_person(first_name, last_name, age=''):
# 	'''
# 	input是名和姓
# 	返回名和姓为键的字典
# 	'''
# 	dictionary = {'first' : first_name,
# 	'last': last_name,
# 	'age': age}
# 	return dictionary

# musician = built_person('jimi', 'hendrix')
# print(musician)
def build_person(first_name, last_name, age=''):
	"""返回一个字典，其中包含有关一个人的信息
	age默认空字符串""" 
	person = {'first': first_name, 'last': last_name}
	if age:
		person['age'] = age
	return person

musician = build_person('jimi', 'hendrix', 27)
print(musician)


# name_function.py的文件里有如下函数get_formatted_name()将名和姓合并成姓名
def get_formatted_name(first, last):
	full_name = first + ' ' + last
	return full_name.title()

# from name_function import get_formatted_name
# print("Enter 'q' at any time to quit.") 
# while True:
# 	first = input("\nPlease give me a first name: ")
# 	if first == 'q':
# 		break
# 	last = input("Please give me a last name: ")
# 	if last == 'q':
# 		break
# 	formatted_name = get_formatted_name(first, last) 
# 	print("\tNeatly formatted name: " + formatted_name + '.')

# 使用python标准库

import unittest
from name_function import get_formatted_name
# 创建类，便于一系列针对get_formatted_name()的单元测试
# unittest类最有用的功能之一:断言方法
# assertEqual(a, b)：核实a == b
class NamesTestCase(unittest.TestCase):
	formatted_name = get_formatted_name('janis', 'joplin')
	self.assertEqual(formatted_name, 'Janis Joplin')

unittest.main()
# 其他断言方法：
# assertNotEqual(a, b)：核实a != b 
# assertTrue(x)：核实x为True 
# assertFalse(x)：核实x为False 
# assertIn(item, list)：核实item在list中
# assertNotIn(item, list)：核实item不在list中

# 创建一个类
class AnonymousSurvey():
	def __init__(self, question):
		self.question = question
		self.responses = []
	
	def show_question(self):
		print(question)

	def store_response(self, new_response):
		self.responses.append(new_response)

	def show_results(self):
		print("Survey results:")
		for response in responses:
			print('- ' + response)

# 为证明AnonymousSurvey类能够正确地工作，编写一个使用它的程序
from survey import AnonymousSurvey
#定义一个问题，并创建一个表示调查的AnonymousSurvey对象 
question = "What language did you first learn to speak?" 
my_survey = AnonymousSurvey(question)
#显示问题并存储答案 
my_survey.show_question()
print("Enter 'q' at any time to quit.\n")
while True:
	response = input("Language: ")
	if response == 'q':
		break
	my_survey.store_response(response)
# 显示调查结果
print("\nThank you to everyone who participated in the survey!")
my_survey.show_results()
title = "Alice in Wonderland" 
# 方法split()根据字符串创建列表
print(title.split()) # ['Alice', 'in', 'Wonderland']

# filename = 'alice.txt'
# try:
# 	with open(filename) as f_obj:
# 		contents = f_obj.read()
# except FileNotFoundError:
# 		msg = "Sorry, the file " + filename + " does not exist."
# 		print(msg)
# else:
# # 计算文件大致包含多少个单词
# 	words = contents.split()
# 	num_words = len(words)
# 	print("The file " + filename + " has about " + str(num_words) + " words.")

# 整合，定义函数，以便日后对其他书类似地分析
def count_words(filename):
	try:
		with open(filename) as f_obj:
			contents = f_obj.read() 
	except FileNotFoundError:
			msg = "Sorry, the file " + filename + " does not exist." 
			print(msg)
	else:
# 计算文件大致包含多少个单词 16 words = contents.split()
		words = contents.split()
		num_words = len(words)
		print("The file " + filename + " has about " + str(num_words) + " words.")

filename = 'alice.txt'
count_words(filename)
# 创建数字序列，并打印其乘方
# 法一 列表解析
squares = [value**2 for value in range(1, 11)]
print(squares)

# 法二,0.0s

# squares = []
# for value in range(1,11): 
# 	squares.append(value**2)
# print(squares)

# # 法三
# squares = []
# for value in range(1,11):
# 	square = value**2
# 	squares.append(square)
# print(squares)

# 法四很像法二，但0.1s
# for value in list(range(1, 11)):
# 	squares.append(value**2)
# print(squares)


# 字典的遍历
favorite_languages = {
	'Ken': 'Python',
	'Sophie': 'C++',
	'Mark': 'Java',
	}
# pairs
for name, language in favorite_languages.items():
	print(name.title() + "'s favorite language is " +
		language.title() + '.')
# key
for name in favorite_languages.keys():
	print(name.title())

# value
# 法一：
for language in set(favorite_languages.values()):
	print(language.title())

# 法二：有可能重复
# for language in favorite_languages.values():
# 	print(language.title() + "'s one of the languages.")

# 按顺序遍历
for name in sorted(favorite_languages.keys()):
	print(name.title() + " Thanks!")



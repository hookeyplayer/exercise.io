import random
dic = {k:random.randint(4, 9) for k in ['a', 'b', 'c']}
print(dic) # {'a': 9, 'b': 6, 'c': 6}


根据键排序
# 1. zip
dic = {'f': 'man', 'b': 'woman', 'c': 'animal'}
foo = zip(dic.keys(), dic.values())
foo = [i for i in foo]
print(foo) # [('a', 'man'), ('b', 'woman'), ('c', 'animal')]
a = sorted(foo, key=lambda x:x[0])
print(a) # [('b', 'woman'), ('c', 'animal'), ('f', 'man')]
# 排序完构造新字典
new_dic = {i[0]:i[1] for i in a}
print(new_dic) # {'b': 'woman', 'c': 'animal', 'f': 'man'}

# 2
dic = {'f': 'man', 'b': 'woman', 'c': 'animal'}
print(dic.items()) # dict_items([('f', 'man'), ('b', 'woman'), ('c', 'animal')])
b = sorted(dic.items(), key=lambda x:x[0])
print(b) # [('b', 'woman'), ('c', 'animal'), ('f', 'man')]
new_dic = {i[0]:i[1] for i in b}
print(new_dic)


# 根据key从小到大排序
dic = {"name":"zs",
"age":18,
"city":"深圳",
"tel":"1362626627"}
# 法1
l = sorted(dic.items(), key=lambda i:i[0], reverse=False)
print(l) # [('age', 18), ('city', '深圳'), ('name', 'zs'), ('tel', '1362626627')]
# 法2 dict函数
print(dict(l))
# {'age': 18, 'city': '深圳', 'name': 'zs', 'tel': '1362626627'}


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

# Ken's favorite language is Python.
# Sophie's favorite language is C++.
# Mark's favorite language is Java.

# # key
for name in favorite_languages.keys():
	print(name.title())
# Ken
# Sophie
# Mark

# # value
# # 法一：
for language in set(favorite_languages.values()):
	print(language.title())
# Python
# C++
# Java

# # 法二：有可能重复
for language in favorite_languages.values():
	print(language.title() + "'s one of the languages.")
# Python's one of the languages.
# C++'s one of the languages.
# Java's one of the languages.


# # 按顺序遍历
for name in sorted(favorite_languages.keys()):
	print(name.title() + " Thanks!")
# Ken Thanks!
# Mark Thanks!
# Sophie Thanks!

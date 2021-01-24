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
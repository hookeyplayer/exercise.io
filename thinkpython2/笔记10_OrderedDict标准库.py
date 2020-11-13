from collections import OrderedDict
favorite_languages = OrderedDict()

# 字典的录入因此有记忆顺序
favorite_languages['jen'] = 'python' 
favorite_languages['sarah'] = 'c' 
favorite_languages['phil'] = 'python'
favorite_languages['edward'] = 'ruby' 

for name, language in favorite_languages.items():
	print(name.title() + "'s favorite language is " + language.title() + ".")
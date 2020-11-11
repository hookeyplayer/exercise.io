favorite_languages = {
'jen': ['python', 'ruby'],
'sarah': ['c'],
'edward': ['ruby', 'go'], 
'phil': ['python', 'haskell'],
}
# 打印出人和喜欢的语言
# for person, language in favorite_languages.items():
	# print(person.title() + "'s favorite are:" + language.title())
 #    for language in language.values():
 #    	print('\t' + language.title())
for name, languages in favorite_languages.items():
	print("\n" + name.title() + "'s favorite languages are:")
	for language in languages: 
		print("\t" + language.title())
# 跟另一个列表《朋友》做关联查询，打印好朋友的喜欢语言
friends = ['phil', 'sarah']
for name in favorite_languages:
	if name in friends:
		print(" Hi " + name.title() +
			", I see your favorite language are " + str(favorite_languages[name]) + "!")
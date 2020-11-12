# 任意数量的关键字实参
# 返回一个包含所有信息的字典
# python看到**便创建空字典
def build_profile(first, last, **user_info): 
	profile = {}
	profile['first_name'] = first
	profile['last_name'] = last

	for key, value in user_info.items():
		# 将双星号字典里的键值对加入到最初的字典里
		profile[key] = value
	return profile

user_profile = build_profile('albert', 
	'einstein',
	location='princeton',
	field='physics')

print(user_profile)
import re
# 用100替换98
a = 'He got 98 scores'
ans = re.sub(r'\d+', '100', a)
print(ans)


# 过滤英文和整数
a = "not 404 found 张三 99 深圳"
l = a.split(' ')
print(l) #['not', '404', 'found', '张三', '99', '深圳']
ans = re.findall('\d+|[a-zA-Z]+', a) 
for i in ans:
	if i in l:
		l.remove(i)
new_str = ' '.join(l)
print(ans) # ['not', '404', 'found', '99']
print(new_str) # 张三 深圳

# 过滤小数和英文
a = "not 404 5.55 found 张三 99 深圳"
ans2 = re.findall('\d+\.?\d*|[a-aA-Z]+', a) 
for i in ans2:
	if i in l:
		l.remove(i)
new_str2 = ' '.join(l)
print(ans2) # ['404', '5.55', '99']
print(new_str) # 张三 深


# 用正则切分字符串输出['info', 'xiaoZhang', '33', 'shandong']
s="info:xiaoZhang 33 shandong"
res = re.split(r':| ', s) # 根据冒号或者空格切分
print(res)

# 正则匹配不是2或9结尾的手机号
tels = ['13324513568','13515201702', '13390963369','89639769367']
for tel in tels:
	ret = re.match('1\d{9}[0-3, 5-6,8-9]', tel)
	if ret:
		print('yes', ret.group())
	else:
		print('%s no' % tel)

# yes 13324513568
# yes 13515201702
# yes 13390963369
# 89639769367 no

# 正则匹配163邮箱
emails = ['chsy19a@econ.msu.ru', 'hookeyplayer@yandex.ru', 'lesley96911@163.com']
for email in emails:
	ret = re.match('[\w]{4,20}@163\.com$', email)
	if ret:
		print('%s yes:%s' % (email, ret.group()))
	else:
		print('%s no' % email)

s = '我会越来越100%自信！自卑0%'
a = re.findall(r'\d+', s) # ['100', '0']
b = re.match('我', s).group() # 我
c = re.search(r'\d+', s).group() # 100(因为是第一个匹配到的数据)

# 正则匹配中文
sentence = '中国，confidence，美国'
pattern = re.compile(r'[\u4e00-\u9fa5]+')
result = pattern.findall(sentence)
print(result) # ['中国', '美国']


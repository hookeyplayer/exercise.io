# lambda func
a = ['苏州', '', '', '南京']
ans = list(map(lambda x: '无' if x == '' else x, a))
print(ans) # ['苏州', '无', '无', '南京']

# 随机数
import random
a = 100 * random.random()
b = random.choice(range(0, 101)) # random int

# 列表去重
l = [11, 11, 12]
print([x for x in set(l)]) #[11, 12]

# 交集
a = [1, 2, 3, 5, 7, 8]
b = [3, 4, 5, 7, 8, 9]
ans1 = [x for x in a if x in b] # # [3, 5, 7, 8]
ans1 = list(set(a).intersection(set(b))) # [8, 3, 5, 7]
# 并集
ans2 = list(set(a).union(set(b)))
# 差集
aMinusb = list(set(b).difference(set(a))) # [9, 4]

# 平方的罗列
# 法一 列表解析
squares = [value**2 for value in range(1, 11)]
print(squares)

# 法二
squares = []
for value in range(1,11): 
	squares.append(value**2)
print(squares)

# 法三很像法二，但慢
for value in list(range(1, 11)):
	squares.append(value**2)
print(squares)

# lambda func
a = ['苏州', '', '', '南京']
ans = list(map(lambda x: '无' if x == '' else x, a))
print(ans) # ['苏州', '无', '无', '南京']
a = [1, 3]
b = ['a', 'b', 'c']
ans = [i for i in zip(a, b)]
print(ans) # [(1, 'a'), (3, 'b')]


# lambda func 从小到大排序
foo = [-5,8,0,4,9,-4,-20,-2,8,2,-4]
a = sorted(foo, key=lambda x:x)
print(a)


# lambda func specific 排序
# 正数从小到大，负数从大到小
foo = [-5,8,0,4,9,-4,-20,-2,8,2,-4]
b = sorted(foo, key=lambda x:(x<0, abs(x)))
print(b) # [0, 2, 4, 8, 8, 9, -2, -4, -4, -5, -20]


# lambda 对 列表嵌套字典 的排序
foo = [{"name":"zs","age":19},{"name":"ll","age":54}, {"name":"wa","age":17},{"name":"df","age":23}]
c = sorted(foo, key=lambda x:x['age'], reverse=True) # older to young
d = sorted(foo, key=lambda x:x['name']) # 姓名从小到大


# lambda 对 列表嵌套tuple 的排序
foo = [('me', 24), ('mum', 51), ('dad', 52)]
e = sorted(foo, key=lambda x:x[1], reverse=True)
# [('dad', 52), ('mum', 51), ('me', 24)]
f = sorted(foo, key=lambda x:x[0], reverse=False)
# [('dad', 52), ('me', 24), ('mum', 51)]


# lambda 对 列表嵌套列表 的排序，当年龄相同则添加参数按字母排序
foo = [['me', 25], ['she', 25], ['he', 26]]
g = sorted(foo, key = lambda x:(x[1], x[0]))
print(g) # [['me', 25], ['she', 25], ['he', 26]]
h = sorted(foo, key = lambda x:(x[0]))
print(h) # [['he', 26], ['me', 25], ['she', 25]]


a = (1, 'a')
b = (2, 'b')
anss = [i for i in zip(a, b)]
print(anss) # [(1, 2), ('a', 'b')]


# 求出列表所有奇数并构造新列表
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 1 filter方法
def fn(a):
	return a % 2 == 1
l = filter(fn, a)
l = [i for i in l]
print(l)

# 2
l = [i for i in a if i%2==1]
print(l)


# 合并
m = [1,5,7,9]
n = [2,2,6,8]
m.extend(n)
print(m)
m.sort(reverse=False)
print(m)


# 一行代码展开该列表
a = [[1,2],[3,4],[5,6]]
# 法1
x = [j for i in a for j in i]
print(x) # [1, 2, 3, 4, 5, 6]

# 法2
import numpy as np 
y = np.array(a).flatten()
print(y) #[1 2 3 4 5 6]
y2 = np.array(a).flatten().tolist()
print(y2) # [1, 2, 3, 4, 5, 6]


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

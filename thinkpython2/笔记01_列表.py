# lambda func
a = ['苏州', '', '', '南京']
ans = list(map(lambda x: '无' if x == '' else x, a))
print(ans) # ['苏州', '无', '无', '南京']
a = [1, 3]
b = ['a', 'b', 'c']
ans = [i for i in zip(a, b)]
print(ans) # [(1, 'a'), (3, 'b')]

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

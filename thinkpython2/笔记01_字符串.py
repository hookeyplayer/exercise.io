# # 字符串去重
s = 'yihkdnbbbk'
s = list(set(s))
s.sort(reverse=False)
ans = ''.join(s)
print(ans) # bdhikny

# 去空格的两种方法
a = 'I love mum and dad'
ans = a.replace(' ', '')
print(ans)

list = a.split(' ')
ans2 = ''.join(list)
print(ans2)

a = 'kjalfj;ldsjafl;hdsllfdhg;lahfbl;hl;ahlf;h'
from collections import Counter
print(Counter(a)) 
# Counter({'l': 9, ';': 6, 'h': 6, 'f': 5, 'a': 4, 'j': 3, 'd': 3, 's': 2, 'k': 1, 'g': 1, 'b': 1})

a = 'ab'
b = 'xyzz'
ans = [i for i in zip(a, b)]
print(ans) # [('a', 'x'), ('b', 'y')]

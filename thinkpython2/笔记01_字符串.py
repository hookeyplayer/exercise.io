# # 字符串去重
# s = 'yihkdnbbbk'
# s = list(set(s))
# s.sort(reverse=False)
# ans = ''.join(s)
# print(ans) # bdhikny

# 去空格的两种方法
a = 'I love mum and dad'
ans = a.replace(' ', '')
print(ans)

list = a.split(' ')
ans2 = ''.join(list)
print(ans2)
# # 32位的范围，超出返回0
class Solution:
# top 1
	def reverse(self, x:int) -> int:
		s = str(x)
		# 内置函数
		if s.startswith('-'):
			s1 = s[1:]
			if int('-' + s1[::-1]) < -2**31 - 1:
				return 0
			return int('-' + s1[::-1])
		else:
			if int(s[::-1]) > 2**31 - 1:
				return 0
			return int(s[::-1])

# top 2
	def reverse(self, x:int) -> int:
		s = str(x)[::-1].rstrip('-')
		if int(s) < 2**31:
			if x >= 0:
				return int(s)
			else:
				return -int(s)
		return 0

# top 3
	def reverse(self, x:int) -> int:
		sign = 0 if x < 0 else 1
		x = [i for i in str(abs(x))]
		res = ''
		for i in range(len(x)):
			res += x.pop()
		x = -int(res) if sign == 0 else int(res)
		if not -2**31 <= x <= 2**31 - 1:
			return 0
		return x


# 4. O(N)
	# def reverse(self, x:int) -> int:
	# 	y = 0 
	# 	j = 0 # 幂指数
	# 	sign = 0
	# 	# 判断input正负
	# 	if x < 0:
	# 		sign = 1
	# 		x *= (-1)
	# 	# 拆分整数
	# 	for i in str(x):
	# 		y = y + int(i) * pow(10, j) # 从个位开始
	# 		j += 1
	# 	if y > pow(2, 31) - 1:
	# 		return 0
	# 	if sign == 1:
	# 		y *= (-1)
	# 	return y

# 5
	# def reverse(self, x:int) -> int:
	# 	y = 0
	# 	sign = 0
	# 	if x < 0:
	# 		x *= -1
	# 		sign = 1
	# 	while x != 0:
	# 		pop = x % 10 # 取出低位
	# 		x = x // 10 # 循环拆解剩余的位
	# 		y = y * 10 + pop
	# 	if y > pow(2, 31) - 1:
	# 		return 0
	# 	if sign == 1:
	# 		return -y
	# 	return y


test = Solution()
x = -20300
print(test.reverse(x))
a = [1, 3, 5, 7, 9] # a[始:末:步]
print(a[1::-1]) # [3, 1]
print(a[:-3:-1]) # [9, 7]
print(a[-3::-1]) # [5, 3, 1]
print(a[::-2]) # [9, 5, 1]
print(a[::3]) # [1, 7]

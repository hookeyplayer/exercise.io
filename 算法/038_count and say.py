# 读数
# 1: one one
# 11: two ones
# 21: one two one one
# 1211: one one one two two ones

class Solution(object):
# 1, recursive
	def countAndSay(self, n):
		if n == 1:
			return '1'
		x = '1'
		# 每轮读自己
		while n > 1:
			x = self.count(x)
			n -= 1
		return x

	def count(self, x):
		m = list(x)
		res = []
		m.append(None)
		i, j = 0, 0
		while i < len(m) - 1:
			j += 1
			if m[j] != m[i]:
				# j-i是m[i]的计数
				res += [j-i, m[i]]
				i = j
		return ''.join(str(s) for s in res)

# 2
	def countAndSay(self, n):
		b = '1'
		for i in range(n-1):
			a = b[0] # 上一行的第一个字符
			c = '' # 存放读出的内容
			count = 0 # 对上一行计数
			for j in b:
				if a == j: 
					count += 1
				else:
					c += str(count) + a
					a = j
					count = 1
			c += str(count) + a
			b = c
		return b

if __name__ == '__main__':
	test = Solution()
	print(test.countAndSay(5))
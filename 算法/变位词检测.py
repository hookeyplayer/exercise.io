# 一个src是另一个src的排列组合
# heart 和 earth
# 1:检查第一个src中的所有字符是不是都在第二个src中出现
# O(n^2)
def anagram_1(s1, s2):
	s2_list = list(s2)
	pointer = 0
	match = True
	while pointer < len(s1) and match:
		pointer2 = 0
		found = False
		while pointer2 < len(s2_list) and not found:
			if s1[pointer] == s2_list[pointer2]:
				found = True
			else:
				pointer2 = pointer2 + 1
		if found:
			s2_list[pointer2] = None
		else:
			match = False
		pointer = pointer + 1
	return match
print(anagram_1("height", "eighth"))

# 2: 计数比较char的出现次数，创建含26个计数器的列表
# T(2n+26)
def anagram_2(a, b):
	c = [0] * 26
	d = [0] * 26
	for i in range(len(a)):
		pointer = ord(a[i]) - ord('a') # 返回ASCII值
		c[pointer] += 1
	for i in range(len(b)):
		pointer = ord(b[i]) - ord('a')
		d[pointer] += 1
		j = 0
		match = True
		
		while j < 26 and match:
			if c[j] == d[j]:
				j += 1
			else:
				match = False
	return match
print(anagram_2("apple", "pealp"))

# 3: sort
def anagram_3(a, b):
	a_list = list(a)
	b_list = list(b)
	a_list.sort()
	b_list.sort()
	pointer = 0
	match = True
	while pointer < len(a) and match:
		if a_list[pointer] == b_list[pointer]:
			pointer += 1
		else:
			match = False
	return match

print(anagram_3("height", "eighth"))

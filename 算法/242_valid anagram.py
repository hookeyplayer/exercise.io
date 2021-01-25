class Solution:
# 1
    def isAnagram(self, s: str, t: str) -> bool:
    	from collections import Counter
    	return Counter(s) == Counter(t)

# 2
    def isAnagram(self, s: str, t: str) -> bool:
    	return sorted(s) == sorted(t)

# 3
    def isAnagram(self, s: str, t: str) -> bool:
    	hms, hmt = {}, {}
    	for char in s:
    		hms[char] = hms.get(char, 0) + 1 
    	# hms: {'h': 2, 'e': 1, 'i': 1, 'g': 1, 't': 1}
    	for char in t:
    		hmt[char] = hmt.get(char, 0) + 1
    	return hms == hmt

if __name__ == '__main__':
	test = Solution()
	s = 'height'
	t = 'eight'
	print(test.isAnagram(s, t))


# 4: 计数比较char的出现次数，创建含26个计数器的列表
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

# 5: sort
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


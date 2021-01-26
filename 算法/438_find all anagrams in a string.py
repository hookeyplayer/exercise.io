# 找到所有异位词的start index
from typing import List
from collections import defaultdict
class Solution:

    def findAnagrams(self, s: str, p: str) -> List[int]:
    	if not s or not p:
    		return []

    	p_dict = defaultdict(int)
    	temp_dict = defaultdict(int) 

    	for char in p:
    		p_dict[char] += 1
    	# temp长度=s的前len(p)个字符
    	# temp值：每个字符在s[0:len(p)]中出现次数
    	for char in s[:len(p)]:
    		temp_dict[char] += 1

    	ans = []
    	# 两个字典相等则满足题意，记下start index的位置
    	for i in range(len(s) - len(p)):

    		if temp_dict == p_dict:
    			ans.append(i)
    		temp_dict[s[i]] -= 1

    		if temp_dict[s[i]] == 0:
    			temp_dict.pop(s[i])
    		temp_dict[s[i+len(p)]] += 1

    	if temp_dict == p_dict:
    		ans.append(len(s)-len(p))
    	return ans

    def findAnagrams(self, s: str, p: str) -> List[int]:
    	if not s or not p:
    		return []
    	# p_dict表示需要形成Anagram的字典，需要字符key各value个
    	p_dict = defaultdict(int)
    	for char in p:
    		p_dict[char] += 1

    	l, r = 0, 0
    	cnt = len(p)
    	ans = []
    	# 当cnt=0时，找到了一个满足解
    	while r < len(s):
    		p_dict[s[r]] -= 1
    		if p_dict[s[r]] >= 0:
    			cnt -= 1
    		if cnt == 0:
    			ans.append(l)
    		if r-l+1 == len(p):
    			if p_dict[s[l]] >= 0:
    				cnt += 1
    			p_dict[s[l]] += 1
    			l += 1
    		r += 1
    	return ans


s = "cbaebabacd" 
p = "abc"
test = Solution()
print(test.findAnagrams(s, p))


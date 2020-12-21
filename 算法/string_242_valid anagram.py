# anagram:变换字母顺序，变成另一个词
class Solution(object):
# 1
	def isAnagram(self, s, t):
    	hms, hmt = {}, {}
    	for char in s:
    		hms[char] = hms.get(char, 0) + 1
    	for char in t:
    		hmt[char] = hmt.get(char, 0) + 1
    	return hms == hmt
# 2
	def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return sorted(s) == sorted(t)
# 3
	def isAnagram(self, s, t):
		from collections import Counter
		return Counter(s) == Counter(t)

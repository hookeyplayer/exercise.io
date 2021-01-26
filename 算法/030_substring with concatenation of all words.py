from typing import List
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
    	ls = len(s)
    	word_ls = len(words[0])
    	target_dict = {}

    	for word in words:
    		try:
    			target_dict[word] += 1
    		except KeyError:
    			target_dict[word] = 1

    	ans = []
    	for start in range(ls - word_ls*len(words) + 1):
    		curr_dict = target_dict.copy()
    		for pos in range(start, start + word_ls*len(words), word_ls):
    			curr = s[pos:pos+word_ls]
    			try:
    				curr_dict[curr] -= 1
    				if curr_dict[curr] < 0: # word appears more than target
    					break
    			except KeyError: # word not in words
    				break
    		else:
    			ans.append(start)
    	return ans
    	
test = Solution()
s = "barfoothefoobarman" 
words = ["foo","bar"]
print(test.findSubstring(s, words))
# Output: [0,9]
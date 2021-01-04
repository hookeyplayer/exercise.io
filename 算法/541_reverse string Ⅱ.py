# reverse the first k characters for every 2k characters 
 # If there are <= k characters, reverse all of them.
 # If <= 2k & >= k, reverse the first k and left others as original.
class Solution(object):

	def reverseStr(self, s, k):
		s = list(s)
		for i in range(0, len(s), 2*k):
			s[i : i+k] = reversed(s[i : i+k])
		return "".join(s)

    # def reverseStr(self, s, k):
    #     """
    #     :type s: str
    #     :type k: int
    #     :rtype: str
    #     """
    #     N = len(s)
    #     ans = ""
    #     position = 0
    #     while position < N:
    #     	nx = s[position : position + k]
    #     	ans = ans + nx[::-1] + s[position+k : position+2*k]
    #     	position += 2*k
    #     return ans

s1 = Solution()
s="abcdefg"
k=2
print(s1.reverseStr(s,k))

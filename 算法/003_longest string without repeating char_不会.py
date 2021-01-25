# given "abcabc", 给出子串的长度3
class Solution(object):
# 0. DP
    def lengthOfLongestSubstring(self, s):
        exist = [False] * 256
        length = len(s)
        max_len = i = 0
        for j in range(length):
            while(exist[ord(s[j])]):
                exist[ord(s[i])] = False
                i += 1
            exist[ord(s[j])] = True
            max_len = max(max_len, j - i + 1)

        return max_len

    def lengthOfLongestSubstring(self, s):
        left, right = 0, 0
        res = 0
        char_map = {}
        for right in range(len(s)):
            if s[right] in char_map:
                left = max(left, char_map[s[right]] + 1)
            char_map[s[right]] = right
            res = max[res, right - left + 1]
        return res

    def lengthOfLongestSubstring(self, s):
        char_map = {}
        for i in range(256):
            char_map[i] = -1
        length = len(s)
        i = max_len = 0
        for j in range(length): 
            if char_map[ord(s[j])] >= i:
                i = char_map[ord(s[j])] + 1
            char_map[ord(s[j])] = j
            max_len = max(max_len, j - i + 1)
        return max_len
        
# 1:hash+双指针法+sliding window
# O(N)
        left, right = 0, 0
        char_map = {}
        res = 0
        while left < len(s) and right < len(s):
            if s[right] in char_map:
                if s[left] in char_map:
                    char_map.remove(s[left])
                left += 1
            else:
                char_map.add(s[right])
                right += 1
                res = max(rex, len(char))
        return res

# 无重复最长子串
class Solution(object):
    # def lengthOfLongestSubstring(self, s):
    #     exist = [False] * 256
    #     length = len(s)
    #     max_len = i = 0

    #     for j in range(length):

    #         while (exist[ord(s[j])]):
    #             exist[ord(s[i])] = False
    #             i += 1

    #         exist[ord(s[j])] = True
    #         max_len = max(max_len, j - i + 1)

    #     return max_len

    # def lengthOfLongestSubstring(self, s):
    #     char_map = {}
    #     for i in range(256):
    #         char_map[i] = -1
    #     length = len(s)
    #     i = max_len = 0
    #     # exists duplicate in current i, j
    #     for j in range(length): 
    #         if char_map[ord(s[j])] >= i:
    #             i = char_map[ord(s[j])] + 1
    #         char_map[ord(s[j])] = j
    #         max_len = max(max_len, j - i + 1)
    #     return max_len
        
# 1:hash+双指针法+sliding window
# O(N)
    # def lengthOfLongestSubstring(self, s: str) -> int:
    #     maxLenthAns = []
    #     tempAns = []
    #     if len(s) == 1:
    #         return len(s)
    #     for index, char in enumerate(s):

    #         if char not in tempAns:
    #             tempAns.append(char)
    #         else:
    #             del_index = tempAns.index(char)
    #             del tempAns[:del_index+1]
    #             tempAns.append(char)

    #         if len(maxLenthAns) < len(tempAns):
    #             maxLenthAns = tempAns[:]

    #     return len(maxLenthAns)

    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        char_map = []
        res = 0
        while left < len(s) and right < len(s):
            if s[right] in char_map:

                if s[left] in char_map:
                    char_map.remove(s[left])
                left += 1

            else: # 右移指针
                char_map.append(s[right])
                right += 1
                res = max(res, len(char_map))
        return res

# queue
    # def lengthOfLongestSubstring(self, s: str) -> int:
    #     ans = []
    #     max = 0
    #     for element in s:
    #         if len(ans) == 0 or element not in ans:

    #             ans.append(element)
    #             cur = len(ans)
    #             if cur > max:
    #                 max = cur

    #         else:
    #             while ans[0] != element:
    #                 ans.remove(ans[0])
    #             ans.remove(element)
    #             ans.append(element)
                
    #     return max

test = Solution()
print(test.lengthOfLongestSubstring('abcabc'))

# 一个字符串修改k个字符后，最长的相同字符组成的连续子序列
class Solution(object):
    # def characterReplacement(self, s: str, k: int) -> int:
    #     start, end = 0, 0
    #     res = 0
    #     maxcur = 0
    #     count = [0] * 26
    #     while end < len(s):
    #         count[ord(s[end]) - 65] += 1
    #         maxcur = max(maxcur, max(count))
    #         while (end - start + 1 - maxcur) > k:
    #             count[ord(s[start]) -65] -= 1
    #             start += 1
    #         res = max(res, end - start + 1)
    #         end += 1
    #     return res

    def characterReplacement(self, s: str, k: int) -> int:
        from collections import defaultdict
        # 统计窗口内每个字符出现过的次数
        window_count = defaultdict(int) 
        ans = 0
        l, r = 0, 0
        lens = len(s)
        # 窗口内出现最多次的字符
        max_repeat = 0 

        while r < lens:
            window_count[s[r]] += 1
            max_repeat = max(max_repeat, window_count[s[r]])
            # 判断条件
            while r-l+1-max_repeat > k:

                window_count[s[l]] -= 1
                max_repeat = max(max_repeat, window_count[s[l]])
                l += 1 

            ans = max(ans, r-l+1) 
            r += 1

        return ans

test = Solution()
s = "ABAB"
k = 2
print(test.characterReplacement(s, k))
# output: 4
s = "AABABBA"
k = 1
print(test.characterReplacement(s, k))
# output: 4

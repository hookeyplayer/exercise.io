class Solution(object):
    def minWindow(self, s: str, t: str) -> str:
        l, r = 0, 0
        min_len = len(s) + 1
        count = 0
        
        m = {} # 记录目标字符串
        for i in t:
            m[i] = m.get(i, 0) + 1 

        while r < len(s): 
            if s[r] in m: 
                m[s[r]] -= 1
                if m[s[r]] >= 0: 
                    count += 1

                while (count == len(t)): 
                    if (r - l + 1 < min_len): # 窗口小于s的长度时更新
                        min_len = r - l + 1
                        res = s[l:r+1]
                    if s[l] in m:
                        m[s[l]] += 1
                        if m[s[l]] > 0:
                            count -= 1
                    l += 1 # 左移

            r += 1 # 右移

        return res

s = Solution()
print(s.minWindow("ADOBECODEBANC", "ABC")) #BANC

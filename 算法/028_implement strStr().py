# 返回一个index，令needle首次出现在haystack中；若haystack不含needle则返回-1
class Solution:
# 1 内置函数
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)

# 2 切片
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)-len(needle)+1):
            if haystack[i : i+len(needle)] == needle:
                return i
        return -1

    # def strStr(self, haystack, needle):
    #     lsh, lsn = len(haystack), len(needle)
    #     if lsn == 0:
    #         return 0
    #     pos, index = 0, 0
    #     while index <= lsh - lsn:
    #         if haystack[index] == needle[0]:
    #             # slice index:index + lsn
    #             if haystack[index:index + lsn] == needle:
    #                 return index
    #         index += 1
    #     return -1


# 3 KMP: 在一个字符串S内查找一个词W的出现位置
    # https://discuss.leetcode.com/topic/3576/accepted-kmp-solution-in-java-for-reference/2
    def strStr(self, haystack, needle):
        lsH, lsN = len(haystack), len(needle)
        if lsN == 0:
            return 0
        next = self.makeNext(needle)
        i = j = 0
        while i < lsH:
            if j == -1 or haystack[i] == needle[j]:
                i += 1
                j += 1
                if j == lsN:
                    return i - lsN
            if i < lsH and haystack[i] != needle[j]:
                j = next[j]
        return -1

    def makeNext(self, needle):
        lsN = len(needle)
        next = [0] * lsN
        next[0], i, j = -1, 0, -1
        while i < lsN - 1:
            if j == -1 or needle[i] == needle[j]:
                next[i + 1] = j + 1
                if needle[i + 1] == needle[j + 1]:
                    next[i + 1] = next[j + 1]
                i += 1
                j += 1
            if needle[i] != needle[j]:
                j = next[j]
        return next
        
if __name__ == '__main__':
    # begin
    s = Solution()
    print(s.strStr('hello', 'll'))
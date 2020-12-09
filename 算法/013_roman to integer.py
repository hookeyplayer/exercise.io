# I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9
# X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90
# C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900
class Solution(object):
# 1
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = {'Ⅰ': 1, 'Ⅴ': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        prev, total = 0, 0
        for c in s:
            curr = roman[c]
            total += curr
            if curr > prev:
                total -= 2 * prev
            prev = curr
            return total
            
# 2
    def romanToInt(self, s):
        roman = {'Ⅰ': 1, 'Ⅴ': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        stack = []
        res = 0
        for inx, item in enumerate(s):
            res += roman[item]
            if item == 'V' or item == 'X':
                if stack and stack[-1] == 'I':
                    res -= 2
            elif item == 'L' or item == 'C':
                if stack and stack[-1] == 'X':
                    res -= 20
            elif item == 'D' or item == 'M':
                if stack and stack[-1] == 'C':
                    res -= 200
            stack.append(item)
        return res

# 3
    def romanToInt(self, s):
        roman = {'Ⅰ': 1, 'Ⅴ': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        ans = 0
        for i in range(len(s)):
            if i < len(s) - 1 and roman[s[i]] < roman[s[i+1]]:
                ans -= roman[s[i]]
            else:
                ans += roman[s[i]]
        return ans



s = Solution()
print(s.romanToInt('ⅠⅤ'))
print(s.romanToInt('LⅤⅠⅠⅠ'))


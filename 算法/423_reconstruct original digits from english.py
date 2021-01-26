# 'z' 只出现在 zero 中，因此 z 唯一确定 0 的个数；
# w，u，x，g 分别只出现在 two，four，six，eight 中，因此唯一确定 2，4，6，8.
# o 出现在 zero，two，four，one 中，由于 0，2，4 已经被确定，因此 1 可以被确定；
# h 出现在 three ，eight 中，8 已经被确定，因此 3 可以被确定；
# s 出现在 six，seven 中，由于 6 已经被确定，因此 7 可以被确定；
# i 出现在 five，six，eight，nine 中，由于 5，6，8 已经被确定，因此 9 可以被确定；

from collections import Counter
class Solution:

    def originalDigits(self, s: str) -> str:
    	ans = {}
    	cnt = Counter(s)

    	for key, char in zip([0, 2, 4, 6, 8], ['z', 'w', 'u', 'x', 'g']):
    		ans[key] = cnt.get(char, 0)

    	ans[1] = cnt.get('o', 0) - ans[0] - ans[2] - ans[4]
    	ans[3] = cnt.get('h', 0) - ans[8]
    	ans[5] = cnt.get('f', 0) - ans[4]
    	ans[7] = cnt.get('s', 0) - ans[6]
    	ans[9] = cnt.get('i', 0) - ans[5] - ans[6] - ans[8]

    	return ''.join(str(num) * ans[num] for num in range(0, 10))


# input: print(''.join('3'*3)) 
# output: 333

s = "owoztneoeroezr"
test = Solution()
print(test.originalDigits(s))
s = "fviefuroourf"
print(test.originalDigits(s))

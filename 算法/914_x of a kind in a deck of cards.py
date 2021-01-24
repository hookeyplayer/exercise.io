from typing import List
class Solution:
# gcd
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
    	from math import gcd
    	from collections import Counter
    	from functools import reduce
    	vals = Counter(deck).values()
    	return reduce(gcd, vals) >= 2

if __name__ == '__main__':
	test = Solution()
	deck = [2, 2, 3, 3]
	print(test.hasGroupsSizeX(deck))
        
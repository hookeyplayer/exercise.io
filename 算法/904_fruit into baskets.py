from typing import List
import collections
# 求一个数组的最长连续子数组，要求这个子数组中最多只存在两个不同的元素
class Solution:
    def totalFruit(self, tree: List[int]) -> int:
    	basket = 2
    	ans = 0
    	start = 0
    	queueMap = {}
    	for i, v in enumerate(tree):
    		queueMap[v] = queueMap.get(v, 0) + 1
    		if len(queueMap) > 2:
    			queueMap[tree[start]] -= 1
    			if queueMap[tree[start]] == 0:
    				del queueMap[tree[start]]
    			start += 1
    		ans = max(ans, i - start + 1)
    	return ans


# 不会
    def totalFruit(self, tree: List[int]) -> int:
    	ans = 0
    	i = 0
    	cnt = collections.Counter()
    	for j, x in enumerate(tree):
    		cnt[x] += 1
    		while len(cnt) >= 3:
    			cnt[tree[i]] -= 1
    			if cnt[tree[i]] == 0:
    				del cnt[tree[i]]
    			i += 1
    		ans = max(ans, j - i + 1)
    	return ans, cnt


    def totalFruit(self, tree: List[int]) -> int:
    	left, right = 0, 0
    	ans = 0
    	cnt = collections.defaultdict(int)
    	while right < len(tree):
    		cnt[tree[right]] += 1
    		while len(cnt) > 2:
    			cnt[tree[left]] -= 1
    			if cnt[tree[left]] == 0:
    				del cnt[tree[left]]
    			left += 1
    		ans = max(ans, right - left + 1)
    		right += 1
    	return ans

test = Solution()
print(test.totalFruit([0, 1, 2, 2])) # 3
print(test.totalFruit([1, 2, 3, 2, 2])) # 4
print(test.totalFruit([3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4])) # 5
        
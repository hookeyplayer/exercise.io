# Input: N = 3, trust = [[1,3],[2,3],[3,1]]
# Output: -1
# Input: N = 3, trust = [[1,3],[2,3]]
# Output: 3
# Input: N = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
# Output: 3
class Solution(object):
# 1
	def findJudge(self, N, trust):
		graph = {i:[] for i in range(1, N+1)}
		# 遍历字典trust
		for t in trust:
			graph[t[0]].append(t[1])
		# 若某个键的列表为空，检查是否符合法官定义
		for k in graph:
			if len(graph[k]) == 0:
				judge = k
				for person in graph:
					if person != judge and judge not in graph[person]:
						return -1
				return judge
		return -1

# 2
    def findJudge(self, N, trust):
        """
        :type N: int
        :type trust: List[List[int]]
        :rtype: int
        """
        if N == 1:
        	return 1
        d1 = {}
        d2 = {}
        for i, j in trust:
        	if j in d1:
        		d1[j] += 1
        	else:
        		d1[j] = 1
        	if i in d2:
        		d2[i] += 1
        	else:
        		d2[i] = 1
        for i, j in d1.items():
        	if j == N-1:
        		if i not in d2:
        			return i 
        return -1

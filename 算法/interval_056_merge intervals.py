class Solution(object):
# 法1.1
	def merge(self, intervals):
		"""
		:type intervals: List[Interval]
		:rtype: List[Interval]
		"""
		if not intervals:
			return
		length = len(intervals)
		if length <= 1:
			return intervals
# 		# 直接修改，且只针对列表
		intervals.sort(key=lambda x: x.start)
		pos = 0
		while pos < len(intervals) - 1:
			if intervals[pos].end >= intervals[pos+1].start:
				next = intervals.pop(pos+1)
				if next.end > intervals[pos].end:
					intervals[pos].end = next.end
			else:
				pos += 1
		return intervals
		
# 法1.2
	def merge(self, intervals):
		if intervals is None:
			return []
		intervals = sorted(intervals, key=lambda x: x.start) # 任何的sort
		res = []
		# 首个区间作为当前区间，取左右端点
		left = intervals[0].start
		right = intervals[0].end
		for item in intervals:
			if item.start <= right: # 若新区间的左端点小于当前区间的右端点，则可以合并
				right = max(right, item.end) # 取两者之较大值为新的右端点
			else:
				res.append([left, right]) # 否则，需要添加此区间
				left = item.start # 并重置端点
				right = item.end
		res.append([left, right])

		return res

# 法二
	def merge(self, intervals):
		if not intervals or not intervals[0]:
			return intervals
		intervals = sorted(intervals, key=lambda x: x[0])
		res = []
		start, end = intervals[0][0], intervals[0][1]
		for i in range(len(intervals)):
			s, e = intervals[i][0], intervals[0][1]
			if s <= end:
				end = max(end, e)
			else:
				res.append([start, end])
				start, end = s, e
		res.append([start, end])
		return res

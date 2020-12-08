class Solution(ogject):
# 1
	def insert(self, intervals, newInterval):
		if intervals is None or len(intervals) == 0:
			return [newInterval]
		intervals.sort(key=lambda x: x.start)
		pos = 0
		while pos < len(intervals):
			# left of pos
			if newInterval.end < intervals[pos].start:
				intervals.insert(pos, newInterval)
				return intervals
			# overlap
			if self.check_overlap(intervals[pos], newInterval):
				temp = intervals.pop(pos)
				newInterval = self.merge_intervals(temp, newInterval)
			else:
				pos += 1
		if len(intervals) == 0 or pos == len(intervals):
			intervals.append(newInterval)
		return intervals

	def check_overlap(self, curr_interval, new_interval):
		if curr_interval.start <= new_interval.start:
			if curr_interval.end > new_interval.start:
				return True
		else:
			if curr_interval.start <= new_interval.end:
				return True
		return False

	def merge_intervals(self, interval1, interval2):
		temp = Interval()
		temp.start = min([interval1.start, interval2.start])
		temp.end = max([interval1.end, interval2.end])
		return temp
# 2
	def insert(self, intervals, newInterval):
		intervals.append(newInterval)
		return self.merge(intervals)

	def merge(self, intervals):
		if not intervals:
			return []
		intervals = sorted(intervals, key=lambda x: x[0])
		res = []
		left = intervals[0][0]
		right = intervals[0][1]
		for item in intervals:
			if item[0] <= right:
				right = max(right, item[1])
			else:
				res.append([left, right])
				left = item[0]
				right = item[1]
		res.append([left, right])
	return res

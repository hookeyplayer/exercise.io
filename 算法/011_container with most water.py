# n个int a1, a2, ...an, 也是坐标(i, ai)
# 和x轴围成的面积最大
from typing import List
class Solution(object):
	def maxArea(self, height: List[int]) -> int:
		left, right = 0, len(height)-1
		result = 0
		while left < right:
			result = max(result, min(height[left], height[right]) * (right-left))

			if height[left] > height[right]:
				right -= 1
			else:
				left += 1
		return result


if __name__ == "__main__":
	test = Solution()
	print(test.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
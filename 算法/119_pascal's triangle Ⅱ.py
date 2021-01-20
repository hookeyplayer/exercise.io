from typing import List
# 给index，返回一行
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
    	ans = [1]
    	for i in range(1, rowIndex+1):
    		ans = list(map(lambda x,y:x+y, ans+[0], [0]+ans))
    	return ans

if __name__ == "__main__":
    test = Solution()
    print(test.getRow(4))
        
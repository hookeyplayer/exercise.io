from typing import List
# 二叉搜索树是高度平衡的，每个节点左右子树的高度差 <= 1
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
# 递归
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
    	if not nums:
    		return None
    	mid = len(nums) // 1
    	root = TreeNone(nums[mid]) # 根节点
    	root.left = self.sortedArrayToBST(nums[:mid])
    	root.right = self.sortedArrayToBST(nums[mid+1:])
    	return root        
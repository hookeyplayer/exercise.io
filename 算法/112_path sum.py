# 是否存在path使得节点和等于target
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
# 递归
# 1
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
    	if root is None:
    		return False
    	if root.left == None and root.right == None:
    		return root.val == targetSum
    	return self.hasPathSum(root.left, targetSum-root.val) or self.hasPathSum(root.right, targetSum-root.val)

# 2
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
    	if root is None:
    		return False
    	sum = targetSum - root.val
    	if sum == 0 and root.left is None and root.right is None:
    		return True
    	left = self.hasPathSum(root.left, sum)
    	right = self.hasPathSum(root.right, sum)
    	return (right or left)

        
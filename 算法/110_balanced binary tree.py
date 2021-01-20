class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
# top-down
    def isBalanced(self, root: TreeNode) -> bool:
    	if root == None:
    		return True
    	ld = self.getDepth(root.left) 
    	rd = self.getDepth(root.right)
    	if abs(ld - rd) <= 1:
    		return self.isBalanced(root.left) and self.isBalanced(root.right)
    	else:
    		return False
    def getDepth(self, root):
    	if root == None:
    		return 0
    	return max(self.getDepth(root.left), self.getDepth(root.right)) + 1
        
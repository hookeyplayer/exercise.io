class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def maxDepth(self, root):
        # 根节点是否为空
        if root is None:
        	return 0
        # 根节点不为空，则深度 >= 1
        # 递归
        ld = self.maxDepth(root.left)
        rd = self.maxDepth(root.right)
        return 1 + max(ld, rd)

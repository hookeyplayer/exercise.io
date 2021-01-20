# 最小深度：从根节点到最近叶子节点到最短路径上的节点数量
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
# 1. 递归
    def minDepth(self, root: TreeNode) -> int:
    	if root == None:
    		return 0
    	if root.left == None and root.right != None:
    		return self.minDepth(root.right)+1
    	if root.left != None and root.right == None:
    		return self.minDepth(root.left)+1
    	return min(self.minDepth(root.right), self.minDepth(root.left))+1

# 2. BFS(不会)
    def minDepth(self, root: TreeNode) -> int:
    	if root is None:
    		return 0
    	queue = [root]
    	depth, rightMost = 1, root
    	while len(queue) > 0:
    		node = queue.pop(0)
    		if node.left is None and node.right is None:
    			break
    		if node.left is not None:
    			queue.append(node.left)
    		if node.right is not None:
    			queue.append(node.right)
    		# 到达本层end
    		if node == rightMost:
    			depth += 1
    			if node.right is not None:
    				rightMost = node.right 
    			else:
    				rightMost =  node.left
    	return depth

        
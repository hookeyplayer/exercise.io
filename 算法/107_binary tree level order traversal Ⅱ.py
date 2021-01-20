# bottom-up 
# Input: [3,9,20,null,null,15,7]
# Output:
# [
# [15,7],
#   [9,20],
#   [3]
#  ]
from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
# 1.stack
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
    	if root is None:
    		return []
    	stack = [[root]]
    	ans = []
    	while len(stack) > 0:
    		top = stack.pop()
    		ans.insert(0, [t.val for t in top])
    		temp = []
    		for node in top:
    			if node.left is not None:
    				temp.append(node.left)
    			if node.right is not None:
    				temp.append(node.right)
    		if len(temp) > 0:
    			stack.append(temp)
    	return ans

# 2.queue
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
    	if not root:
    		return []
    	queue = [root]
    	ans = []
    	while queue:
    		nodes = []
    		node_values = []
    		for node in queue:
    			if node.left:
    				nodes.append(node.left)
    			if node.right:
    				nodes.append(node.right)
    			node_values += [node.val]
    		ans = [node_values] + ans
    		# 新添加的节点重新赋值给queue
    		queue = nodes 
    	return ans

# 3.按层次
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
    	ans = []
    	if root is None:
    		return []
    	self.get_level(ans, root, 0)
    	ans.reverse()
    	return ans
    def get_level(self, ans, root, depth):
    	if root is None:
    		return []
    	if depth == len(ans):
    		ans.append([])
    	ans[depth].append(root.val)
    	self.get_level(ans, root.left, depth+1)
    	self.get_level(ans, root.right, depth+1)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# 1
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
    	if root is None:
    		return True
    	return self.mirrorVisit(root.left, root.right)
    def mirrorVisit(self, left, right):
    	if left is None and right is None:
    		return True
    	try:
    		if left.val == right.val:
    			if self.mirrorVisit(left.left, right.right) and self.mirrorVisit(left.right, right.left):
    				return True
    		return False
    	except:
    		return False

# 2
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
    	def solve(p, q):
    		if p == None:
    			return q == None
    		if q == None:
    			return p == None
    		if p.val == q.val:
    			return solve(p.left, q.right) and solve(p.right, q.left)
    		return False
    	if root == None:
    		return True
    	else:
    		return solve(root.left, root.right)
        
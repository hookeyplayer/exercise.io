# Input: p = [1,2], q = [1,null,2]
# Output: false
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
    	if p == q:
    		return True
    	try:
    		l = r = True
    		if p.val == q.val:
    			l = self.isSameTree(p.left, q.left)
    			r = self.isSameTree(p.right, q.right)
    			return (l and r)
    	except:
    		return False
    	return False 
    	
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
    	# 判断是否为空
    	if not p and not q:
    		return True
    	# 判断根节点
    	if p and q and p.val == q.val:
    		l = self.isSameTree(p.left, q.left)
    		r = self.isSameTree(p.right, q.right)
    		return （l and r）
    	else:
    		return False
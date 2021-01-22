# 求入环节点
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
    	try:
    		fast = head.next.next
    		slow = head.next
    		while fast != slow:
    			fast = fast.next.next
    			slow = slow.next
    	except:
    		return None # 无cycle
    	slow = head
    	while fast != slow:
    		fast = fast.next
    		slow = slow.next
    	return fast
        
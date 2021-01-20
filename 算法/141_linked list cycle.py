# node可以再次被reach
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
# 设置快慢两个指针，步长分别为1和2
    def hasCycle(self, head: ListNode) -> bool:
    	fast = slow = head
    	while fast and fast.next:
    		fast = fast.next.next
    		slow = slow.next
    		if slow == fast:
    			return True
    	return False
# 另一种写法
    def hasCycle(self, head: ListNode) -> bool:
    	try:
    		fast = head.next.next
    		low = head.next
    		while fast != slow:
    			fast = fast.next.next
    			slow = slow.next
    		return True
    	except:
    		return False


        
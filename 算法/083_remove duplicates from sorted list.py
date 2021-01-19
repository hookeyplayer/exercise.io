# 比较相邻元素即可，相同则修改节点的next指向
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
# 1
    def deleteDuplicates(self, head: ListNode) -> ListNode:
    	if not head:
    		return head
    	b = head
    	n = head.next
    	while n != None:
    		if b.val != n.val:
    			b = n
    			n = n.next
    		else:
    			b.next = n.next
    			n = n.next
    	return head

# 2
    def deleteDuplicates(self, head: ListNode) -> ListNode:
    	if head is None:
    		return None
    	while head is not None and head.next is not None:
    		if head.val == head.next.val:
    			head.next = head.next.next
    		else:
    			head = head.next
    	return head
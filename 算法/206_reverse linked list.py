class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
# 1: recursion
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
        	return head
        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return p

# 2: iterator
	def reverseList(self, head):
		 if not head or not head.next:
        	return head
        pre, cur = None, head
        while cur:
        	temp = cur.next # savel tail
        	cur.next = pre # часть вернуть
        	pre = cur # pre позади
        	cur = temp # cur позади
        return pre

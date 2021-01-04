# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        head = cur = ListNode(0)
        while l1 or l2:
        	val = carry
        	if l1:
        		val += l1.val
        		l1 = l1.next
        	if l2:
        		val += l2.val
        		l2 = l2.next
        	cur.next = ListNode(val % 10)
        	cur = cur.next
        	carry = val / 10
        if carry > 0:
        	curr.next = ListNode(carry)
        return head.next

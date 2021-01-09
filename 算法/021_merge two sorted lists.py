# Output: [1,1,2,3,4,4]
# Definition for singly-linked list.
from typing import List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# recursion
class Solution:
    # def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    # 	if l1 and l2:
    # 		if l1.val > l2.val: l1, l2 = l2, l1
    # 		l1.next = self.mergeTwoLists(l1.next, l2)
    # 	return l1 or l2
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    	if l1 is None: return l2
    	if l2 is None: return l1
    	if l1.val <= l2.val:
    		l1.next = self.mergeTwoLists(l1.next, l2)
    		return l1
    	else:
    		l2.next = self.mergeTwoLists(l1, l2.next)
    		return l2


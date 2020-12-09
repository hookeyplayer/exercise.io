class Solution(object):
	def removeElements(self, head, val):
		"""
		:type head: ListNode
		:type val: int
		:rtype: ListNode
		"""
		if not head:
			return head
		prehead = ListNode(-1)
		prehead.next = head
		pre, cur = prehead, head
		while cur:
			if cur.val == val:
				pre.next = cur.next
				cur.next = None
				cur = pre.next
			else:
				pre = pre.next
				cur = cur.next
		return prehead.next
		
	# def removeElements(self, head, val):
	# 	if not head:
	# 		return head
	# 	prehead = ListNode(-1)
	# 	prehead.next = head
	# 	pre, cur = prehead, head
	# 	while cur:
	# 		if cur.val == val:
	# 			pre.next = cur.next
	# 		else:
	# 			pre = cur
	# 		cur = cur.next
	# 	return prehead.next

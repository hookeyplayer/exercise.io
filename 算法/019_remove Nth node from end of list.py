class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
# 法一：双指针（差n步）
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
    	p1 = p2 = head
    	index = 0
    	# p1先走n步
    	while index != n:
    		p1 = p1.next
    		index += 1
    	if p1 == None:
    		return head.next
    	# 一起走
    	while p1.next:
    		p1 = p1.next
    		p2 = p2.next
    	# p2.next就是倒数第N个节点
    	p2.next = p2.next.next
    	return head

# 另一种写法
     def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
     	if head is None:
     		return None
     	p1 = p2 = head
     	for i in range(n):
     		p1 = p1.next
     	if p1 is None:
     		head = head.next
     		return head
     	while p1.next is not None:
     		p1 = p1.next
     		p2 = p2.next
     	curr = p2.next
     	p2.next = curr.next
     	return head

# 法二：遍历，统计链表的节点总数，再遍历找到第count-n+1个节点
     def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
     	temp = head
     	count = 0
     	while temp != None:
     		count += 1
     	temp = head
     	index = 0
     	if count == n:
     		return head.next
     	else:
     		while index != (count-n-1):
     			temp = temp.next
     			index += 1
     		temp.next = temp.next.next
     		return head



class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        root = ListNode(0)
        temp = ListNode(0)
        while l1 or l2 or carry:
            v1, v2 = 0, 0

            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next

            # 和10做除法：1, 5 = divmod(15, 10)
            carry, value = divmod(v1 + v2 + carry, 10)
            temp.next = ListNode(value)
            temp = temp.next

        return root.next

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0 # 两数相加需要进位的情况
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
    
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]

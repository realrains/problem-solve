# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        curr = head
        left = l1
        right = l2

        carry = 0
        while left and right:
            val = left.val + right.val + carry
            carry = val // 10
            val = val % 10
            curr.next = ListNode(val=val)

            left = left.next
            right = right.next
            curr = curr.next
        
        while left:
            val = left.val + carry
            carry = val // 10
            val = val % 10
            curr.next = ListNode(val=val)
            curr = curr.next
            left = left.next
        
        while right:
            val = right.val + carry
            carry = val // 10
            val = val % 10
            curr.next = ListNode(val=val)
            curr = curr.next
            right = right.next
        
        if carry > 0:
            curr.next = ListNode(val=carry)
        
        return head.next

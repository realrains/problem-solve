# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast, slow = head, head

        for _ in range(n):
            fast = fast.next
        
        # when n == sz
        if not fast:
            return head.next
        
        # move sz - n times
        while fast.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return head

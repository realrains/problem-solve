# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        size = 1
        curr = head

        if not curr:
            return head

        while curr.next:
            size += 1
            curr = curr.next
        
        tail = curr
        tail.next = head

        k = k % size

        count = 0

        curr = head

        while count != size - k - 1:
            curr = curr.next
            count += 1

        head = curr.next
        curr.next = None

        return head

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nhead = None
        curr = head

        while curr:
            temp = ListNode(curr.val)
            temp.next = nhead
            nhead = temp
            curr = curr.next

        return nhead
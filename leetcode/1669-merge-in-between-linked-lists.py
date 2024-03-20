# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        start, end = list1, None

        for i in range(a-1):
            start = start.next

        end = start

        for i in range(b-a+2):
            end = end.next
        
        start.next = list2

        curr = list2
        while curr.next is not None:
            curr = curr.next
        
        curr.next = end

        return list1
        
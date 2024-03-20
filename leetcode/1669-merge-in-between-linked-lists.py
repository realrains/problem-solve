# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        l2_start = list2
        l2_end = list2

        while l2_end.next is not None:
            l2_end = l2_end.next
        
        l1_start = list1
        l1_cut_start = list1
        l1_cut_end = None

        diff = b - a

        curr = list1
        while a - 1 > 0:
            curr = curr.next
            a -= 1
        
        l1_cut_start = curr

        while diff + 1 > 0:
            curr = curr.next
            diff -= 1
        
        l1_cut_end = curr.next

        l1_cut_start.next = l2_start
        l2_end.next = l1_cut_end

        return l1_start

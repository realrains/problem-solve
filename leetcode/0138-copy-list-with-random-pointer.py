"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head
        new_head = Node(0)
        new_curr = new_head

        pt_idx = {}
        idx_pt = {}
        idx = 0

        while curr:
            new_curr.next = Node(curr.val)
            pt_idx[curr] = idx
            idx_pt[idx] = new_curr.next
            curr = curr.next
            new_curr = new_curr.next
            idx += 1
        
        new_head = new_head.next
        new_curr = new_head
        curr = head

        while new_curr:
            try:
                new_curr.random = idx_pt[pt_idx[curr.random]]
            except:
                new_curr.random = None
            new_curr = new_curr.next
            curr = curr.next
        
        return new_head

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        return self.num_to_list(self.list_to_num(l1) + self.list_to_num(l2))

    def list_to_num(self, listNode: ListNode) -> int:
        res = 0
        cnt = 1
        current_node = listNode

        while current_node is not None:
            res += current_node.val * (10 ** (cnt - 1))
            cnt += 1
            current_node = current_node.next
        
        return res
    
    def num_to_list(self, num: int) -> Optional[ListNode]:
        head = ListNode(val = num % 10)
        num = num // 10

        current_node = head
        while num > 0:
            current_node.next = ListNode(val = num % 10)
            current_node = current_node.next
            num = num // 10
        
        return head



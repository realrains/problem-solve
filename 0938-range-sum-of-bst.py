# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def traverse_sum(node: Optional[TreeNode], low: int, high: int):
    result = 0

    if (node is not None and low <= node.val <= high):
        result += node.val

    if (node.left is not None):
        result += traverse_sum(node.left, low, high)
    
    if (node.right is not None):
        result += traverse_sum(node.right, low, high)
    
    return result

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        return traverse_sum(root, low, high)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def get_max_v(node: TreeNode):
    mini = node.val
    maxi = node.val
    v = 0

    if (node.left is not None):
        a, b, c = get_max_v(node.left)
        mini = min(mini, a)
        maxi = max(maxi, b)
        v = max(v, c)
    
    if (node.right is not None):
        a, b, c = get_max_v(node.right)
        mini = min(mini, a)
        maxi = max(maxi, b)
        v = max(v, c)
    
    v = max(v, abs(mini-node.val), abs(maxi-node.val))

    return mini, maxi, v

class Solution:
    def maxAncestorDiff(self, root) -> int:
        _, _, v = get_max_v(root)
        return v
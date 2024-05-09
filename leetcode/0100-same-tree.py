# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def in_order(root: TreeNode, result: List):
            if root is None:
                result.append(None)
                return
            result.append(root.val)
            in_order(root.left, result)
            in_order(root.right, result)
        
        p_order = []
        q_order = []

        in_order(p, p_order)
        in_order(q, q_order)

        return p_order == q_order

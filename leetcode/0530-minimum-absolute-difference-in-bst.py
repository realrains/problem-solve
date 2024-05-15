# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        result = {'prev': None, 'min_diff': 999999}
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            if result['prev'] is not None:
                result['min_diff'] = min(result['min_diff'], abs(result['prev'] - root.val))
            result['prev'] = root.val
            inorder(root.right)
        inorder(root)
        return result['min_diff']

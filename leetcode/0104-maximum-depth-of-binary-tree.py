# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def dfs(node, depth, max_depth):
            if not node:
                return depth - 1
            
            return max(
                dfs(node.left, depth + 1, max_depth),
                dfs(node.right, depth + 1, max_depth),
                max_depth)
        
        return dfs(root, 1, -1)
        
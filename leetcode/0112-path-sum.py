# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def dfs(curr, curr_sum):
            if not curr:
                return False

            curr_sum += curr.val

            if curr.left is None and curr.right is None:
                return curr_sum == targetSum
            
            left, right = False, False

            if curr.left:
                left = dfs(curr.left, curr_sum)
            
            if curr.right:
                right = dfs(curr.right, curr_sum)
            
            return left or right
        
        return dfs(root, 0)

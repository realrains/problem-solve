# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        left = []
        right = []

        def preorder(node):
            if not node:
                left.append(None)
                return
            left.append(node.val)
            preorder(node.left)
            preorder(node.right)
        
        def lastorder(node):
            if not node:
                right.append(None)
                return
            right.append(node.val)
            lastorder(node.right)
            lastorder(node.left)
        
        preorder(root.left)
        lastorder(root.right)

        return left == right

        

            

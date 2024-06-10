# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        parent = {}

        def dfs(node):
            if node.left is None and node.right is None:
                return
            
            if node.left:
                parent[node.left.val] = node
                dfs(node.left)
            if node.right:
                parent[node.right.val] = node
                dfs(node.right)
        
        dfs(root)

        def path(node):
            result = [node]
            curr = node
            while curr.val in parent:
                result.append(parent[curr.val])
                curr = parent[curr.val]
            
            return result
        
        p_path = path(p)
        q_path = path(q)
        result = None
    
        while p_path and q_path:
            pv = p_path.pop()
            qv = q_path.pop()
            if pv.val == qv.val:
                result = pv
            else:
                return result

        return result

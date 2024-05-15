from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queue = deque([(1, root)])
        level_elements = []

        while queue:
            level, node = queue.popleft()
            if len(level_elements) < level:
                level_elements.append([node.val])
            else:
                level_elements[level-1].append(node.val)
            
            if node.left:
                queue.append((level+1, node.left))
            if node.right:
                queue.append((level+1, node.right))

        return [sum(elements) / len(elements) for elements in level_elements]

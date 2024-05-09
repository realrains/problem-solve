# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def buildTree(start, end) -> Optional[TreeNode]:
            if start > end:
                return None
            mid = (start + end) // 2
            root = TreeNode(val=nums[mid])
            root.left = buildTree(start, mid-1)
            root.right = buildTree(mid+1, end)
            return root
        
        nums.sort()

        return buildTree(0, len(nums)-1)

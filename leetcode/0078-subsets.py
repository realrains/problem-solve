from typing import List
    
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        visited = [False for _ in range(len(nums))]
        res = []

        def comb(n, r, target):
            if r == 0:
                res.append([nums[i] for i in range(len(nums)) if visited[i]])
                return
            if target == n:
                return
            
            visited[target] = True
            comb(n, r - 1, target + 1)
            visited[target] = False
            comb(n, r, target + 1)
        

        for r in range(len(nums) + 1):
            comb(len(nums), r, 0)
        
        return res